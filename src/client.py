import requests


class TinypulseAPIClient(object):
    
    BASE_URL = 'https://api.tinypulse.com/pulse'

    def __init__(self, API_KEY, ACCESS_TOKEN=None):
        self._api_key = API_KEY
        self._access_token = ACCESS_TOKEN

    def get(self, resource):
        # add tokens here
        # build url here
        url = ''
        try:
            r = requests.get(url)
            response = r.json()
            
            # return whatever
            
        
        except requests.exceptions.HTTPError:
            return {}
        
        