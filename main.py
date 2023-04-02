from linebot import LineBotApi
from linebot.models import TextSendMessage
import os
import bus_info

line_bot_api = LineBotApi(os.environ.get("CHANNEL_ACCESS_TOKEN"))

kokusai_info = bus_info.KokusaiScraper()
kokusai_result = kokusai_info.scrape()

seibu_info = bus_info.SeibuScraper()
seibu_result = seibu_info.scrape()

text = ""

def main():
    messages = TextSendMessage(text)
    line_bot_api.push_message(os.environ.get("USER_ID"), messages=messages)

if __name__ == "__main__":
    if kokusai_result is not None:
        if int(kokusai_result) > 5:
            text += "国際興業バス:" + kokusai_result + "分の遅れ" + "\n"
    if seibu_result is not None:
        if int(seibu_result) > 18:
            text += "西武バス所要時間:" + seibu_result + "分"
    if text:
        main()