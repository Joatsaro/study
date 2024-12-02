import bs4
import requests
def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.paser')
    elems = soup.select("#corePrice_feature_div > div > span > span:nth-child(2)")
    elems[0].test.strip()


price = getAmazonPrice('http://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/')
print('The price is' + price)