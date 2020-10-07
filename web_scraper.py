import smtplib
import time
import requests
from bs4 import BeautifulSoup

#Function to convert the price of the product
def convert_price(price):
    #remove currency sign and the space 
    s_price = price[2:]
    #remove the decimal part
    s_price = new.split('.')
    s_item_price = new[0]
    
    item_price = s_item_price.split(',')
    converted_price = item_price[0]+item_price[1]
    converted_price = int(converted_price)
    return converted_price

#Function to send the mail
def send_email(title, price_item1):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('sendertestid@gmail.com', 'qccvyvjcryuhvodd')
    subject = 'Hey! the price of item you wishlisted is finally down'
    body = 'Your product '+ title + ' is now available at the price of ' + str(price_item1) + ' Check the product at : https://www.amazon.in/Apple-iPhone-XR-128GB-Black/dp/B07JG7DS1T/ref=sr_1_2?dchild=1&keywords=iphone&qid=1602000723&s=electronics&sr=1-2' 
    
    message = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'sendertestid@gmail.com',
        'receivertestid@gmail.com',
        message
    )
    print('Email has been sent')
    server.quit()

URL = 'https://www.amazon.in/Apple-iPhone-XR-128GB-Black/dp/B07JG7DS1T/ref=sr_1_2?dchild=1&keywords=iphone&qid=1602000723&s=electronics&sr=1-2'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}

#Function to check wheather the price of the product has dropped less than or equal to our budget
def check_price():
    page = requests.get(URL, headers = headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    title = soup.find(id = "productTitle").get_text()
    price = soup.find(id = "priceblock_ourprice").get_text()
    price_item1 = convert_price(price)
    if(price_item1>=45000):
        send_email(title, price_item1)
        
while(True):
    check_price()
    time.sleep(60*60*24)    