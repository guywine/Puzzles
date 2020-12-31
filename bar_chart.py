import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt  

data = pd.read_csv('R1-3 results (thresh 5) - Sheet1.csv', index_col=0)

data_fractions = pd.DataFrame({'R1':data['R1_fraction'], 'R2':data['R2_fraction'], 'R3':data['R3_fraction']})
data_fractions.index = data.index

## https://pythonforundergradengineers.com/python-matplotlib-error-bars.html

