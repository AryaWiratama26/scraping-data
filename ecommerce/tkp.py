import bs4
import requests
import lxml
from datetime import datetime
import csv

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'
REQUEST_HEADER = {
    'User-Agent' : USER_AGENT,
    'Accept-Language' : 'en-US, en;q=0.5'
}


class Tkpd:
    def __init__(self, url):
        self.url = url
    
    
    def get_html_pages(self):
        res = requests.get(url=self.url, headers=REQUEST_HEADER)
        return res.content
    
    def get_product_price(self, soup):
        price_element = soup.find('div', attrs={
            'class' : 'price'
        })

        # return price_element
        for x in price_element:
            price = x.text.strip().replace('Rp', '').replace('.', '')
            try:
                return float(price)
            except ValueError:
                print('Value error')
                
    def get_product_title(self, soup):
        title_element = soup.find('h1', attrs={
            "class" : 'css-j63za0',
        })
        
        # return title_element
        for x in title_element:
            title = x.text.strip()
            try:
                return str(title)
            except ValueError:
                print('valur error')
                
    def get_product_description(self, soup):
        description_element = soup.find('div', attrs={
            'data-testid' : 'lblPDPDescriptionProduk'
        })
        
        # return description_element
        for x in description_element:
            description = x.text.strip().replace('\xa0', ' ')
            try:
                return str(description)
            except ValueError:
                print('value error')

    def get_product_rating(self, soup):
        rating_element = soup.find('span', attrs={
            'class' : 'css-dn7ef3',
        })
        
        if rating_element is None:
            return 0
        
        for x in rating_element:
            rating = x.text.strip()
            try:
                return float(rating)
            except ValueError:
                print('valur error')
                
    
    def get_product_info(self):
        product_info = {}
        html = Tkpd.get_html_pages(self)
        # print(html)
        soup = bs4.BeautifulSoup(html, 'lxml')
        product_info['price'] = Tkpd.get_product_price(self, soup)
        product_info['title'] = Tkpd.get_product_title(self, soup)
        product_info['description'] = Tkpd.get_product_description(self, soup)
        product_info['rating'] = Tkpd.get_product_rating(self, soup)
        print(product_info)

