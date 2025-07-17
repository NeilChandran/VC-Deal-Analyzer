import requests

class CrunchbaseAPI:
    def __init__(self, api_key):
        self.base_url = 'https://api.crunchbase.com/v3.1'
        self.api_key = api_key

    def get_company_info(self, company_name):
        params = {'user_key': self.api_key, 'name': company_name}
        url = f'{self.base_url}/organizations'
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print("Error:", response.text)
            return None


