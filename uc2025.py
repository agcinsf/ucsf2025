#usr/bin/env python

import urllib2
from bs4 import BeautifulSoup
import re
import csv

def getURL(baseURL, postNo):
    request = urllib2.Request(baseURL + str(postNo))
    response = urllib2.urlopen(request)
    html = response.read()
    soup = BeautifulSoup(html)
    return soup

def parseHTML(soup):
    try:
        soup.find("div", class_="card-play-parents-wrap").decompose()
        card =  soup.find("div", class_="card")
        card_type = card.find("div", class_="card-type").em
        card_parent = card.find("div", class_="card-parent-text").a
        card_text = card.find("div", class_="card-body").a
        card_interesting = card.find("div", class_="card-marker")
        card_user = card.find(href=re.compile("users"))
        return [card_type, card_parent, card_text, card_interesting, card_user]
    except:
        return 'a'


def writeOUT(data, fileLoc):
    with open(fileLoc,'a') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        for row in data:
            spamwriter.writerow(row)

baseURL = 'http://game.ucsf2025.org/card_plays/'
fileLoc = './2025text.csv'
dataArr = []
myArr = [] 


#here is the main process
for PostNo in range(1,100):
    soup = []
    dataArr = []

    try:
        #pull the data from the post
        soup = getURL(baseURL,PostNo) 

        #parse out the key data elements and append them to the dataArr
        dataArr = parseHTML(soup)
    except:
        a = 1
    
    if len(dataArr)>1:    
        myArr.append(dataArr)     

    #to keep me updated on the status of the job
    print PostNo

writeOUT(myArr,fileLoc)
