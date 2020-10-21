[![HitCount](http://hits.dwyl.com/rahulbollisetty/CFbot.svg)](http://hits.dwyl.com/rahulbollisetty/CFbot)
# CFbot
Downloads the test cases from CODEFORCES and adds templates for selected default language(c, cpp, python)
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Things you need to have before installing this bot.
```
python3
```

```
pip3
```
```
git
```

### Installing

##### From Source

**For linux**

```
git clone https://github.com/rahulbollisetty/CFbot
```
```
cd CFbot
```
To install all dependencies used, enter:
```
pip3 install -r requirements.txt
```
To setup the initial folders and executabe files enter:
```
python3 initial.py
```
Default language is set to cpp , to change the default to (**py** or **c** or **cpp**) enter:
```
python3 change.py --l {extension of your desired language}
```
For example, to change the default language to c:
```
python3 change.py --l c
```
**Note**- In order to change the default language you need to be in the CFbot directory

## Running the bot

The bot is designed in such a way that you need not to have the scripts in your working directory,
to run the bot enter

```
cf
```
You will be asked the contest id, so enter the last numeric digits of the respective contest url
**For example**, if your respective contest site is https://codeforces.com/contest/1347 , then **1347** is the id you need to enter
```
$enter the contest id
1347
```


## Built With

* [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - The Python  module used to parse the website
* [Requests](https://requests.readthedocs.io/en/master/) - Used to send HTTP requests
* [tqdm](https://tqdm.github.io/) - Used to add progress bar
* [lxml](https://lxml.de/) - Parser

## Author

* **B Rahul** - [rahulbollisetty](https://github.com/rahulbollisetty)

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/rahulbollisetty/CFbot/blob/master/LICENSE) file for details
