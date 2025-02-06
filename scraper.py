import requests
from bs4 import BeautifulSoup
import smtplib


# URL of the product
url = '<add-amazon-URL>'


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


def check_price():
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')


    price = soup.find('span', class_='a-price-whole')  
    
    if price:
        price = price.get_text()
        return price.strip()
    else:
        return None




def send_telegram_notification(price):
    bot_token = '7566648525:AAH334KcFwswp5YIgugBAUQ8mVgNWv_j3og'
    chat_id = '<your-chat-id>'
    message = f"The price has dropped! The current price is: rupees {price}"
    
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {'chat_id': chat_id, 'text': message}
    
    response = requests.post(url, data=data)
    print(f"Telegram notification sent! The price is {price}")

import requests

def main():
    current_price = check_price()
    required_price = float(input("enter desired price"))

    current_price = current_price.replace(",", "").replace(".", "").strip()  

    if (float(current_price) < required_price):
        print(f"Current price: {current_price}")
        send_telegram_notification(current_price)



            

if __name__ == "__main__":
    main()
