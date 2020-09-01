import requests
from bs4 import BeautifulSoup
def check_price():
    url = 'https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch'
    get_url_response = requests.get(url)
    parse_response = BeautifulSoup(get_url_response.text, 'lxml')
    price = parse_response.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    print(price)
while True:
    check_price()
