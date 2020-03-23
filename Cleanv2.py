import os, re
import pandas as pd
import numpy as np
from cleanco import cleanco

# Setting up path/file
path_1 = r'C:\Users\adhillon\Downloads'
file_name = 'Job Apps - Applications (MASTER) - Trend export 2020-01-08 08_52 PST.xlsx'
os.chdir(path_1)
df = pd.read_excel(file_name,sheet_name='Details View')

# Standardize columns
df['current_company_normalize'] = df['Current Company'].str.upper()
df['current_company_normalize'] = df['current_company_normalize'].str.replace(' - ', ' ')
df['current_company_normalize'] = df['current_company_normalize'].str.replace('-', ' ')
df['current_company_normalize'] = df['current_company_normalize'].str.replace(' – ', ' ')
df['current_company_normalize'] = df['current_company_normalize'].str.replace(',', ' ')
df['current_company_normalize'] = df['current_company_normalize'].str.replace(':', ' ')
df['current_company_normalize'] = df['current_company_normalize'].str.replace(' @ ', ' AT ')
df['current_company_normalize'] = df['current_company_normalize'].str.replace(' ARTIFICIAL INTELLIGENCE ', ' AI ')
df['current_company_normalize'] = df['current_company_normalize'].str.replace('.', '')
df['current_company_normalize'] = df['current_company_normalize'].str.replace(r"'", '')
df['current_company_normalize'] = df['current_company_normalize'].str.replace(r"’", '')
df['current_company_normalize'] = df.current_company_normalize.str.replace(r"\(.*\)","")
df['current_company_normalize'] = df.current_company_normalize.str.replace(' AND ', ' & ')
df['current_company_normalize'] = df['current_company_normalize'].str.replace(' GEORGIA TECH ', ' GEORGIA INSTITUTE OF TECHNOLOGY ')
df['current_company_normalize'] = df['current_company_normalize'].apply(lambda x: cleanco(str(x)).clean_name())
# df['current_company_normalize'] = df.current_company_normalize.str.encode('utf-8')
countries = ['INDIA', 'INDIA PVT', 'INDIA PRIVATE', 'PVT']
for country in countries:
    df['current_company_normalize'] = df.current_company_normalize.apply(lambda x: x.replace(country, '') if (type(x)==str and x.endswith(country)) else x)
df['current_company_normalize'] = df.current_company_normalize.str.strip()


# View dataset
100*(1-(len(df['current_company_normalize'].unique())/len(df['Current Company'].unique())))

df.to_excel('Normalized_Company_3.xlsx')
