import pandas as pd
from ydata_profiling import ProfileReport

data=pd.read_csv("C:/Users/Taran/Desktop/KrishiAi/Raw Data Soil Fettility.csv")
print(data.head(),"\n")
print(data.info(),"\n")

profile=ProfileReport(data)
# profile.to_widgets()
profile.to_file("Soil_Data.html")
# we have no catagorical values
print(data.describe(),"\n")

# There are no null values
print(data.isna().sum())
print(data.nunique())
print(data['fertility'].value_counts())
print(" 0- Describes low fertility\n 1- describes moderate fertility\n 2- describes good fertility")

