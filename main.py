#!/usr/bin/python3

import sys
import requests
from bs4 import BeautifulSoup

#Iphone's User-Agent is to evade CloudFlare
headers = {
  'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1',
  'Referer': 'https://noidea.ip',
  'Origin': 'https://noidea.ip'
}

def link_validation(url):

  print('')

  if 'grabify.link' in url:
    print('[+] Looks like a grabiy link')
  else:
    print("[-] Doesn't look like a grabify link")
    sys.exit(1)

  response = requests.get(url, headers=headers)

  print('')

  if response.status_code == 200:
    print('[+] URL works')
    return response
  else:
    print('[-] Url does not work')
    sys.exit(1)

def get_url(content, url):

  final_url = content.url

  print('')

  if final_url not in url:
    print(f'Ready! URL: {final_url}')
  else: 
    #If it has smart logger
    soup = BeautifulSoup(content.content, 'html.parser')
    result = soup.find('meta', {'name':'url'}).get('content','')
    print(f'Ready! URL: {result}')

if __name__ == '__main__':

  url = input('Type the url: ')

  r = link_validation(url)

  get_url(r, url)
