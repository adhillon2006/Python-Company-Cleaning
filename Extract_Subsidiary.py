import pandas as pd
import wikipedia as wp

Top_Company = ['Alphabet','Apple']

for company in range(0,len(Top_Company)):
    html = wp.page("List of mergers and acquisitions by "+ Top_Company[company]).html().encode("UTF-8") # Get the html source
    df = pd.read_html(html)[0]
    new_header = df.iloc[0]
    df = df[1:]
    df.columns = new_header
    df['Top Company'] = Top_Company[company]
