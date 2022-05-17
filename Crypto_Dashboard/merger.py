import pandas as pd
import numpy as np
import json

# read in coinburea json
df1 = pd.read_json('Data/coinbureau.json')
df2 = pd.read_json('Data/forbes.json')
df3 = pd.read_json('Data/moneyweb.json')

metadat_df1 = df1['metadata'].values  # a list of dictonaries
source_list = []
read_time_list = []
category_list = []
for dic in metadat_df1:
    source_list.append(dic['source'])
    read_time_list.append(dic['readtime'])
    category_list.append(dic['category'])
df1['source'] = source_list
df1['read_time'] = read_time_list
df1['category'] = category_list
df1 = df1.drop(columns='metadata',axis=0)
metadata_df2 = df2['metadata'].values # a list of dictionaries
source_list2 = []
author_list = []
views_2 = []
summary_list = []
for dic in metadata_df2:
    source_list2.append(dic['source'])
    author_list.append(dic['author'])
    views_2.append(dic['views'])
    summary_list.append(dic['summary'])
df2['source'] = source_list2
df2['author'] = author_list
df2['views'] = views_2
df2['summary'] = summary_list
# df1['source'] = ['Coin Bureau'for i in range(len(df1))]
# df2['source'] = ['Forbes'for i in range(len(df2))]
# df3['source'] = ['Moneyweb'for i in range(len(df3))]
# # stack dataframes on top of each other
# df_stack = pd.concat([df1,df2,df3],axis=0)

print(df1)