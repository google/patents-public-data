# BigQuery column indexer

This tool supports indexing and normalizing various columns in BigQuery tables.
It reads an input BigQuery SQL statement to select the columns and outputs a new
BigQuery table with the indexed columns.


# Running locally (development)

Build the runner container image with RDKit and Beam dependencies installed. Install the gcloud SDK and authenticate.

```
$ podman --cgroup-manager=cgroupfs build ./beam-rdkit-runner --format docker
...
STEP 14: COMMIT
--> 49b365fef6f
$ podman run -it --entrypoint "/bin/bash" -v .:/opt/bigquery-indexer 49b365fef6f
(beam-env) root@94bb44368d14$ wget https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-352.0.0-linux-x86_64.tar.gz
(beam-env) root@94bb44368d14$ tar -xzf google-cloud-sdk-352.0.0-linux-x86_64.tar.gz
(beam-env) root@94bb44368d14$ google-cloud-sdk/install.sh
(beam-env) root@94bb44368d14$ gcloud init
(beam-env) root@94bb44368d14$ gcloud auth application-default login
(beam-env) root@94bb44368d14$ cd /opt/bigquery-indexer && python3 -m main --input_sql "SELECT * FROM nih-nci-cbiit-chem-prod.savi.all LIMIT 100" --output_table <project>:savi.fingerprints --project <project> --temp_location gs://<cloud storage bucket>/tmp/ --skip_fingerprint_columns reaction_smiles
```

# Running in Dataflow on GCP

```
$ pip install 'apache-beam[gcp]=2.31.0'
```

See https://cloud.google.com/dataflow/docs/quickstarts/quickstart-python,
specifically setting GOOGLE_APPLICATION_CREDENTIALS is required.

Use your local GCP account credentials by executing:

```
$ gcloud init
$ gcloud auth application-default login
```

Build the runner container.

```
patents-public-data$ cd tools/bigquery-indexer/beam-rdkit-runner
beam-rdkit-runner$ gcloud builds submit --tag gcr.io/<project>/beam-rdkit-runner:latest
```

This example indexes a column containing SMILES (the computer representation of a chemical).

```$ python3 -m main --input_sql "SELECT * FROM nih-nci-cbiit-chem-prod.savi.all LIMIT 100" --output_table <project>:savi.fingerprints --project <project> --temp_location gs://<cloud storage bucket>/tmp/ --skip_fingerprint_columns reaction_smiles --runner DataflowRunner --max_num_workers=20 --region us-central1 --machine_type=n2-highcpu-16 --disk_size_gb=50 --experiment=use_runner_v2 --sdk_container_image=gcr.io/<project>/beam-rdkit-runner:latest --save_main_session```

See more configuration flags at https://cloud.google.com/dataflow/docs/guides/flexrs and regions at https://cloud.google.com/dataflow/docs/resources/locations.
