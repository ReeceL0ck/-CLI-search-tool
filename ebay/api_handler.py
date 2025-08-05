import requests
import os
from dotenv import load_dotenv

class API_Handler():
    def __init__(self):
        self.VERB = 'GET'
        self.URL = os.getenv('SANDBOX_URL')  
        self.LIMIT = os.getenv('LIMIT', 10)
        self.ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
        if not self.ACCESS_TOKEN:
            raise ValueError("ACCESS_TOKEN is not set. Please set it in the environment variables.")
        self.headers= self._headers()
    def _headers(self):
        self.headers = {
            "Authorization": f"Bearer {self.ACCESS_TOKEN}",
            # "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        }
    
        return self.headers
    def _request(self, params):
        if params is None:
            raise ValueError("Parameters cannot be None. Please provide valid parameters.")
        
        self.URL = f"{self.URL}?q={params}"

        print(f"Making request to URL: {self.URL}")
        if not self.URL:
            raise ValueError("URL is not set. Please set the URL before making a request.")
        res = requests.get(url=f"{self.URL}?q={params}",
                           headers=self.headers)
        if res.status_code != 200:
            raise requests.HTTPError(f"Request failed with status code {res.status_code}: {res.text}")
        print(f"Request successful: {res.status_code}")
        print(f"Response: {res.text}")
        

        return res
    
    def _test(self,tst):
        print("Testing API Handler")
        print(tst)


load_dotenv(override=True)
ebay_api_handler = API_Handler()
response = ebay_api_handler._request("laptop")
