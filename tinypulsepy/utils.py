def add_resource_parameter(resource, parameter):
    '''
    Adds url parameter to a resource
    :param resource: str
    :param parameter: str - already url encoded with
                            any of the utilities below
    '''
    if '?' not in resource:
        return '{0}?{1}'.format(resource, parameter)
    return '{0}&{1}'.format(resource, parameter)


# pagination reference: https://api-docs.tinypulse.com/doc/develop_paging

def page(key, value):
    '''
    accepted keys:
        number: page number
        size: results per page
    value: int
    '''
    return 'page[{key}]={value}'.format(key=key, value=value)

#  Sorting: Allowed Sorting Field varies across different TINYpulse API resources. Please see the v1 documentation for more details.
#  More: https://api-docs.tinypulse.com/doc/develop_sorting
#        https://api-docs.tinypulse.com/doc/api

def sort(key, value):
    return 'sort[{key}]={value}'.format(key=key, value=value)


# fieldsets reference: https://api-docs.tinypulse.com/doc/develop_fieldsets

def fields(key, value):
    '''
    value may be a single string 
    or comma separated strings (not a list or array)
    
    Example:
        Single: value1
        Multiple: value1,value2
    '''
    return 'fields[{key}]={value}'.format(key=key, value=value)


# filter reference: https://api-docs.tinypulse.com/doc/develop_filter

def filter_equal(key, value):
    return 'filter[{key}]={value}'.format(key=key, value=value)


def filter_equal_alt(key, value):
    '''
    alternative to filter
    functionality is same as filter_equal()
    '''
    return 'filter[{key}][eq]={value}'.format(key=key, value=value)


def filter_not_equal(key, value):
    return 'filter[{key}][ne]={value}'.format(key=key, value=value)


def filter_greater(key, value):
    return 'filer[{key}][gt]={value}'.format(key=key, value=value)


def filter_greater_or_equal(key, value):
    return 'filter[{key}][ge]={value}'.format(key=key, value=value)


def filter_less_than(key, value):
    return 'filter[{key}][lt]={value}'.format(key=key, value=value)


def filter_less_than_or_equal(key, value):
    return 'filter[{key}][le]={value}'.format(key=key, value=value)


# filter dates, datetimes

def filter_date_equal(key, date_str):
    '''
    date_str: YYYY-MM-DD format
    supported range: '1000-01-01' to '9999-12-31'
    '''
    return 'filter[{key}]={value}'.format(key=key, value=dates_str)


def filter_date_between(key, dates_str):
    '''
    dates_str: YYYY-MM-DD format
    Comma separated dates (not a list or array)
    Example -> '20180101,20180201'
    '''
    return 'filter[{key}]={value}'.format(key=key, value=dates_str)


def filter_date_between_alt(key, dates_str):
    '''
    alternative to filter_date_between()
    functionality is the same
    
    dates_str: YYYY-MM-DD format
    Comma separated dates (not a list or array)
    Example -> '20180101,20180201'
    '''
    return 'filter[{key}][between]={value}'.format(key=key, value=dates_str)


def filter_datetime_equal(key, datetime_str):
    '''
    datetime_str: YYYY-MM-DD HH:MM:SS format
    supported range: '1000-01-01 00:00:00' to '9999-12-31 23:59:59'
    '''
    return 'filter[{key}]={value}'.format(key=key, value=datetimes_str)


def filter_datetime_between(key, datetimes_str):
    '''
    datetimes_str: YYYY-MM-DD HH:MM:SS format
    Comma separated dates (not a list or array)
    Example -> '20180101 00:00:00,20180201 00:00:00'
    '''
    return 'filter[{key}]={value}'.format(key=key, value=datetimes_str)


def filter_datetime_between_alt(key, datetimes_str):
    '''
    alternative to filter_datetime_between()
    functionality is the same
    
    datetimes_str: YYYY-MM-DD HH:MM:SS format
    Comma separated dates (not a list or array)
    Example -> '20180101 00:00:00,20180201 00:00:00'
    '''
    return 'filter[{key}][between]={value}'.format(key=key, value=datetimes_str)


def process_cheer_data(cheer_data=[]):
    cheers = []
    for cheer in cheer_data:
        current_cheer = {}
        current_cheer['sender'] = cheer.get('attributes').get('sender_name', 'unknown')
        current_cheer['receiver'] = cheer.get('attributes').get('receiver_name', 'unknown')
        current_cheer['praise'] = cheer.get('attributes').get('praise', '')
        current_cheer['created_at'] = cheer.get('attributes').get('created_at')
        current_cheer['id'] = cheer.get('id')
        cheers.append(current_cheer)
    return cheers
