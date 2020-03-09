import requests

#reference: https://api-docs.tinypulse.com/doc/develop_get_auth_tokens

# Access Token: When calling the TINYpulse API, 
#you must attach the access token as a Bearer token 
#to the Authorization header in an HTTP request.
#You can use to this to access multiple organizations.
# ACCESS_TOKEN = ''

# API Key: When calling the TINYpulse API, 
# you attach the API key to the AccessToken header 
# in an HTTP request. Use may use this to 
# access one single organization only.

class TinypulseAPIClient(object):
    
    BASE_URL = 'https://api.tinypulse.com/pulse'

    def __init__(self, api_key, access_token=None):
        self._api_key = api_key
        self._access_token = access_token

    def get(self, resource):
        headers = {'AccessToken': self._api_key}
        if self._access_token:
            headers['Authorization:': 'Bearer {}'.format(self._access_token)]
        
        url = '{}{}'.format(self.BASE_URL, resource)
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        
        if r.status_code == requests.codes.ok:
                return r.json()
        return {}
