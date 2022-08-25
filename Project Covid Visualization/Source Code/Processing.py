import pandas as pd 
import numpy as np
import os 

print(os.listdir("D:\\Zoom_HK3_2021\\Data visualization\\data"))
column_component = [
 'TotalCases',
 'NewCases',
 'TotalDeaths',
 'NewDeaths',
 'TotalRecovered',
 'NewRecovered',
 'ActiveCases',
 'Serious,Critical',
 'Tot Cases/1M pop',
 'Deaths/1M pop',
 'TotalTests',
 'Tests/ 1M pop ',
 'Population',
 'Continent']


def CombineMultiTable (Country):
 FileInFolder = os.listdir("D:\\Zoom_HK3_2021\\Data visualization\\data")
 source = ""
 dataFrame = pd.DataFrame(columns = column_component)
 date = []
 for i in range(len(FileInFolder)):
     date.append(FileInFolder[i][:-4])

     df = pd.read_csv(os.path.join("D:\Zoom_HK3_2021\Data visualization\data\\",FileInFolder[i]))
     country_index = df.index[df['Country,Other'] == 'World'].tolist()
     dataFrame.loc[i] = list(df[column_component].iloc[country_index[0]])
 return dataFrame , date
df , date = CombineMultiTable("VietNam")
df['Date'] = date
df[['NewCases',
 'TotalDeaths',
 'NewDeaths',
 'TotalRecovered',
 'NewRecovered',
 'ActiveCases',
 'Serious,Critical']].astype(int)
df.to_csv('World_new.csv',header=True,index=False)
 
#  return