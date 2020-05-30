#!/usr/bin/env python3
import requests
import re
from bs4 import BeautifulSoup

url1 = str(input())
url = "https://codeforces.com/contest/" + url1
r = requests.get(url)
html_cont = r.text
# parsing the url

soup = BeautifulSoup(html_cont, 'html.parser')
table = soup.find('table', class_= "problems")
lst = []

# dynamic url

j = url.replace("https://codeforces.com", "") + "/problem/"
problem_name = []

# fetching url of every problem

for i in table.find_all("td", class_ = "id"):
    a = i.find('a')
    # fetching problem name
    problem_name.append(a['href'].replace(j,""))
    b = url + "/problem/" + a['href'].replace(j, "")
    # storing problem links
    lst.append(b)
    print(problem_name)
