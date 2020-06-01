import os
import json
import subprocess
cache_directory = os.path.join(os.path.expanduser('~'), '.cache', 'CFbot')
mv = subprocess.Popen('mv cf.py cf', shell=True, stdout=subprocess.PIPE)
chmod = subprocess.Popen('chmod +x cf', shell=True, stdout=subprocess.PIPE)
cp = subprocess.Popen('sudo cp -t /usr/local/bin cf change.py codeforces.py', shell=True,stdout=subprocess.PIPE)
cpdir = subprocess.Popen('sudo cp -r templates /usr/local/bin', shell=True, stdout=subprocess.PIPE)

stdout, stderr = mv.communicate()
stdout, stderr = chmod.communicate()
stdout, stderr = cp.communicate()
stdout, stderr = cpdir.communicate()

if not os.path.isdir(cache_directory):
        os.mkdir(os.path.join(cache_directory))
data = {'default_lang': "cpp".strip(), 'cached_directory': cache_directory}
try:
    with open(os.path.join(cache_directory, 'default.json'), 'w') as f:
        f.write(json.dumps(data, indent=2))
except OSError as error:
    print(error)

