from .alphavantage import AlphaVantage as av


class TechIndicators(av):

    def __init__(self, *args, **kwargs):

        super(TechIndicators, self).__init__(*args, **kwargs)
        self._append_type = False
        if self.output_format.lower() == 'csv':
            raise ValueError("Output format {} is not comatible with the TechIndicators class".format(
                self.output_format.lower()))

    @av._output_format
    @av._call_api_on_func
    def get_sma(self, symbol, interval='daily', time_period=20, series_type='close'):

        _FUNCTION_KEY = "SMA"
        return _FUNCTION_KEY, 'Technical Analysis: SMA', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_ema(self, symbol, interval='daily', time_period=20, series_type='close'):

        _FUNCTION_KEY = "EMA"
        return _FUNCTION_KEY, 'Technical Analysis: EMA', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_wma(self, symbol, interval='daily', time_period=20, series_type='close'):

        _FUNCTION_KEY = "WMA"
        return _FUNCTION_KEY, 'Technical Analysis: WMA', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_dema(self, symbol, interval='daily', time_period=20, series_type='close'):

        _FUNCTION_KEY = "DEMA"
        return _FUNCTION_KEY, 'Technical Analysis: DEMA', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_tema(self, symbol, interval='daily', time_period=20, series_type='close'):

        _FUNCTION_KEY = "TEMA"
        return _FUNCTION_KEY, 'Technical Analysis: TEMA', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_trima(self, symbol, interval='daily', time_period=20, series_type='close'):

        _FUNCTION_KEY = "TRIMA"
        return _FUNCTION_KEY, 'Technical Analysis: TRIMA', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_kama(self, symbol, interval='daily', time_period=20, series_type='close'):

        _FUNCTION_KEY = "KAMA"
        return _FUNCTION_KEY, 'Technical Analysis: KAMA', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_mama(self, symbol, interval='daily', time_period=20, series_type='close',
                 fastlimit=None, slowlimit=None):

        _FUNCTION_KEY = "MAMA"
        return _FUNCTION_KEY, 'Technical Analysis: MAMA', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_t3(self, symbol, interval='daily', time_period=20, series_type='close'):

        _FUNCTION_KEY = "T3"
        return _FUNCTION_KEY, 'Technical Analysis: T3', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_macd(self, symbol, interval='daily', series_type='close',
                 fastperiod=None, slowperiod=None, signalperiod=None):

        _FUNCTION_KEY = "MACD"
        return _FUNCTION_KEY, 'Technical Analysis: MACD', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_macdext(self, symbol, interval='daily', series_type='close',
                    fastperiod=None, slowperiod=None, signalperiod=None, fastmatype=None,
                    slowmatype=None, signalmatype=None):
  
        _FUNCTION_KEY = "MACDEXT"
        return _FUNCTION_KEY, 'Technical Analysis: MACDEXT', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_stoch(self, symbol, interval='daily', fastkperiod=None,
                  slowkperiod=None, slowdperiod=None, slowkmatype=None, slowdmatype=None):

        _FUNCTION_KEY = "STOCH"
        return _FUNCTION_KEY, 'Technical Analysis: STOCH', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_stochf(self, symbol, interval='daily', fastkperiod=None,
                   fastdperiod=None, fastdmatype=None):

        _FUNCTION_KEY = "STOCHF"
        return _FUNCTION_KEY, 'Technical Analysis: STOCHF', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_rsi(self, symbol, interval='daily', time_period=20, series_type='close'):

        _FUNCTION_KEY = "RSI"
        return _FUNCTION_KEY, 'Technical Analysis: RSI', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_stochrsi(self, symbol, interval='daily', time_period=20,
                     series_type='close', fastkperiod=None, fastdperiod=None, fastdmatype=None):

        _FUNCTION_KEY = "STOCHRSI"
        return _FUNCTION_KEY, 'Technical Analysis: STOCHRSI', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_willr(self, symbol, interval='daily', time_period=20):

        _FUNCTION_KEY = "WILLR"
        return _FUNCTION_KEY, 'Technical Analysis: WILLR', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_adx(self, symbol, interval='daily', time_period=20):

        _FUNCTION_KEY = "ADX"
        return _FUNCTION_KEY, 'Technical Analysis: ADX', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_adxr(self, symbol, interval='daily', time_period=20):

        _FUNCTION_KEY = "ADXR"
        return _FUNCTION_KEY, 'Technical Analysis: ADXR', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_apo(self, symbol, interval='daily', series_type='close',
                fastperiod=None, slowperiod=None, matype=None):

        _FUNCTION_KEY = "APO"
        return _FUNCTION_KEY, 'Technical Analysis: APO', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_ppo(self, symbol, interval='daily', series_type='close',
                fastperiod=None, slowperiod=None, matype=None):

        _FUNCTION_KEY = "PPO"
        return _FUNCTION_KEY, 'Technical Analysis: PPO', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_mom(self, symbol, interval='daily', time_period=20, series_type='close'):

        _FUNCTION_KEY = "MOM"
        return _FUNCTION_KEY, 'Technical Analysis: MOM', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_bop(self, symbol, interval='daily', time_period=20):

        _FUNCTION_KEY = "BOP"
        return _FUNCTION_KEY, 'Technical Analysis: BOP', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_cci(self, symbol, interval='daily', time_period=20):

        _FUNCTION_KEY = "CCI"
        return _FUNCTION_KEY, 'Technical Analysis: CCI', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_cmo(self, symbol, interval='daily', time_period=20, series_type='close'):

        _FUNCTION_KEY = "CMO"
        return _FUNCTION_KEY, 'Technical Analysis: CMO', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_roc(self, symbol, interval='daily', time_period=20, series_type='close'):

        _FUNCTION_KEY = "ROC"
        return _FUNCTION_KEY, 'Technical Analysis: ROC', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_rocr(self, symbol, interval='daily', time_period=20, series_type='close'):

        _FUNCTION_KEY = "ROCR"
        return _FUNCTION_KEY, 'Technical Analysis: ROCR', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_aroon(self, symbol, interval='daily', time_period=20, series_type='close'):

        _FUNCTION_KEY = "AROON"
        return _FUNCTION_KEY, 'Technical Analysis: AROON', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_aroonosc(self, symbol, interval='daily', time_period=20, series_type='close'):

        _FUNCTION_KEY = "AROONOSC"
        return _FUNCTION_KEY, 'Technical Analysis: AROONOSC', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_mfi(self, symbol, interval='daily', time_period=20, series_type='close'):

        _FUNCTION_KEY = "MFI"
        return _FUNCTION_KEY, 'Technical Analysis: MFI', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_trix(self, symbol, interval='daily', time_period=20, series_type='close'):

        _FUNCTION_KEY = "TRIX"
        return _FUNCTION_KEY, 'Technical Analysis: TRIX', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_ultsoc(self, symbol, interval='daily', timeperiod1=None,
                   timeperiod2=None, timeperiod3=None):

        _FUNCTION_KEY = "ULTOSC"
        return _FUNCTION_KEY, 'Technical Analysis: ULTOSC', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_dx(self, symbol, interval='daily', time_period=20, series_type='close'):

        _FUNCTION_KEY = "DX"
        return _FUNCTION_KEY, 'Technical Analysis: DX', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_minus_di(self, symbol, interval='daily', time_period=20):

        _FUNCTION_KEY = "MINUS_DI"
        return _FUNCTION_KEY, 'Technical Analysis: MINUS_DI', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_plus_di(self, symbol, interval='daily', time_period=20):

        _FUNCTION_KEY = "PLUS_DI"
        return _FUNCTION_KEY, 'Technical Analysis: PLUS_DI', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_minus_dm(self, symbol, interval='daily', time_period=20):

        _FUNCTION_KEY = "MINUS_DM"
        return _FUNCTION_KEY, 'Technical Analysis: MINUS_DM', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_plus_dm(self, symbol, interval='daily', time_period=20):

        _FUNCTION_KEY = "PLUS_DM"
        return _FUNCTION_KEY, 'Technical Analysis: PLUS_DM', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_bbands(self, symbol, interval='daily', time_period=20,  series_type='close',
                   nbdevup=None, nbdevdn=None, matype=None):

        _FUNCTION_KEY = "BBANDS"
        return _FUNCTION_KEY, 'Technical Analysis: BBANDS', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_midpoint(self, symbol, interval='daily', time_period=20, series_type='close'):

        _FUNCTION_KEY = "MIDPOINT"
        return _FUNCTION_KEY, 'Technical Analysis: MIDPOINT', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_midprice(self, symbol, interval='daily', time_period=20):

        _FUNCTION_KEY = "MIDPRICE"
        return _FUNCTION_KEY, 'Technical Analysis: MIDPRICE', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_sar(self, symbol, interval='daily', acceleration=None, maximum=None):

        _FUNCTION_KEY = "SAR"
        return _FUNCTION_KEY, 'Technical Analysis: SAR', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_trange(self, symbol, interval='daily'):

        _FUNCTION_KEY = "TRANGE"
        return _FUNCTION_KEY, 'Technical Analysis: TRANGE', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_atr(self, symbol, interval='daily', time_period=20):

        _FUNCTION_KEY = "ATR"
        return _FUNCTION_KEY, 'Technical Analysis: ATR', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_natr(self, symbol, interval='daily', time_period=20):

        _FUNCTION_KEY = "NATR"
        return _FUNCTION_KEY, 'Technical Analysis: NATR', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_ad(self, symbol, interval='daily'):

        _FUNCTION_KEY = "AD"
        return _FUNCTION_KEY, 'Technical Analysis: Chaikin A/D', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_adosc(self, symbol, interval='daily', fastperiod=None,
                  slowperiod=None):

        _FUNCTION_KEY = "ADOSC"
        return _FUNCTION_KEY, 'Technical Analysis: ADOSC', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_obv(self, symbol, interval='daily'):

        _FUNCTION_KEY = "OBV"
        return _FUNCTION_KEY, 'Technical Analysis: OBV', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_ht_trendline(self, symbol, interval='daily', series_type='close'):

        _FUNCTION_KEY = "HT_TRENDLINE"
        return _FUNCTION_KEY, 'Technical Analysis: HT_TRENDLINE', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_ht_sine(self, symbol, interval='daily', series_type='close'):

        _FUNCTION_KEY = "HT_SINE"
        return _FUNCTION_KEY, 'Technical Analysis: HT_SINE', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_ht_trendmode(self, symbol, interval='daily', series_type='close'):

        _FUNCTION_KEY = "HT_TRENDMODE"
        return _FUNCTION_KEY, 'Technical Analysis: HT_TRENDMODE', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_ht_dcperiod(self, symbol, interval='daily', series_type='close'):

        _FUNCTION_KEY = "HT_DCPERIOD"
        return _FUNCTION_KEY, 'Technical Analysis: HT_DCPERIOD', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_ht_dcphase(self, symbol, interval='daily', series_type='close'):

        _FUNCTION_KEY = "HT_DCPHASE"
        return _FUNCTION_KEY, 'Technical Analysis: HT_DCPHASE', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_ht_phasor(self, symbol, interval='daily', series_type='close'):

        _FUNCTION_KEY = "HT_PHASOR"
        return _FUNCTION_KEY, 'Technical Analysis: HT_PHASOR', 'Meta Data'
