import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as sc
import math 
from statistics import mode
import warnings
warnings.filterwarnings('ignore')


disney = pd.read_csv("D:/INFORMATICA-Proyectos/Bootcam_data_platform/demo_bootcamp/data/disney_plus_titles.csv")
netflix = pd.read_csv("D:/INFORMATICA-Proyectos/Bootcam_data_platform/demo_bootcamp/data/netflix_titles.csv")
amazon = pd.read_csv("D:/INFORMATICA-Proyectos/Bootcam_data_platform/demo_bootcamp/data/amazon_prime_titles.csv")


#Añadimos una columna para identificar la fuente de los datos
netflix['platform']='netflix'
amazon['platform']='amazon'
disney['platform']= 'disney'

df=pd.concat([netflix,amazon,disney],ignore_index=True)
df['date_added'] = df['date_added'].str.strip()
df['date_added']= pd.to_datetime(df['date_added'], format='%B %d, %Y')

movies_ntf=netflix[netflix['type']=='Movie']
movies_pie_ntf = movies_ntf.groupby('country').size().rename_axis('Country').reset_index(name='Count')
movies_top5_ntf = movies_pie_ntf.sort_values(by='Count',ascending=False).head(5)

movies_amz=amazon[amazon['type']=='Movie']
movies_pie_amz = movies_amz.groupby('country').size().rename_axis('Country').reset_index(name='Count')
movies_top5_amz = movies_pie_amz.sort_values(by='Count',ascending=False).head(5)
movies_top5_amz['Country'] = movies_top5_amz['Country'].str.replace('United Kingdom, United States','UK, USA')

movies_dis=disney[disney['type']=='Movie']
movies_pie_dis = movies_dis.groupby('country').size().rename_axis('Country').reset_index(name='Count')
movies_top5_dis = movies_pie_dis.sort_values(by='Count',ascending=False).head(5)
 

#Removemos los Nulls 
df['country'].fillna(df['country'].mode()[0],inplace=True)
df['director'].fillna('Unknown',inplace=True)
df['rating'].fillna('Unknown',inplace=True)
df['duration'].fillna('Unknown',inplace=True)
df['cast'].fillna('Unknown',inplace=True)
mean_date_added = df['date_added'].mean()
df['date_added']=df['date_added'].fillna(mean_date_added)

df=df.dropna()
