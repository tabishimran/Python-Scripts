#!/usr/bin/python
#!/usr/bin/env python

#simple script to look for and download videos from YT, parameters are provided via arguments, you can select the video acording to size,format
#resolution etc. I have to add an option to download audio only. And have to polish up the code a little bit, its 5:52 am and the holiday was well
#used.

import mechanize
import pafy
from bs4 import BeautifulSoup as bs
from sys import argv

i=0
q=len(argv)
query=""
for i in range(1,len(argv)):
    query=query+str(argv[i])+" "

print("Searching for \""+query+"\" :")

search_url="https://www.youtube.com/results?search_query="+query.replace(" ","+")
list=[]
res_list=[]
size_list=[]
ext_list=[]
i=0

br=mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_referer(False)
br.set_handle_refresh(False)
br.addheaders=[('User-agent','Firefox')]
br.open(search_url)
soup=bs(br.response().read())
for link in soup.find_all('a'):
    if "watch" in str(link.get('href')):
        list.append(str(link.get('href')))

dl="https://www.youtube.com"+str(list[0])
video=pafy.new(dl)
print("\n\nDownloading : "+video.title)
streams = video.streams
for s in streams:
    i=i+1
    ext_list.append(s.extension)
    res_list.append(s.resolution)
    size_list.append(s.get_filesize())

l=0
print("Select File ->")
for l in range(0,i):
	print(str(l+1)+"> "+str(ext_list[l])+" | "+str(res_list[l])+" | "+str("{0:.2f}".format(size_list[l]/(1024.0*1024.0)))+"Mb"+" |")

print("\n----------")
choice=input()
if(choice==0 or choice>i):
    exit()

choice=choice-1
best = video.getbest(preftype=str(ext_list[choice]))
filename = best.download(filepath="/home/txjoe/Downloads/"+video.title +"."+best.extension)
