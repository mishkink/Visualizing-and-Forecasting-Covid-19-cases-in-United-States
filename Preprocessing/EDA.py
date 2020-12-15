import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

df = pd.read_csv('/Users/mishkinkhunger/Desktop/Data Viz Project2/United_States_COVID-19_Cases_and_Deaths_by_State_over_Time.csv')
df = df.drop(['created_at','consent_cases','consent_deaths'], axis=1)
duplicate_rows_df = df[df.duplicated()]
df.columns = ['Date','State','Total_cases','Confirmed_cases','Probable_cases','New_cases','Probable_newcases', 'Total_death','Confirmed_deaths',
              'Probable_death','New_Death','Probable_newdeath']
df.Date = pd.to_datetime(df.Date, dayfirst=True, errors= 'coerce')
df.index= pd.to_datetime(df.index, format='%Y/%m/%d')
df = df.set_index('Date')
df['Year'] = df.index.year
df['Month'] = df.index.month_name()
df['Weekday'] = df.index.day_name()
df = df.sort_values(by="Date")

weekday = []
for i in df['Weekday'][1:300]:
    weekday.append(i)
cases = []
for i in df['Total_cases'][1:300]:
    cases.append(i)

# plt.bar(weekday, cases)
# plt.show()

df = df[df.Month != 'January']
df = df[df.Month != 'February']

df2 = pd.read_csv('PP.csv')

print(df2.columns)
df2=df2.iloc[4:55]
df2.drop(df2.columns.difference(['State','STATE','RELIGEX','FMFINE','RSTOUTDR','NOPAYCOV','VBMAUTOBAL']), 1, inplace=True)
df_final=pd.merge(df, df2, on='State')


df_final['FMFINE'] = df_final['FMFINE'].map({1:'Yes', 0:'No'})
# df_final['FMFINE'].replace(0,'No')
df_final['RELIGEX'] = df_final['RELIGEX'].map({1:'Yes', 0:'No'})
df_final['RSTOUTDR'] = df_final['RSTOUTDR'].map({1:'Yes', 0:'No'})
df_final['NOPAYCOV'] = df_final['NOPAYCOV'].map({1:'Yes', 0:'No'})
df_final['VBMAUTOBAL'] = df_final['VBMAUTOBAL'].map({1:'Yes', 0:'No'})

# df_new2 = pd.concat(list2)
frame2 = pd.DataFrame(df_final)
frame2.to_csv('Project3.csv')

