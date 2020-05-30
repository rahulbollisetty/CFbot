#!/usr/bin/env python3
import requests
import re
from codeforces import lst, problem_name,url1
from bs4 import BeautifulSoup
import os
from ch import Utilities
# importing the cache_directory for default language
x = Utilities.cache_directory
print(str(x))
print("enter the contest id")
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
    # creating directoy for each problem
    cwd = os.getcwd()
    path = os.path.join(cwd, problem_name[j])
    j += 1
    try: 
        os.mkdir(path) 
    except OSError as error: 
        print(error)

    os.chdir(path)

    url = i
    r = requests.get(url)
    html_cont = r.text
    # parsing every problem page
    soup = BeautifulSoup(html_cont, 'lxml')
    div = soup.find_all('div', class_ = "input")
    
    count = 0 #count for number of input
    # finding input div
    for inp in  div:
        
        pre = inp.find('pre')
        inputf = open('input' + str(count) + '.txt', 'w')

        for i in pre.select('br'):
            i.replace_with('\n')
        x = pre.text.strip().strip('\n').strip()
        inputf.write(''.join(x))
        inputf.close()
        count += 1
        # print(x)

    count = 0 #count for number of output

    div = soup.find_all('div', class_ = "output")
    for inp in  div:
        
        pre = inp.find('pre')
        outputf = open('output' + str(count) + '.txt', 'w')

        for i in pre.select('br'):
            i.replace_with('\n')
        x = pre.text.strip().strip('\n').strip()
        outputf.write(''.join(x))
        outputf.close()
        count += 1
        # print(x)


    os.chdir('..')
