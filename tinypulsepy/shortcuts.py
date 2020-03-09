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

    cheer_data = client.get(resource).get('data', [])
    
    return utils.process_cheer_data(cheer_data)
