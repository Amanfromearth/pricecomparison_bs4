from bs4 import BeautifulSoup
import requests

querry = input("Enter Product name: ")
querry.replace(" ","+")

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'
}

url_amazon = "https://www.amazon.in/s?k="+querry
url_flipkart = "https://www.flipkart.com/search?q="+querry

content_amazon = requests.get(url_amazon ,headers = headers).text
content_flipkart = requests.get(url_flipkart).text

soup_amazon = BeautifulSoup(content_amazon, 'html.parser')
soup_flipkart = BeautifulSoup(content_flipkart, 'html.parser')
print("<<<<Flipkart>>>>")
try:
    print(f'Product Name: {soup_flipkart.find(class_="s1Q9rs").text}')
    print(f'Product Price: {soup_flipkart.find(class_="_30jeq3").text}')
except:
    print(f'Product Name: {soup_flipkart.find(class_="_4rR01T").text}')
    print(f'Product Price: {soup_flipkart.find(class_="_30jeq3 _1_WHN1").text}')
print("<<<<Amazon>>>>")
print(f'Product Name: {soup_amazon.find(class_="a-size-medium a-color-base a-text-normal").text}')
print(f'Product Price: {soup_amazon.find(class_="a-offscreen").text}')