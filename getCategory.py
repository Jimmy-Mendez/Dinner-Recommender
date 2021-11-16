from urllib.request import Request, urlopen
import pandas as pd
from bs4 import BeautifulSoup
import re

def getCategory(data, name_var, addr_var):
    data['category'] = ""
    count = 0
    for restaurant in data[name_var]:
        url_head = "http://google.com/search?q="
        name_string=data.at[count,name_var].replace(',','%2C').replace('\'','%27').replace(' ','+')
        addr_string=data.at[count,addr_var].replace(',','%2C').replace('\'','%27').replace(' ','+')
        url = url_head+name_string+addr_string
        try:
            req = Request(url, headers={'User-Agent':'Mozilla/5.0'})
            page = urlopen(req)
            # parse the html using beautiful soup and store in variable `soup`
            soup = BeautifulSoup(page, 'html.parser')
            # Take out the <div> of name and get its value
            content = soup.find("div", {"class":"BNeawe tAd8D AP7Wnd"})
            article = "None"
            category = ''
            if content is not None:
                article = str(content)
            if ')</span> </span>' in article:
                category = article.split(')</span> </span>')[1] 
                category = category.replace('</div>','').replace('\n','')
            # Saving the scraped text
            data.at[count,'category'] = category
        except:
            data.at[count,'category'] = "NA"
        count+=1
    return data 

