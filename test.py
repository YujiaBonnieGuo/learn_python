import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importting the dataset
datasets=pd.read_csv('Data.csv')
X = datasets.iloc[:,:-1].values#all columns except teh last one
