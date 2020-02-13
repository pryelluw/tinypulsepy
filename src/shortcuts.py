import constants
from client import TinypulseAPIClient


def get_cheers(api_key, access_token=None):
    client = TinypulseAPIClient(api_key, access_token)
    return client.get(constants.CHEERS) # add pagination and filtering
    # only return the actual cheers and not the whole response
    # if multiple pages, then iterate here and only return data
    # define model for cheer