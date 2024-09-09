import os
from dotenv import load_dotenv
import requests
from requests.exceptions import HTTPError

load_dotenv()

class Currency():
    def get_all(self):
        url = f'{os.getenv("BASE_API_URL")}/currencies?apikey={os.getenv("CURRENCY_API_KEY")}'
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except HTTPError as http_err:
            print('--- ERROR ---')
            print(http_err)
            return {'error': http_err.msg}
        except Exception as e:
            print('--- ERROR ---')
            print(e)
            return {'error': e.msg}

    def convert(self, amount: float, base_currency: str='DKK', destination_currency: str='EUR') -> float:
        url = f'{os.getenv("BASE_API_URL")}/latest?apikey={os.getenv("CURRENCY_API_KEY")}&base_currency={base_currency}'
        try:            
            response = requests.get(url)
            response.raise_for_status()        
            response = response.json()
            return round(float(amount) * response['data'][destination_currency]['value'], 2)
        except HTTPError as http_err:
            print('--- ERROR ---')
            print(http_err)
            return {'error': http_err}
        except Exception as e:
            print('--- ERROR ---')
            print(e)
            return {'error': e}