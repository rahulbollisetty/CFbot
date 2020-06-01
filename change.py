import argparse
import sys
import os
import json

flags = {}
# default_lang = 'cpp'
supported_lang = {'c', 'cpp', 'py'}


# code for changing default language

class Utilities:
    # cache_directory = os.getcwd()
    cache_directory = os.path.join(os.path.expanduser('~'), '.cache', 'CFbot')
        
    @staticmethod
    def mainf(supported_lang):
        parser = argparse.ArgumentParser()
        parser.add_argument("--l", type=str, dest ='default_lang',choices=supported_lang,
                                help='What is your preferred lang?(enter the extension)')
        args = parser.parse_args()
        flags['default_lang'] = args.default_lang
        return flags
    @staticmethod   
    def set_constants(key, value):
            """
            Utility method to set default site and contest
            """
            with open(os.path.join(Utilities.cache_directory, 'default.json'), 'r+') as f:
                data = f.read()
                data = json.loads(data)
                data[key] = value
                f.seek(0)
                f.write(json.dumps(data, indent=2))
                f.truncate()

args = Utilities.mainf(supported_lang)
if args['default_lang']:
    Utilities.set_constants('default_lang', args['default_lang'])
