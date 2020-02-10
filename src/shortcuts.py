import constants
from client import TinypulseAPIClient


def get_cheers(api_key, access_token=None):
    client = TinypulseAPIClient(api_key, access_token)
    return client.get(constants.CHEERS)
