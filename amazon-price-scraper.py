import sys
import bs4, requests, pyperclip

amazon_price_css_selector = '.header-price'


def getAmazonPrice(product_url):
    print('product url: ', product_url)
    if len(product_url) <= 1:
        return 'Please enter a amazon product url'
    res = requests.get(product_url)
    res.raise_for_status()
    price = price_text_from_res(res)
    return price

def price_text_from_res(res):
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    price_elem = soup.select(amazon_price_css_selector)
    price_string = price_elem[0].text.strip()
    return price_string

print('starting...')
product_url = ''
if len(sys.argv) > 1:
    product_url = ' '.join(sys.argv[1:])
else:
    product_url = pyperclip.paste()

price = getAmazonPrice(product_url)
print('Price is: ', price)

