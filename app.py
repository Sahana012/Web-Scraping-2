from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page = requests.get(url)
print(page)

soup = BeautifulSoup(page.text,'html.parser')

star_table = soup.find_all('table')
print(len(star_table))

star_list= []
table_rows = star_table[4].find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    star_list.append(row)
print(star_list)


Star_names = []
Distance =[]
Mass = []
Radius =[]

for i in range(1,len(star_list)):
    Star_names.append(star_list[i][0])
    Distance.append(star_list[i][5])
    Mass.append(star_list[i][7])
    Radius.append(star_list[i][8])

df = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,)),columns=['Star_name','Distance','Mass','Radius'])
print(df)

df.to_csv('dwarf_stars.csv')