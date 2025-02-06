import requests
from bs4 import BeautifulSoup
import smtplib


# URL of the product
url = 'https://www.amazon.in/iPhone-16-Pro-Max-256/dp/B0DGJJM5HZ/ref=sr_1_2?crid=1J9SG8PB5PTX6&dib=eyJ2IjoiMSJ9._2x8IUpCs9yuvr42V7LJno07jGeJTJcJNdKEUV9p03RSIS2Wn3LPAUPSIpEiPKU4k4mJknAUIzStYdUebQTQd8xz1uQceP_QfwCrping_IkdIh7rWkdoRD8kWGALpKH5dCMI0S4uS17Jsqs0gKwUZWaoOB1xYRPjs9Eb0K_Pjqs7ZmUWj-AreMgBWPVUO2H1uTIFjp0s46y74htuzX6jFAQpFRHv7CC35SpTGBqiOlM.Qrd0XoYg8oF7gaBrt1jzD9rO2tO0h83XZsDmwkPimdE&dib_tag=se&keywords=iphone+16pro+max&nsdOptOutParam=true&qid=1738678503&sprefix=iphone%2Caps%2C301&sr=8-2'


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
