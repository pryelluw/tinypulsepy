import constants
import utils
from client import TinypulseAPIClient


def get_cheers_between_date(api_key, start_date='19700101', end_date='19700101', page_size=10000, access_token=None):
    '''
    Gets n amount of cheers within date range
    Defined by page_size parameter.
    Default is 10000 to avoid pagination
    '''
    client = TinypulseAPIClient(api_key, access_token)
    resource = constants.CHEERS 

    date_filter = utils.filter_date_between('created_at', '{},{}'.format(start_date, end_date))
    resource = utils.add_resource_parameter(resource, date_filter)

    size = utils.page('size', page_size)
    resource = utils.add_resource_parameter(resource, size)

    data = client.get(resource).get('data', [])

    def cheer_data(attributes):
        cheers = []
        for attr in attributes:
            cheer = {}
            cheer['sender'] = attr.get('sender_name', 'unknown')
            cheer['receiver'] = attr.get('receiver_name', 'unknown')
            cheer['praise'] = attr.get('praise', '')
            cheers.append(cheer)
        return cheers

    attributes = [attr.get("attributes") for attr in data]
    return cheer_data(attributes)
