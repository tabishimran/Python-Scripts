#!/usr/bin/python

import mechanize
from bs4 import *
from sys import argv

br=mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3'),
('accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')]

url_list=[]
completed_list=[]
new_list=[]
display_list=[]

if len(argv)<2:
    print("\nTURTLE CRAWL 1.0 Lame web crawler \n\nUsage : ./tcrawl.py [options] <url> \n\nOPTIONS ->\n\n    -r : recursive -> crawl ectracted links too\n    -l : limited -> don't crawl links out of the domain given by user \n    -i : crawl the url given as parameter and quit\n\n")
    exit(1)

main_url="http://"+argv[2]
url_list.append(main_url)

def get_links(url):                                        #scrape a page, get urls, add to url list, add crawled page to completed list
    if(".com" not in url):
        url=main_url+url
    print("\n\nCrawling : "+url+"\n\n")
    completed_list.append(url)
    try:
        response=br.open(url)
    except:
        print("[*] Failed to crawl -> "+url+"\n")
        return
    soup=BeautifulSoup(response)
    for link in soup.find_all('a'):
        new_list.append(link.get('href'))
    for x in new_list:
        if len(x)>4:
            url_list.append(x)


def clean_list():
    list=[]
    for elements in url_list:
        if ".com" not in elements:
            list.append(main_url+elements)
        else:
            list.append(elements)
    return list


if(argv[1]=="-r"):
    print("\n\n> Staring Recursive Crawl ")
elif(argv[1]=="-l"):
    print("\n\n> Staring Limited Crawl ")
elif(argv[1]=="-i"):
    print("\n\n> Staring single Crawl ")
else:
    print("\nWrong option selected \nYou need help \n")
    exit()

try:
    get_links(main_url)
    list=clean_list()
    for x in list:
        display_list.append(x)
        print("> "+x)
except:
    print("\nBye")
    exit()

try:
    if(argv[1]=="-r"):
        print("\n\n>>Adding new urls to crawl list \n\n")
        for item in list:
            if item not in completed_list:
                get_links(item)
                list=clean_list()
                for i in list:
                    if(i not in display_list):
                        print("> "+i)

except:
    print("\nBye")
    exit()
