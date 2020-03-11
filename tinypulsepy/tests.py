# python -m unittest -v tests
import json
import unittest
try:
    import mock
except:
    import unittest.mock as mock

import requests
from client import TinypulseAPIClient
from constants import CHEERS
from shortcuts import get_cheers_between_date
from utils import add_resource_parameter, filter_date_between, page, process_cheer_data


def get_fixture(fixture):
    if fixture == 'cheers':
        with open('./fixtures/cheers.json', 'r') as f:
            return json.loads(f.read())
    return {}


class MockResponse:
    def __init__(self, status_code=200, json_data={}):
        self.status_code = status_code
        self.json_data = json_data

    def json(self):
        return self.json_data

    def raise_for_status(self):
        pass


def mock_get(*args, **kwargs):
    return MockResponse()


def mock_cheers(*args, **kwargs):
    m = MockResponse(200, get_fixture('cheers'))
    return m


class TestAPIEndpoints(unittest.TestCase):
    
    def setUp(self):
        self.api_key = '12345'
        self.client = TinypulseAPIClient(self.api_key, access_token=None)

    @mock.patch('requests.get', side_effect=mock_get)
    def test_get_cheers_calls_api_all_cheers_endpoint(self, mocko):
        self.client.get(CHEERS)
        mocko.assert_called_with(
            '{}{}'.format(self.client.BASE_URL, CHEERS),
            headers={'AccessToken': self.client._api_key}
        )

class TestShorcuts(unittest.TestCase):
    def setUp(self):
        self.api_key = '12345'
    
    @mock.patch('requests.get', side_effect=mock_cheers)
    def test_get_cheers_between_date(self, mocko):
        cheers = get_cheers_between_date(self.api_key)
        self.assertTrue(len(cheers) == 1)


class TestProcessCheerData(unittest.TestCase):
    def setUp(self):
        self.fixture = get_fixture('cheers')

    def test_process_cheer_data(self):
        cheer_data = process_cheer_data(self.fixture.get('data'))
        self.assertTrue(self.fixture.get('data')[0].get('attributes').get('sender_name') == cheer_data[0]['sender'])
        self.assertTrue(self.fixture.get('data')[0].get('id') == cheer_data[0]['id'])


if __name__ == '__main__':
    unittest.main()
