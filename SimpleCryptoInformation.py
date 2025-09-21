import requests
import json
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

api_url_server_time = os.getenv("api_url_server_time")
api_url_pairs = os.getenv("api_url_pairs")
api_url_price = os.getenv('api_url_price')

def generatePrice(api):
    try:
        req_pair = input("what pair u want to search?: ")
        response = requests.get(f'{api}/{req_pair.lower()}idr')
        data = response.json()
        if 'error' not in data:
            buy_val = data['ticker']['buy']
            sell_val = data['ticker']['sell']
            time_stamp = data['ticker']['server_time']
            time_stamp_sec = time_stamp / 1000
            format_time_stamp_sec = datetime.fromtimestamp(time_stamp_sec)
            formatted_time = format_time_stamp_sec.strftime("%H:%M:%S")

            print(f"Buy is for {buy_val}")
            print(f"Sell is for {sell_val}")
            print(f"This data is generated on {format_time_stamp_sec}")
        else:
            print("Pair not exist")
    except Exception as e:
        print(e)

generatePrice(api_url_price)