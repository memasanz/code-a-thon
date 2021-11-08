
from azureml.core import Run, Workspace, Datastore, Dataset
from azureml.core.model import Model
from azureml.data.datapath import DataPath
import pandas as pd
import os
import argparse
import joblib
import json
import joblib
import numpy as np
from azureml.core.model import Model
import time
import pandas as pd
import azureml.core
from azureml.core import Workspace, Dataset
import os
import math


# Parse input arguments
parser = argparse.ArgumentParser("Score Inferencing Data")
parser.add_argument('--model_name_parm', type=str, required=True)
parser.add_argument('--scored_dataset', dest='scored_dataset', required=True)

args, _ = parser.parse_known_args()
model_name = args.model_name_parm
scored_dataset = args.scored_dataset

# Get current run
current_run = Run.get_context()

# Get associated AML workspace
ws = current_run.experiment.workspace

# Get default datastore
ds = ws.get_default_datastore()

# Get inferencing dataset
inferencing_dataset = current_run.input_datasets['inferencing_data']
inferencing_data_df = inferencing_dataset.to_pandas_dataframe()


print('inferencing data df shape:' + str(inferencing_data_df.shape))

print('model_name' + model_name)

# Get model from workspace - the code below will always retrieve the latest version of the model; specific versions can be targeted.
model_list = Model.list(ws, name=model_name, latest=True)
model_path = model_list[0].download(exist_ok=True)
model = joblib.load(model_path)


print(inferencing_data_df.shape)



# Make predictions with new dataframe
predictions = model.predict(inferencing_data_df)

inferencing_data_df['Predictions']=predictions

# Save scored dataset
os.makedirs(scored_dataset, exist_ok=True)
print(scored_dataset)

inferencing_data_df.to_parquet(os.path.join(scored_dataset, 'scored_data.parquet'), index=False)
