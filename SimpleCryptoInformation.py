import requests
import json
import os
from dotenv import load_dotenv

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
            print(f"Buy is for {buy_val}")
            print(f"Sell is for {sell_val}")
        else:
            print("Pair not exist")
    except Exception as e:
        print(e)

generatePrice(api_url_price)

def generateInfo(api):
    response = requests.get(api)
    if response.status_code == 200:
        data = response.json()
        with open(file_name, 'w') as file:
            try:
                for response_val in data:
                    cr_symbol = response_val['symbol']
                    cr_desc = response_val['description']
                    file.write(f"{cr_symbol} {cr_desc}\n")
            except Exception as e:
                print(e)
        print("done")
    else:
        print(f"Error {response.status_code} - {response.text}")