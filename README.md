code-a-thon
===========

intro-into-leveraging-aml

Signing up for a free account & setup an Azure ML Workspace: [Azure Account Signup and AML Workspace Deployment](CodeAThon.md)

This is a source code repo demonstrating how to use Azure ML - but don't forget about AutoML.  

![Graphical user interface, text Description automatically generated](media/e77c38939932afe3b27c7da9a98ee6c4.png)


About this Repository:
----------------------

Data can be found in the data folder, these sample notebooks are working with
parquet files with Azure ML.

-   [001_model_train_notebook.ipynb](001_model_train_notebook.ipynb) - Training
    a basic model with no AML

-   [002_local_model_train_with_aml.ipynb](002_local_model_train_with_aml.ipynb)

    -   Training a basic model leveraging an AML experiment

-   [003_compute_cluster_train.ipynb](003_compute_cluster_train.ipynb) -
    Training a model leveraging AML Computer Cluster

-   [004_DeployToACI.ipynb](004_DeployToACI.ipynb) – Deploying a model to ACI

-   [005_inference_pipeline-parquet.ipynb](005_inference_pipeline-parquet.ipynb)
    – Inferencing Pipeline

Great Resources
---------------

### Training Materials

<https://github.com/MicrosoftLearning/mslearn-dp100>

<https://github.com/Azure-Samples/Synapse/tree/main/Notebooks/PySpark>

### Using Modin

<https://docs.microsoft.com/en-us/azure/machine-learning/concept-optimize-data-processing>

<https://medium.com/distributed-computing-with-ray/how-to-speed-up-pandas-with-modin-84aa6a87bcdb>

<https://modin.readthedocs.io/en/latest/>

### Using batch endpoints

<https://docs.microsoft.com/en-us/azure/machine-learning/how-to-use-batch-endpoints-studio>
