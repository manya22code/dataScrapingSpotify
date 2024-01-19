import pandas as pd
from bs4 import BeautifulSoup
import requests
url='https://en.wikipedia.org/wiki/List_of_most-streamed_artists_on_Spotify'
page=requests.get(url)
soup=BeautifulSoup(page.text,features='html.parser')

soup.find('table')
table=soup.find_all('table')[4]
print(table)
alltitles=table.find_all('th')
print(alltitles)
seperated_all_titles=[title.text.strip() for title in alltitles]
print(seperated_all_titles)
heading=seperated_all_titles[0:4]
df=pd.DataFrame(columns=heading)
print(df)
column_data=table.find_all('tr')
for row in column_data[1:len(column_data)-1]:
    ranking=row.find_all('th')
    row_data=row.find_all('td')
    individual_row_data=[data.text.strip() for data in row_data]
    ranking_data=[data.text.strip() for data in ranking]
    complete_data=ranking_data+ individual_row_data
    length=len(df)
    df.loc[length]=complete_data
df.to_csv(r"spotifydatascraping.csv",index=False)

    
