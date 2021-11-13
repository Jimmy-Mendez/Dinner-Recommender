# import libraries
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

# specify the url
url = "http://google.com/search?q=Skampa+Cambridge"

# Connect to the website and return the html to the variable ‘page’
try:
    req = Request(url, headers={'User-Agent':'Mozilla/5.0'})
    page = urlopen(req)
    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(page, 'html.parser')
    # Take out the <div> of name and get its value
    content = soup.find("div", {"class":"BNeawe tAd8D AP7Wnd"})
    article = ''
    if content is not None:
        article = content
        print(article)
    else:
        print("None")
    # Saving the scraped text
    with open('scraped_text.txt', 'w') as file:
        file.write(str(article))
except:
    print("Error opening the URL")

