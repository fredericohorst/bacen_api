import requests
import pandas

def bacen_api_request(series_code, initial_date, end_date):
    """ 
    Builds a request to BACEN API and returns a time series dataframe.
    BACEN Open Data website: https://dadosabertos.bcb.gov.br
    """
    data_format = 'json'
    bacen_api_path = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.' + str(series_code) + '/dados?formato=' + data_format + '&dataInicial=' + initial_date + '&dataFinal=' + end_date
    bacen_api = requests.get(bacen_api_path)
    time_series_df = bacen_api.json()
    return time_series_df

def which_index(index_name):
    """
    Returns index code from an index name
    """
    kpis = pandas.read_csv('timeseries_dict.txt')
    index_name = 'IPCA'
    index = kpis[kpis.name == index_name]
    return index.cod.values[0]

def standard_formats(index_name):
    import datetime
    from dateutil.relativedelta import relativedelta
    today = datetime.date.today()
    end_date = today.strftime('%d/%m/%Y')
    first_date = today + relativedelta(months=-24)
    initial_date = first_date.strftime('%d/%m/%Y')
    index_code = which_index(index_name=index_name)
    return index_code, initial_date, end_date

def standard_cleaning(data, series_code, series_name):
    dataframe = pandas.DataFrame(data)
    dataframe['index'] = series_code
    dataframe['index_name'] = series_name
    dataframe['date'] = pandas.to_datetime(dataframe.data,dayfirst=True,format='%d/%m/%Y')
    dataframe['year'] = dataframe.date.dt.year
    dataframe['month'] = dataframe.date.dt.month
    dataframe['value'] = dataframe.valor.astype('float64')
    del dataframe['valor']
    del dataframe['data']
    return dataframe
