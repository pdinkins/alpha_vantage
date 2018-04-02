from alpha_vantage import alphavantage, cryptocurrencies, foreignexchange, sectorperformance, techindicators, timeseries
from pprint import pprint
from matplotlib import pyplot as plt

apikey = ''

spd0_keys= ["Rank A: Real-Time Performance", 
            "Rank B: 1 Day Performance",
            "Rank C: 5 Day Performance",
            "Rank D: 1 Month Performance",
            "Rank E: 3 Month Performance",
            "Rank F: Year-to-Date (YTD) Performance",
            "Rank G: 1 Year Performance",
            "Rank H: 3 Year Performance",
            "Rank I: 5 Year Performance",
            "Rank J: 10 Year Performance"]

s_keys =   ['Consumer Discretionary',
            'Consumer Staples',
            'Energy',
            'Financials',
            'Health Care',
            'Industrials',
            'Information Technology',
            'Materials',
            'Real Estate',
            'Telecommunication Services',
            'Utilities']

ts_int = ['1min', '5min', '15min', '30min', '60min']

#STOCK MARKET MENU FUNCTIONS
def rt_sector_performance_graph():
    from matplotlib import pyplot as plt
    sp = sectorperformance.SectorPerformances(key= apikey, output_format='pandas', indexing_type='date')
    data, meta_data = sp.get_sector()
    data['Rank A: Real-Time Performance'].plot(kind='bar')
    plt.title('Real Time Performance (%) per sector')
    plt.tight_layout()
    plt.grid()
    plt.show()

def sp_one_sector():
    try:
        print('Sectors')
        for i in range(0, len(s_keys)):
            print(i, '=', s_keys[i])
        key_value = int(input('\nEnter Index Value: '))
    except (IndexError, ValueError):
        print('***invalid*choice***')
    sp = sectorperformance.SectorPerformances(key=apikey, output_format='json', indexing_type='date')
    spdata = sp.get_sector()
    spdata0 = spdata[0]
    sector = s_keys[key_value]
    print('\n', sector, '\n')
    sd = []
    for z in range(0, len(spd0_keys)):
        secdic = spdata0[spd0_keys[z]]
        secper = secdic[s_keys[key_value]]
        sp100 = secper * 100
        sd.append(sp100)
        print(spd0_keys[z])
        print(sp100, '%\n')
    print(sd)
    
    

def print_sd():
    sp = sectorperformance.SectorPerformances(key=apikey, output_format='json', indexing_type='date')
    spdata = sp.get_sector()
    pprint(spdata)

def sector_performance_raw_data():
    try:
        print('Time Frames')
        for i in range(0, len(spd0_keys)):
            print(i, '=', spd0_keys[i])
        key_value = int(input('\nEnter Index Value: '))
    except (IndexError, ValueError):
        print('***invalid choice***')
    sp = sectorperformance.SectorPerformances(key=apikey, output_format='json', indexing_type='date')
    spdata = sp.get_sector()
    spdata0 = spdata[0]
    spdata1 = spdata[1]
    print('\n\n' + spd0_keys[key_value])
    print('Refreshed: ' + spdata1['Last Refreshed'] + '\n')
    try:
        sd_dict = spdata0[spd0_keys[key_value]]
        sd_values = []
        for i in range(0, len(s_keys)):
            sd_values.append(sd_dict[s_keys[i]])
        for i in range(0, len(s_keys)):
            print(s_keys[i])
            sper = sd_values[i] * 100
            print(sper, '%\n')
    except KeyError:
        pprint(spdata0[spd0_keys[key_value]])

def ts_stock_data(s_symbol, func_key, s_interval):
    if func_key == 'i':
        ts = timeseries.TimeSeries(key= apikey)
        tsdata, meta_data = ts.get_intraday(symbol=s_symbol, interval= s_interval)
        pprint(tsdata)
        pprint(meta_data)
    elif func_key == 'd':
        ts = timeseries.TimeSeries(key= apikey)
        tsdata, meta_data = ts.get_daily(symbol=s_symbol)
        pprint(tsdata)
        pprint(meta_data)
    elif func_key == 'da':
        ts = timeseries.TimeSeries(key= apikey)
        tsdata, meta_data = ts.get_daily_adjusted(symbol=s_symbol)
        pprint(tsdata)
        pprint(meta_data)
    elif func_key == 'w':
        ts = timeseries.TimeSeries(key= apikey)
        tsdata, meta_data = ts.get_weekly(symbol=s_symbol)
        pprint(tsdata)
        pprint(meta_data)
    elif func_key == 'wa':
        ts = timeseries.TimeSeries(key= apikey)
        tsdata, meta_data = ts.get_weekly_adjusted(symbol=s_symbol)
        pprint(tsdata)
        pprint(meta_data)

ts_func_keys = ['i - intraday', 'd - daily', 'da - daily adjusted',
                'w - weekly', 'wa - weekly adjusted', 'm - monthly ']

def ts_stock_data_intput():
    ss = input('Enter stock symbol: ')
    print('\nFunction Keys')
    for i in range(0, len(ts_func_keys)):
        print(ts_func_keys[i])
    fk = input('Function key: ')
    if fk != 'i':
        ts_stock_data(ss, fk)
    elif fk == 'i':
        print('\nIntervals')
        for i in range(0, len(ts_int)):
            print(ts_int[i])
        tsi = input('Enter interval: ')
        ts_stock_data(ss, fk, tsi)

cc_list = ['BTC', 'LTC', 'ETH', 'XRP']

def cc_info():
    cc = cryptocurrencies.CryptoCurrencies(key=apikey, output_format='json')
    for i in range(0, len(cc_list)):
        print(i, '-', cc_list[i])
    cci = int(input('CC index number: '))
    all_data = cc.get_digital_currency_intraday(symbol=cc_list[cci], market='USD')
    data = all_data[0]
    data_keys = []
    for j in range(0, 287):
        data_keys = list(data.keys())
    data_keys.reverse()
    for z in range(0, len(data_keys)):
        print('\n', data_keys[z])
        pprint(data[data_keys[z]])
    
