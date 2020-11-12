Copyright 2020 Google Inc.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

# BERT for Patents

The BERT exported here has been trained on >100 million patent documents and was trained on all parts of a patent (abstract, claims, description).

The BERT model exported here comes in two formats:

* [SavedModel](https://storage.googleapis.com/patents-public-data-github/saved_model.zip)

* [Checkpoint](https://storage.googleapis.com/patents-public-data-github/checkpoint.zip)

The models can also be loaded and saved in another format or just the weights can be saved.

The BERT model has been trained on >100 million patent documents and was trained on all parts of a patent (abstract, claims, description). It has a similar configuration to the BERT-Large model, with a couple of important notes:

* The maximum input sequence length is 512 tokens and maximum masked words for a sequence is 45.
* The vocabulary has approximately 8000 added words from the standard BERT vocabulary. These represent frequently used patent terms.
* The vocabulary includes "context" tokens indicating what part of a patent the text is from (abstract, claims, summary, invention). Providing context tokens in the examples is optional.

The full BERT vocabulary can be downloaded [here](https://storage.googleapis.com/patents-public-data-github/bert_for_patents_vocab_39k.txt). The vocabulary also contains 1000 unused tokens so that more tokens can be added.

The exact configuration for the BERT model is as follows (and downloaded [here](https://storage.googleapis.com/patents-public-data-github/bert_for_patents_large_config.json)):

* attention_probs_dropout_prob: 0.1
* hidden_act: gelu
* hidden_dropout_prob: 0.1
* hidden_size: 1024
* initializer_range: 0.02
* intermediate_size: 4096
* max_position_embeddings: 512
* num_attention_heads: 16
* num_hidden_layers: 24
* vocab_size: 39859

The model has requires the following input signatures:
1. `input_ids`
2. `input_mask`
3. `segment_ids`
4. `mlm_ids`

And the BERT model contains output signatures for:
1. `cls_token`
2. `encoder_layer` is the contextualized word embeddings from the last encoder layer.
3. `mlm_logits` is the predictions for any masked tokens provided to the model.
