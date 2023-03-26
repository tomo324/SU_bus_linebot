from bs4 import BeautifulSoup
import requests
import re

class KokusaiScraper:
    def __init__(self):
        self.site = 'https://transfer.navitime.biz/5931bus/pc/location/BusLocationResult?startId=00021176&goalId=00021229'

    def scrape(self):
        res = requests.get(self.site)
        soup = BeautifulSoup(res.text, 'html.parser')
        if 'delay-minutes-area' in res.text:
            delay_minutes = soup.find('div', class_='delay-minutes-area')
            span_tag = delay_minutes.find('span', class_='middleText')
            for x in span_tag:
                string = x.string
                if string == '遅れなし':
                    return None
                else:
                    num = re.findall(r'\d+', string) #(約○分の遅れ)の数字部分を取り出す
                    num = num[0]
                    return num
        return None



class SeibuScraper:
    def __init__(self):
        self.site = 'https://transfer.navitime.biz/seibubus-dia/pc/location/BusLocationResult?startId=00111628&goalId=00111643'

    def scrape(self):
        res = requests.get(self.site)
        soup = BeautifulSoup(res.text, 'html.parser')
        if 'dnvPane' in res.text:
            delay_minutes = soup.find('div', class_='dnvPane')
            div_tag = delay_minutes.find_all('div')
            txt_list = [x.string for x in div_tag]
            string = txt_list[3]
            num = re.findall(r'\d+', string)
            num = num[0]
            return num
        return None
