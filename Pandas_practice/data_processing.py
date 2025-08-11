import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

data={'name':['Sachin','Suraj','Pratik','Dhiraj','Shubham'],'Age':[27,31,27]}
def data_cleaning():
    print("Lets Learn Data Processing")
    vehicle_data=pd.read_csv("../Data_Files/Electric_Vehicle_Population_Data.csv")
    print(vehicle_data.shape)
    


if __name__=="__main__":
    data_cleaning()