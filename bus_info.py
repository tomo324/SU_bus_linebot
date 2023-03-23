from bs4 import BeautifulSoup
import requests

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
                    print(string)
                else:
                    print(string[2]) #(約1分の遅れ)の数字部分を取り出す



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
            num = ''.join(filter(str.isdigit, string))
            print(num)



kokusai_scraper = KokusaiScraper()
kokusai_scraper.scrape()

seibu_scraper = SeibuScraper()
seibu_scraper.scrape()