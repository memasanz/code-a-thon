
  
from azureml.core import Run, Workspace, Datastore, Dataset
from azureml.data.datapath import DataPath
import pandas as pd
import os
import argparse


#Parse input arguments
parser = argparse.ArgumentParser("Get Inferencing Data")
parser.add_argument('--user_param', type=str, required=True)
parser.add_argument('--get_data_param_2', type=str, required=True)
parser.add_argument('--get_data_param_3', type=str, required=True)
parser.add_argument('--inferencing_dataset', dest='inferencing_dataset', required=True)

# Note: the get_data_param args below are included only as an example of argument passing.
# They are not consumed in the code sample shown here.
args, _ = parser.parse_known_args()

user_param = args.user_param
get_data_param_2 = args.get_data_param_2
get_data_param_3 = args.get_data_param_3
inferencing_dataset = args.inferencing_dataset

print(str(type(inferencing_dataset)))

#Get current run
current_run = Run.get_context()

#Get associated AML workspace
ws = current_run.experiment.workspace

#Get default datastore
ds = ws.get_default_datastore()

dataset = Dataset.get_by_name(name =user_param + '-diabetes-tabular-dataset-raw', workspace = ws)
df = dataset.to_pandas_dataframe()

cols_to_keep = df.columns
df = df[cols_to_keep]

df = df.fillna(0)

print('saving inferencing data')
# Save dataset for consumption in next pipeline step
os.makedirs(inferencing_dataset, exist_ok=True)
df.to_parquet(os.path.join(inferencing_dataset, 'inferencing_data.parquet'), index=False)
