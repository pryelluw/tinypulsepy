# python -m unittest -v tests
import json
import unittest
try:
    import mock
except:
    import unittest.mock as mock

import requests
from client import TinypulseAPIClient
import constants
from shortcuts import get_cheers


def get_fixture(fixture):
    if fixture == 'cheers':
        with open('./fixtures/cheers.json', 'r') as f:
            return json.loads(f.read())
    return {}

def mock_get(*args, **kwargs):

    class MockResponse:
        def __init__(self, status_code, json_data):
            self.status_code = status_code
            self.json_data = json_data

        def json(self):
            return self.json_data

        def raise_for_status(self):
            pass

    return MockResponse(200, {})


class TestShortcuts(unittest.TestCase):
    def setUp(self):
        self.api_key = '12345'

    @mock.patch('requests.get', side_effect=mock_get)
    def test_get_cheers_response_ok(self, mocko):

        self.assertEqual(get_cheers(self.api_key), {})


class TestAPIEndpoints(unittest.TestCase):
    
    def setUp(self):
        self.api_key = '12345'
        self.client = TinypulseAPIClient(self.api_key, access_token=None)

    @mock.patch('requests.get', side_effect=mock_get)
    def test_get_cheers_calls_api_all_cheers_endpoint(self, mocko):
        self.client.get(constants.CHEERS)
        mocko.assert_called_with(
            '{}{}'.format(self.client.BASE_URL,constants.CHEERS),
            headers={'AccessToken': self.client._api_key}
        )
    
        
if __name__ == '__main__':
    unittest.main()
