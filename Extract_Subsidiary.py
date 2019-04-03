import pandas as pd
import wikipedia as wp

Top_Company = ['Alphabet','Apple']

my_tables = {} # dataframe to store results

for company in Top_Company:
    html = wp.page("List of mergers and acquisitions by "+str(company)).html().encode("UTF-8") # Get the html source
    my_tables[company] = pd.read_html(html)[0]
    my_tables[company]
    new_header = my_tables[company].iloc[0]
    my_tables[company]=my_tables[company][1:]
    my_tables[company].columns = new_header
    my_tables[company]['Top Company'] = str(company)
