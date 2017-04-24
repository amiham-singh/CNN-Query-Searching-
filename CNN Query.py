from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

import nltk
from newspaper import Article
from nltk import FreqDist

#%%
def cnn(u):#Check to see if it is CNN.com
    if "http://www.cnn.com/" in u:
        return True
    else:
        return False
turn = '0'
while turn == '0':
    topic = input('Enter the topic[one word only] ')
    sec = input ("Enter the section you want to search in: us | world | politics | opinions | health | entertainment | travel | style | tech: ") 
    year = input ("Enter the year for query ")
    month = input ("Enter the month number for query eg, 01 for JAN and 12 for DEC: ")
    section = '/'+sec.lower()+'/'
    
    regex = '.*'+topic.lower()+'*'
    p = re.compile(regex)# Regex to match the query in the link         
    url = "http://www.cnn.com/sitemaps/sitemap-articles-" + year +'-' + month +".xml" # Link to CNN's SiteMap based on the time frame from user
    
    r = requests.get(url)
    
    data = r.text
    
    soup = BeautifulSoup(data, "xml")
    links =[]
    links= [x.text for x in soup.findAll("loc") if cnn(x.text) if p.match(x.text) if section in (x.text)]
    
    if links ==[]:
        print("Couldn't find results. Try a diffrent section.\n\n")
        turn = '0'
    else: 
        turn = '1'

tokens = []
authors = []
stopwords = nltk.corpus.stopwords.words('english')
stopwords.append("n't")
stopwords.append("'s")
stopwords.append(",")
stopwords.append("``")
punc = ['!',"''",'"',"'",'#','$','%','^',"&",'*','(',')','{',']','}','[',':',':','.','/','?','<','>','~','`','@','!','\\','|']
for link in links: 
    article = Article(url=link)
    article.download()
    article.parse()
    
    text = article.text
    author = article.authors
    for author in author:
        authors.append(author)
    
    words = nltk.word_tokenize(text)
    l_tokens = [w.lower() for w in words]
    t = [w for w in l_tokens if w not in stopwords and w not in punc]
    for i in t:
        tokens.append(i)


freqdist = FreqDist(tokens)
items = freqdist.most_common(30)

freqdistAuthor = FreqDist(authors)
bylines = freqdistAuthor.most_common(3)

topbylines = [x for (x,y) in bylines]
topwords = [x for (x,y) in items[:5]]

print("There are " + str(len(links)) + " results for your query.\n\n")


print ("Top authors for your topic: ")
for auth in topbylines:
    print(auth)

print("\n\nThe following are the top five words used in the articles about your query: ")
for x in topwords:
    print(x)
    
