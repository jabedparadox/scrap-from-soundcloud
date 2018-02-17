# -*- coding: utf8 -*-
# author :- 

from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib
import csv
from multiprocessing import Pool
import requests
import sys
import time
start = time.time()
g = open('links.txt')        #Reads from text file
ab = g.readlines()
bc = [z.strip(' \t\n\r') for z in ab]
import re
def reposts_count(url):
    reposts_list = []
    try:
        html = urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')
        soup = str(soup)
        #print(soup)
        name = str(re.findall('"username":"(.*?)"',soup)[0]).replace('"username":"', '')
        followers = str(re.findall('"followers_count":[0-9]+',soup)[0]).replace('"followers_count":', '')
        #cnt = b[1].strip('"reposts_count":')
        followings = str(re.findall('"followings_count":[0-9]+',soup)[0]).replace('"followings_count":', '')
        track = str(re.findall('"track_count":[0-9]+',soup)[0]).replace('"track_count":', '')
        reposts_list.extend([url,name,followers,followings,track])

    except Exception as e:
        reposts_list.extend([url,str(e)])
    print(reposts_list)
    return reposts_list
if __name__ == '__main__':
    with Pool(10) as p:
        results = p.map(reposts_count, bc)
    with open('SC-client-deails.csv', 'w', newline='') as file:
        fwriter = csv.writer(file)
        for result in results:
            fwriter.writerow(result)

