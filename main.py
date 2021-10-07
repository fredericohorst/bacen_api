import utils
import os

# os.getenv(time_series_name)

def init():
    series_name = 'IPCA'
    index_code, initial_date, end_date = utils.standard_formats(index_name=series_name)
    ts = utils.bacen_api_request(series_code=index_code, initial_date=initial_date, end_date=end_date)
    ts = utils.standard_cleaning(data=ts,series_code=index_code,series_name=series_name)
    return ts




ts = init()
print(ts)




