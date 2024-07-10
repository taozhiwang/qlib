

# Introduction

What is GeneralPtNN
- Fix previous design that fail to support both Time-series and tabular data
- Now you can just replace the Pytorch model structure to run a NN model.

We provide an example to demonstrate the effectiveness of the current design.
- `workflow_config_gru.yaml` align with previous results [GRU(Kyunghyun Cho, et al.)](../README.md#Alpha158 dataset)
- `workflow_config_mlp.yaml` align with previous results [MLP](../README.md#Alpha158 dataset)

# TODO

We will align existing models to current design.