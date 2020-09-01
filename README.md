# Checking-Stock-Prices-with-Python-in-10-lines-of-code-
Nowadays it’s important to keep on checking the stock prices. Some people make millions of dollars out of stocks. So today, let’s handle the topic “Stock Prices” and let’s see how we can check them using python.

## **Importing Packages**
- “Requests” is needed so that we can retrieve pieces of information from websites
- BeautifulSoup is needed so that we can parse HTML and XML documents

## **Check_Price function**
- Let’s find a URL for any companies stock price. I prefer to use yahoo finance while working on these projects.
- We are asking “requests” to retrieve all data from our URL
- Then we parse that data with BeautifulSoup
### Notice: In the variable price your ‘class’ might be different. Use your inspect element function to figure out your ‘class’.
