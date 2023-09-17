import pandas as pd
import nasdaqdatalink as nas

nas.ApiConfig.api_key = "F4G-YDf5W-XYEcfPRSic"

COLUMNS = ['ticker', 'date', 'adj_close']

df = nas.get_table(
    datatable_code = '',
    ticker = ['AAPL', 'MSFT', 'INTC'],
    qopts = { 'columns': COLUMNS },
    date = {
        'gte': '2011-01-01',
        'lte': '2021-12-31'
    },
    paginate = True,
)

#
print(f'Downloaded {len(df)} rows of data.')
print(df.head())
