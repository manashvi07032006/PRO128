from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page = requests.get(url)

soup = bs(page.text, 'html.parser')

star_table = soup.find_all('table', {"class": "wikitable sortable"})

total_table = len(star_table)
temp = []
table_rows = star_table[2].find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp.append(row)

Star_names = []
Distance =[]
Mass = []
Radius =[]

print(temp)

for i in range(1,len(temp)):

    Star_names.append(temp[i][0])
    Distance.append(temp[i][5])
    Mass.append(temp[i][7])
    Radius.append(temp[i][8])

headers = ['Star_name', 'Distance', 'Mass' , 'Radius']
df2 = pd.DataFrame(list(zip(Star_names, Distance, Mass, Radius)), columns=['Star_names', 'Distance', 'Mass', 'Radius'])
print(df2)

df2.to_csv('dwarf_stars.csv', index=True, index_label='id')