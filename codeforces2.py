import requests

import re
from codeforces import lst
from bs4 import BeautifulSoup
#print("enter url of problem")
for i in lst:
    url = i
    r = requests.get(url)
    html_cont = r.text
    soup = BeautifulSoup(html_cont, 'lxml')
    div = soup.find_all('div', class_ = "input")
    for inp in  div:
        #print(inp.getText())
        pre = inp.find('pre')
        # print(pre.get_text())
        for i in pre.select('br'):
            i.replace_with('\n')
        print(pre.text.strip().strip('\n').strip())
#great now remove whitespaces and store them in a array or so