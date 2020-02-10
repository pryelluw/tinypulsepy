import requests


class TinypulseAPIClient(object):
    
    BASE_URL = 'https://api.tinypulse.com/pulse'

    def __init__(self, api_key, access_token=None):
        self._api_key = api_key
        self._access_token = access_token

    def add_url_parameter(self, url, param):
        if '?' not in url:
            return '{0}?{1}'.format(url, param)
        return '{0}&{1}'.format(url, param)

    def build_resource(self, template, **kwargs):
        return template.format(kwargs)

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
