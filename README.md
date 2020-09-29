# Checking-Stock-Prices-with-Python-in-10-lines-of-code-
Nowadays it’s important to keep on checking the stock prices. Some people make millions of dollars out of stocks. So today, let’s handle the topic “Stock Prices” and let’s see how we can check them using python.

## **Importing Packages**

``` python
import requests
from bs4 import BeautifulSoup
```
- “Requests” is needed so that we can retrieve pieces of information from websites
- BeautifulSoup is needed so that we can parse HTML and XML documents

## **Check_Price function**
- Let’s find a URL for any companies stock price. I prefer to use yahoo finance while working on these projects.
- We are asking “requests” to retrieve all data from our URL
- Then we parse that data with BeautifulSoup

``` python
def check_price():
    url = 'https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch'
    get_url_response = requests.get(url)
    parse_response = BeautifulSoup(get_url_response.text, 'lxml')
    price = parse_response.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    print(price)
```

### Notice: In the variable price your ‘class’ might be different. Use your inspect element function to figure out your ‘class’.

## **Calling our function**

```python
while True:
    check_price()
    
    ```
- We are using "while True", so that we get updated stock prices!

# **End**

- Thanks for checking out my story on how to check stock prices using Python. Hopefully, you gained some knowledge and good luck with your stocks ;)
Also check out my medium: https://medium.com/@michelangelo.foschi.10
