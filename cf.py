#!/usr/bin/env python3
import requests
import re
from codeforces import lst, problem_name,url1
from bs4 import BeautifulSoup
import os
import json
from change import Utilities, supported_lang
from tqdm import tqdm
from shutil import copyfileobj
args = Utilities.mainf(supported_lang)

if args['default_lang']:
    Utilities.set_constants('default_lang', args['default_lang'])

j = 0 #cont for no.of problems
for i in tqdm(lst):
######################################## creating directoy for each problem #####################
    cwd = os.getcwd()
    path = os.path.join(cwd, problem_name[j])
    j += 1
    try: 
        os.mkdir(path) 
    except OSError as error: 
        print(error)

    os.chdir(path)

###################################################################################################
    url = i
    r = requests.get(url)
    html_cont = r.text
    # parsing every problem page
    soup = BeautifulSoup(html_cont, 'lxml')
    div = soup.find_all('div', class_ = "input")


############################# creating default language file #######################################


    with open(os.path.join(Utilities.cache_directory, 'default.json'), 'r') as f:
        # data = f.read()
        data = json.load(f)
        lan = data.get('default_lang')
        
        fname = os.path.join('/usr/local/bin/templates',"template." + lan)
        with open('sol.' + lan, 'w') as sol, open(fname, 'r') as temp:
            copyfileobj(temp,sol)
            sol.close()
            temp.close
    
#####################################################################################################

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
        
        

    os.chdir('..')