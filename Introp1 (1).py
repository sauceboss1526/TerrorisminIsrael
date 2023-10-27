"""introduction to variables in terrorism dataset for project 1 of DAV5400

Returns:
    shape: shape of dataset 
    nullstypes: sum of null values among attributes and data types in the dataset 
    numdesc: creates a list of the numerical variables in the dataset and prints a description of numerical variables in the dataset
"""
import numpy as np 
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 

class intro: 
    def __init__(self, dfpath):
        self.df = pd.read_csv(dfpath)
    
    def shape(self):
        shape = self.df.shape
        return shape

    def nullstypes(self):
        nulls = self.df.isnull().sum()
        types = self.df.dtypes
        return types, nulls
    
    def numdesc(self):
        num_var = [i for i in self.df.select_dtypes(exclude = object) if i != 'terrorist' and i != 'date']
        return self.df[num_var].describe().transpose()
    
    
