from tinypulse.constants import CHEERS
from tinypulse.utils import add_resource_parameter, filter_date_between, page, process_cheer_data
from tinypulse.client import TinypulseAPIClient


def get_cheers_between_date(api_key, start_date='19700101', end_date='19700101', page_size=10000, access_token=None):
    '''
    Gets n amount of cheers within date range
    Defined by page_size parameter.
    Default is 10000 to avoid pagination
    '''
    client = TinypulseAPIClient(api_key, access_token)
    resource = CHEERS 

    date_filter = filter_date_between('created_at', '{},{}'.format(start_date, end_date))
    resource = add_resource_parameter(resource, date_filter)

    size = page('size', page_size)
    resource = add_resource_parameter(resource, size)

    cheer_data = client.get(resource).get('data', [])
    
    return process_cheer_data(cheer_data)
