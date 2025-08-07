import csv
from ecommerce import Tkpd

def tkpd():
    with open('tkp.csv', 'r') as file_tokped:
        reader = csv.reader(file_tokped, delimiter=',')
        for urls in reader:
            url = urls[0]
            # print(url)
            scrap_tokped = Tkpd(url)
            scrap_tokped.get_html_pages()
            scrap_tokped.get_product_info()

tkpd()

    

        