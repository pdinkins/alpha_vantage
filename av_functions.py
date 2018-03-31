from av.alpha_vantage import alphavantage, cryptocurrencies, foreignexchange
from av.alpha_vantage import sectorperformance, techindicators, timeseries
from pprint import pprint
from matplotlib import pyplot as plt

apikey = 'DQBYYE0H09YWLS7W'

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
    pprint(spdata0[spd0_keys[key_value]])
    
