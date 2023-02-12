import sys
import requests
import smtplib
import re
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


#Create new function for current price, create header to avoid website blocking
def current_price(x):
    #Define URL to access to
    url = "https://www.tigerdirect.com/applications/SearchTools/item-details.asp?EdpNo=1501390"
    # Create header to avoid blocking from the website
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15'}
    # Sending the request and storing the website on a variable
    page = requests.get(url, headers=header)
    # Create a beautifulsoup object
    soup = BeautifulSoup(page.text, 'html5lib')
    #Select a span of clas "sr-only" that goes after all the other variables with their corresponding class to reach the current price
    cp = soup.select('div.pdp-price > p.final-price > span.sale-price > span.sr-only')

    return cp


#Create new function for current price, create header to avoid website blocking
def list_price(x):
    # Define URL to access to
    url2 = "https://www.tigerdirect.com/applications/SearchTools/item-details.asp?EdpNo=1501390"
    #Create header to avoid blocking from the website
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15'}
    # Sending the request and storing the website on a variable
    page = requests.get(url2, headers=header)
    # Create a beautifulsoup object
    soup = BeautifulSoup(page.text, 'html5lib')
    #Select a span of clas "sr-only" that goes after the paragraph of class "list-price" after the div of class "pdp-price"
    print(title)

#Print the current price as a string from the link specified
print(current_price("https://www.tigerdirect.com/applications/SearchTools/item-details.asp?EdpNo=1501390"))
current_price = str(
    current_price("https://www.tigerdirect.com/applications/SearchTools/item-details.asp?EdpNo=1501390"))
#Print the list price as a string from the link specified
print(list_price("https://www.tigerdirect.com/applications/SearchTools/item-details.asp?EdpNo=1501390"))
list_price = str(list_price("https://www.tigerdirect.com/applications/SearchTools/item-details.asp?EdpNo=1501390"))
#Using RegEx, from the string names "current_price", replace "and" for "."
a = re.sub('and', '.', current_price)
#From the new string stored in variable "a", remove everything that's not a number
b = re.sub("[^0-9.]", '', a)
#Using RegEx, from the string names "list_price", replace "and" for "."
c = re.sub('and', '.', list_price)
#From the new string stored in variable "a", remove everything that's not a number
d = re.sub("[^0-9.]", '', c)
print('List Price:', d)
print('Current Price:', b)

#### PART 2
def maine():
    #Configuring the request to appear natural with headers
    headers = {'User-agent': 'Mozilla/5.0'}
    #Writing the url of the website we want to webscrap from
    url= "https://www.usnews.com/"
    #Requesting the website
    page = requests.get(url, headers=headers)
    # Creating a beautifulsoup object
    soup = BeautifulSoup(page.text, 'html5lib')
    # Looking for any article ("a") that comes after heading level 3
    news = soup.select("h3 > a")
    #print(news)  #to see all the articles that appear and specify the link that we need (the second link)
    news_2 = (news[1]['href'])
    # print(news_2)
    print(news_2)
    # Configuring the request to appear natural with headers
    headers = {'User-agent': 'Mozilla/5.0'}
    # Writing the url of the website we want to webscrap from
    url2 = news_2
    # Requesting the website
    page2 = requests.get(url2, headers=headers)
    # Create a beautifulsoup object
    soup = BeautifulSoup(page2.text, 'html5lib')
    # Finding headings level 1
    news_22 = soup.select("h1")
    # Selecting the heading we want to display
    print(news_22[0].text)
  # Finding all sentences from the specified class
    threeLine = soup.find_all('div', {'class': 'Raw-slyvem-0 bCYKCn'})
    # Selecting the three first sentences
    for i in range(0, 3):
        print({threeLine[i].text})


if __name__ == '__main__':
    # Displaying the function "maine"
    maine()


