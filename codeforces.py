import requests

import re

from bs4 import BeautifulSoup
print("paste the url of contest")
url = str(input())
r = requests.get(url)
html_cont = r.text
soup = BeautifulSoup(html_cont, 'html.parser')
table = soup.find('table', class_= "problems")
lst = []
j = url.replace("https://codeforces.com", "") + "/problem/"
print(j)
for i in table.find_all("td", class_ = "id"):
    a = i.find('a')
    b = url + "/problem/" + a['href'].replace(j, "")
    lst.append(b)
    print(b)
#good now store these links in an array
# for i in lst:
#     print(i)