from fuzzywuzzy import fuzz
import os
import pandas as pd
import numpy as np

os.chdir('C:/Users/adhillon/Downloads')
dirty_data=pd.read_excel("Job History Companies Clean up Process.xlsx") # file to clean-up
top_company_data=pd.read_excel('Top Companies for Clean Up.xlsx', sheet_name='Top Companies (PH 2)') # top companys

# Create Dictionary
company_dirty_list = {}
company_dirty_list['Dirty Company'] = dirty_data['Company Name'].apply(str)
company_dirty_list['Recommendation'] = np.array([np.nan]*len(dirty_data['Company Name'])).T

# create loop
for comp_unique in top_company_data['Top Hire Companies']:
    company_dirty_list[comp_unique] = [] # create list to store dictionary
    for company in dirty_data['Company Name']:
        try:
            company_dirty_list[comp_unique].append(fuzz.token_set_ratio(company,comp_unique)) # get ratio
        except float:
            company_dirty_list['Company Clean'].append('Error')

test = pd.DataFrame.from_dict(company_dirty_list) # convert to dataframe

a=[]
b=0
c=1

for rows in range(len(test)):
    try:
        company = test.columns[np.where(test[b:c]==100)[1][0]]
        a.append(company)
        b+=1
        c+=1
    except IndexError:
        a.append('Index Error')
        b+=1
        c+=1
        pass
    except TypeError:
        a.append('Type Error')
        b+=1
        c+=1
        pass

test['Recommendation'] = a

# dataframe is 200,000 rows by 20 columns
os.chdir('C:/Users/adhillon/Job History Clean Up/Recommendation')

test[0:50000].to_excel('Phase 2 Audit 1.xls', sheet_name = "Sheet1")
test[50000:100000].to_excel('Phase 2 Audit 2.xls', sheet_name = "Sheet1")
test[100000:150000].to_excel('Phase 2 Audit 3.xls', sheet_name = "Sheet1")
test[150000:200000].to_excel('Phase 2 Audit 4.xls', sheet_name = "Sheet1")
test[200000:250000].to_excel('Phase 2 Audit 5.xls', sheet_name = "Sheet1")
test[250000:281531].to_excel('Phase 2 Audit 6.xls', sheet_name = "Sheet1")
