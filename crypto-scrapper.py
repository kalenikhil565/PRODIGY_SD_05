import requests
from bs4 import BeautifulSoup

def crypto_price(coin_name):
    url = 'https://www.google.com/search?q=' + (coin_name) + 'price'
    HTML = requests.get(url)
    soup = BeautifulSoup(HTML.text, 'html.parser')
    coin_price = soup.find('div', attrs={
        'class': 'BNeawe iBp4i AP7Wnd'
    }).find({
        'div': 'BNeawe iBp4i AP7Wnd'
    }).text
    return coin_price

user_input = input("Enter the coin name: ")
price =crypto_price(user_input)
print(f'{user_input} price : ' + price)