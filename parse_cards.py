#usr/bin/python
from bs4 import BeautifulSoup
import re
import csv
import codecs

#this parses the data from the cards to pull out and format only the data.


def writeOUT(data, fileLoc):                                                    
    with open(fileLoc,'a') as csvfile:                                          
        spamwriter = csv.writer(csvfile, delimiter=',')                         
        for row in data:                                                        
            if len(row) > 1:
                spamwriter.writerow([s.encode('utf-8') for s in row])



data = []
i = 1
with open('ucsf2025.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        soup = BeautifulSoup(' '.join(row))
        card_type = soup.em.get_text()
        parent_number = ' '.join(re.findall('\d+', soup.find_all("a")[0].encode('utf-8'))).split(' ')[0]
        parent_text = soup.find_all("a")[0].get_text().strip()
        card_number = ' '.join(re.findall('\d+', soup.find_all("a")[1].encode('utf-8'))).split(' ')[0]
        card_text = soup.find_all("a")[1].get_text().strip()
        card_interest = soup.find("div", class_="card-marker").get_text().strip()
        card_user_no = ' '.join(re.findall('\d+', soup.find_all("a")[2].encode('utf-8'))).split(' ')[0]
        card_user_name = soup.find_all("a")[2].get_text()
            
        data.append([card_type,parent_number,parent_text,card_number,card_text,card_interest,card_user_no,card_user_name]) 
        
        i += 1


writeOUT(data, 'cleanUCSF.csv')
        
