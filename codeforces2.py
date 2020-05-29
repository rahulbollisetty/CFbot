import requests
import re
from codeforces import lst, problem_name,url1
from bs4 import BeautifulSoup
import os

# create a directory for the contest id

cwd = os.getcwd()
path = os.path.join(cwd, url1)
try: 
    os.mkdir(path) 
except OSError as error: 
    print(error)    
os.chdir(path)

j = 0 #cont for no.of problems
for i in lst:
    url = i
    r = requests.get(url)
    html_cont = r.text
    # parsing every problem page
    soup = BeautifulSoup(html_cont, 'lxml')
    div = soup.find_all('div', class_ = "input")
    # creating directoy for each problem

    cwd = os.getcwd()
    path = os.path.join(cwd, problem_name[j])
    j += 1
    try: 
        os.mkdir(path) 
    except OSError as error: 
        print(error)

    os.chdir(path)
    
    # finding input div
    for inp in  div:
        
        pre = inp.find('pre')
        
        for i in pre.select('br'):
            i.replace_with('\n')
        print(pre.text.strip().strip('\n').strip())
    print(str(os.getcwd()))
    os.chdir('..')
    print(str(os.getcwd()))
#great now remove whitespaces and store them in a array or so