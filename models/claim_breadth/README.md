# Measuring Patent Claim Breadth Using Google Patents Public Data on BigQuery

The code in this repository is one approach to measuring patent claim breadth
using a semi supervised approach. For more details and background, please see
[this post on the Google Cloud Big Data
Blog.](https://cloud.google.com/blog/big-data/2018/06/measuring-patent-claim-breadth-using-google-patents-public-datasets)

## Prerequisites

#### Setup a Google Cloud Project and Install the gcloud sdk

Much of the code in this repository requires access to a Google Cloud Project.
Please setup an account before proceeding. To install gcloud, follow the guide
[here](https://cloud.google.com/sdk/docs/quickstarts). Then once its installed,
setup your sdk to reference your account:

`gcloud init`

#### Create a bucket where you'll store relevant data for this project and set some environmental variables.

Each of the steps below relies on Google Cloud Storage for various tasks like
writing logs or output files. You'll need your own bucket to run the steps below
or if you'd like to run only one portion of the steps. You can use our public
bucket gs://patent-claims-data which includes all the relevant input and output
files

```
export GCP_PROJECT=`gcloud config get-value project`
export BUCKET=gs://[YOUR BUCKET NAME]
gsutil mb $BUCKET
```

#### Enable relevant API's in the GCP console.

Dataflow and cloud ML require several api's to be enabled on your account.
Before running the examples below, you'll need the following two API's enabled:

1.  https://console.cloud.google.com/apis/library/dataflow.googleapis.com
2.  https://console.cloud.google.com/apis/library/ml.googleapis.com

#### Create a service account, download your keys and set a local environmental variable.

To do this follow [this
guide](https://cloud.google.com/docs/authentication/getting-started) for setting
the GOOGLE_APPLICATION_CREDENTIALS environmental variable.

`export GOOGLE_APPLICATION_CREDENTIALS="[PATH TO DOWNLOADED JSON FILE]"`

#### Setup a virtual environment and install python dependencies.

Additionally, you'll likely want to work inside a python virtual environment.
You can set one up with the following commands:

```
virtualenv myenv
source myenv/bin/activate
pip install -r requirements.txt
```

## A few sample commands

Below are a handful of sample commands that can be used as a reference on how to
run the scripts in this repository. For more info, see the blog post mentioned
above. Please note that all of the commands below will incur charges on your GCP
account. Most of the commands can be run for less than a dollar at current
prices, but hyperparameter tuning can easily become very expensive if you run
many trials. Consider setting [billing alerts and
limits](https://cloud.google.com/billing/docs/how-to/budgets) before running any
of the commands below.

### To run preprocessing pipeline and produce 1.4m training examples.

```
export OUTPUT_PATH="$BUCKET/training-data/"
python preprocess.py \
  --output_path=$OUTPUT_PATH \
  --project=$GCP_PROJECT \
  --runner=DataflowRunner \
  --pipeline_mode=train \
  --query_kep_pct=0.6 \
  --cpc_code_list='D,E,F,G,H'
```

### To run a local training job for a few steps to ensure your model trains.

#### First, set up a vocab file for an embedding column in the model

The model has an embedding column which is designed to embed CPC codes at the 4
digit level which allows the model to learn differences in feature impact across
technologies (i.e. a claim of the same length might be narrower in one subspace
than in another.)

To generate a vocab file, the simplest way is to run a query against the Google
Patents Public Data on BigQuery and save the output to a text file which we put
on GCP storage. To do this follow the commands below:

```
# Execute a query from the command line and pipe output to text file.
bq --project=$GCP_PROJECT query --max_rows=100000 --format=csv "$(cat generate_embedding_vocab.sql)" > ./cpc_embedding_vocab.txt
# Strip header and blank lines.
sed -i '2 d' cpc_embedding_vocab.txt
sed -i '/^\s*$/d' cpc_embedding_vocab.txt
# Copy to GCS for use in training and remove local copy.
gsutil cp ./cpc_embedding_vocab.txt $BUCKET
rm ./cpc_embedding_vocab.txt
```

#### Launch the local training job.

```
export CPC_EMBEDDING_VOCAB_FILE="$BUCKET/cpc_embedding_vocab.txt"
export GCS_TRAIN_FILES="$BUCKET/training-data/claim-data-train*.tfrecord.gz"
export GCS_EVAL_FILES="$BUCKET/training-data/claim-data-eval*.tfrecord.gz"
gcloud ml-engine local train \
 --package-path trainer \
 --module-name trainer.task \
 --job-dir './test' \
 -- --train-files $GCS_TRAIN_FILES \
    --eval-files $GCS_EVAL_FILES \
    --cpc-embedding-vocab-file $CPC_EMBEDDING_VOCAB_FILE \
    --train-steps 100 \
    --train-batch-size=10 \
    --eval-batch-size=10
```

### To run Hyperparameter Tuning and select the best model parameters (CAN BE EXPENSIVE).

Note - running this command can incur significant charges due to the number of
trials running. Make sure you have billing alerts and budgets set up to avoid
unexpected charges.

```
export JOB_NAME=tuning_$(date +"%s")
export GCS_JOB_DIR="$BUCKET/hptuning/$JOB_NAME"

gcloud ml-engine jobs submit training $JOB_NAME \
  --config hptuning_config.yaml \
  --runtime-version 1.6 \
  --job-dir $GCS_JOB_DIR \
  --module-name trainer.task \
  --package-path trainer/ \
  --region us-central1 \
  -- --train-steps 50000 \
     --train-files $GCS_TRAIN_FILES \
     --eval-files $GCS_EVAL_FILES \
     --cpc-embedding-vocab-file $CPC_EMBEDDING_VOCAB_FILE
```

### To run a cloud training job for 30000 steps with the default Hparams.

```
export JOB_NAME=patent_claims_$(date +"%s")
export GCS_JOB_DIR="$BUCKET/models/$JOB_NAME"

gcloud ml-engine jobs submit training $JOB_NAME \
  --scale-tier STANDARD_1 \
  --runtime-version 1.6 \
  --job-dir $GCS_JOB_DIR \
  --module-name trainer.task \
  --package-path trainer/ \
  --region us-central1 \
  -- --train-steps 30000 \
     --train-files $GCS_TRAIN_FILES \
     --eval-files $GCS_EVAL_FILES \
     --cpc-embedding-vocab-file $CPC_EMBEDDING_VOCAB_FILE
```

While your training job is running, logs will be written to GCS and you can
monitor progress with tensorboard using the command below. Note, because you're
fetching logs from GCS - there is some latency between starting tensorboard and
seeing results.

`tensorboard --logdir $GCS_JOB_DIR`

### To run preprocessing pipeline and produce input data to run inference on all pubs after 1995 in a D, E, F, G, or H class code:

```
export OUTPUT_PATH="$BUCKET/inference-data"
python preprocess.py \
--output_path=$OUTPUT_PATH \
--project=$GCP_PROJECT \
--runner=DataflowRunner \
--pipeline_mode=inference \
--cpc_code_list='D,E,F,G,H'
```

### Set up Your Model on Cloud ML

In a previous step, we trained a model and saved the final model to GCS. In the
next step, we'll use this model for batch inference by leveraging GCP's Cloud
ML. To use this service, we need to configure a model for online inference. To
read more about this, see [this
doc](https://cloud.google.com/ml-engine/docs/tensorflow/prediction-overview).

If you've been following along so far, the following commands will grab the
trained model files from GCP and set up a model version on cloud ML:

```
export MODEL_NAME=patent_claims
export VERSION='v1'
export SAVED_MODEL=`gsutil ls -d "$GCS_JOB_DIR/export/model/[0-9]*/"`
gcloud ml-engine models create $MODEL_NAME
gcloud ml-engine versions create $VERSION --model $MODEL_NAME --origin $SAVED_MODEL --runtime-version=1.4
export MODEL_VERSION_STR="$MODEL_NAME/versions/$VERSION"
```

### Run batch inference against all US Pubs in a D, E, F, G, or H class code.

Now that we have a model ready for predictions, we can run batch inference. Note
that the number of workers will affect how many requests are made against your
model's API.

```
export OUTPUT_PATH="$BUCKET/scored"
export INPUT_FILE_PATTERN="$BUCKET/inference-data/*.tfrecord.gz"
python ./batch_inference.py \
  --model_version_str=$MODEL_VERSION_STR \
  --input_file_pattern=$INPUT_FILE_PATTERN \
  --output_path=$OUTPUT_PATH \
  --num_workers=5 \
  --project=$GCP_PROJECT \
  --write_to_bigquery=True \
  --output_dataset='sandbox' \
  --output_table='claim_scores' \
  --runner=DataflowRunner
```

## Useful Links

The following links are helpful resources for understanding concepts covered in
this repository.

-   [Apache Beam programming
    guide](https://beam.apache.org/documentation/programming-guide/)
-   [Detailed overview of using estimators to train a model locally and on
    GCP.](https://github.com/amygdala/code-snippets/blob/master/ml/census_train_and_eval/using_tf.estimator.train_and_evaluate.ipynb)
-   [Overview of hyperparameter
    tuning](https://cloud.google.com/ml-engine/docs/tensorflow/hyperparameter-tuning-overview)
