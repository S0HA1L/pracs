#!/bin/python
from selenium import webdriver
from bs4 import BeautifulSoup
from collections import defaultdict
from time import sleep
from dotenv import load_dotenv

import chromedriver_autoinstaller
import re
import os
import requests
import pprint
import json
import argparse

class BROWSER: # selenium browser initilization
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--window-size=1420,1080')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.browser = webdriver.Chrome(chromedriver_autoinstaller.install(),chrome_options=chrome_options)


class COMMON: # Common function for all classes
    def __init__(self):pass

    def error(self, code):# Error handler
        try:return eval(code)
        except:pass

    def handle(self,var,val):
        try:return eval(val)
        except Exception as e:
            print(e,val)
            return None

class GITHUB: # Nologin BeautifulSoup used
    def __init__(self,name):
        self.url=f'https://github.com/{name}'
        self.rslt=defaultdict(dict)
        self.soup=BeautifulSoup(requests.get(self.url).content,'html5lib')
        self.cm=COMMON()
        self.mine()
    
    def mine(self):
        self.rslt['Profile']=self.soup.find('img',src=re.compile(r'https://avatars.githubusercontent.com/u/.*')).get('src').replace('s=64','s=100')
        self.rslt['Name']=[n.strip() for n in self.soup.find('h1',{'class':'vcard-names'}).text.split('\n') if n.strip()]
        self.rslt['Social']=list(set([n.get('href').replace('mailto:','') for n in self.soup.find_all('a',href=re.compile(r'(https://twitter.com/.*|https://www.linkedin.com/in/.*|mailto:.*|https://t.me/.*|https://www.instagram.com/.*|https://www.facebook.com/.*|https://www.pinterest.com/.*|https://www.reddit.com/user/.*)'))]))
        self.rslt['About']=[n.strip() for n in self.soup.find('div',{'class':'js-profile-editable-area d-flex flex-column d-md-block'}).get_text('\n').split('\n') if n.strip()]
        self.rslt['Achivements']=self.cm.handle(self.soup,"[{n.get('alt'):n.get('src')} for n in var.find('div',{'class':'border-top color-border-secondary pt-3 mt-3 d-none d-md-block'}).find_all('img',src=re.compile(r'^https://github.githubassets.com/.*'))]")
        self.rslt['Organizations']=self.cm.handle(self.soup,"[{'https://github.com'+n.get('href'):json.loads(n.get('data-hydro-click')).pop('payload')} for n in var.find('div',{'class':'border-top color-border-secondary pt-3 mt-3 clearfix hide-sm hide-md'}).find_all('a',{'data-hovercard-type':'organization'})]")
        self.rslt['Projects']=self.cm.handle(self.soup,"[[m.strip() for m in n.text.split(\n) if m.strip()] for n in var.find('ol',{'class':'d-flex flex-wrap list-style-none gutter-condensed mb-4 js-pinned-items-reorder-list'}).find_all('div',{'class','pinned-item-list-item-content'})]")
        try:self.rslt['Activity']['Commits'],self.rslt['Activity']['Created']=[[{re.sub(r"\n.*\n?"," - ",m.text.replace(' ','').strip()):f"https://github.com{m.find('a',href=True).get('href')}"} for m in n.find_all('li') if m.text.replace(' ','').strip()] for n in self.soup.find('div',{'id':'js-contribution-activity'}).find_all('ul',{'class':'list-style-none mt-1'})]
        except:self.rslt['Activity']['Commits'],self.rslt['Activity']['Created']=None,None



class MINE:
    def __init__(self,username):
        self.username=username
        self.rslt=defaultdict(dict)

    def mine(self):
        #self.rslt['facebook']=FACEBOOK(self.username).rslt # verified
        #self.rslt['linkedin']=LINKEDIN("harishanbalagan").rslt # verified
        self.rslt['github']=GITHUB(self.username).rslt # verified
        # self.rslt['instagram']=INSTAGRAM(self.username).rslt # Test in windows Not used
       # self.rslt['pinterest']=PINTEREST(self.username).rslt # verified
      #  self.rslt['twitter']=TWITTER("theflutterboi").rslt # verified
        # self.rslt['tiktok']=TIKTOK(self.username).rslt # Not used
       # self.rslt['reddit']=REDDIT(self.username).rslt # verified
        open(f'{self.username}.json','w').write(json.dumps(self.rslt,indent=4))






if __name__=='__main__':
    load_dotenv()
    arg=argparse.ArgumentParser(description='SociaLod Social media informations scrapper by username matches')
    arg.add_argument('-u',dest='username',help='Social media common username')
    opt=arg.parse_args()
    MINE(f'{opt.username}').mine()



