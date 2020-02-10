# python -m unittest -v tests.TestShortcuts
import unittest
import mock
from client import TinypulseAPIClient
from shortcuts import get_cheers


def mock_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, status_code, json_data):
            self.status_code = status_code
            self.json_data = json_data

        def json(self):
            return self.json_data

        def raise_for_status(self):
            pass

    return MockResponse(200, {'data': []})



class TestShortcuts(unittest.TestCase):
    
    
    @mock.patch('requests.get', side_effect=mock_get)
    def test_get_cheers_response_ok(self, mocko):
        self.assertEqual(get_cheers('12345'), {'data': []})
        
        
if __name__ == '__main__':
    unittest.main()