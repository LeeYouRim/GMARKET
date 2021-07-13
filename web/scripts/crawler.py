from bs4 import BeautifulSoup
import requests
import telegram
from gmarket.models import GMarket

# from datetime import datetime, timedelta

response = requests.get("http://corners.gmarket.co.kr/BestSellers?viewType=C&largeCategoryCode=100000035")
soup = BeautifulSoup(response.text, features="html.parser")
BOT_TOKEN = "1873787829:AAE5HbVTE45jeCfNiptu1D9df7HFlN4SPSA"

bot = telegram.Bot(token=BOT_TOKEN)

def run():
    # delete deals older than 3days
    # row, _ = GMarket.objects.filter(created_at__lte=datetime.now() -
    #                                              timedelta(days=3)).delete()
    # print(soup)
    for item in soup.find_all("li"):
        try:
            no = item.find("p").text
            no = int(no)
            image = item.find("img", class_="lazy").get("data-original")
            title = item.find("a", class_="itemname").text
            link = item.find("a", class_="itemname").get("href")
            price = item.find("strong").text
            sale = item.find("em").text
            if('[' in title):
                brand = title.split('[')
                brand = brand[1]
                brand = brand.split(']')
                brand = brand[0]
            else:
                brand = '없음'
            if(no <= 10):
                if(GMarket.objects.filter(title__iexact=title).count() == 0):
                    GMarket(image=image, title=title, link=link, price=price, sale=sale, brand=brand).save()
                    bot.sendMessage(-1001566905679,'{} {}'.format(title, link))
                    print(image, title, link, price, sale, no, brand)
        except Exception as e:
            continue