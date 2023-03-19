import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.iplt20.com/auction/2022#:~:text=204%20players%20were%20sold%20and,IPL)%202022%20Auction%20in%20Bengaluru.'
r = requests.get(url)
# print(r)

soup = BeautifulSoup(r.text,'lxml')
# print(soup.prettify())

table = soup.find('table',class_='ih-td-tab auction-tbl')
# print(table)
title = table.find_all("th")

# print(title)
header = []
for i in title:
    name = i.getText()
    header.append(name)
# print(header)

rows = table.find_all('tr')
# print(rows)
df = pd.DataFrame(columns=header)
for i in rows[1:]:
    first_td = i.find_all("div",class_="ih-pt-ic")[0].text.strip()
    print(first_td)
    data = i.find_all("td")[1:]
    row = [tr.text for tr in data]
    row.insert(0,first_td)
    # print(row)
    l= len(df)

    df.loc[l] = row

print(df)
df.to_csv("ipl Action stats.csv")