from .alphavantage import AlphaVantage as av


class CryptoCurrencies(av):

    @av._output_format
    @av._call_api_on_func
    def get_digital_currency_intraday(self, symbol, market):

        _FUNCTION_KEY = 'DIGITAL_CURRENCY_INTRADAY'
        return _FUNCTION_KEY, 'Time Series (Digital Currency Intraday)', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_digital_currency_daily(self, symbol, market):

        _FUNCTION_KEY = 'DIGITAL_CURRENCY_DAILY'
        return _FUNCTION_KEY, 'Time Series (Digital Currency Daily)', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_digital_currency_weekly(self, symbol, market):

        _FUNCTION_KEY = 'DIGITAL_CURRENCY_WEEKLY'
        return _FUNCTION_KEY, 'Time Series (Digital Currency Weekly)', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_digital_currency_monthly(self, symbol, market):

        _FUNCTION_KEY = 'DIGITAL_CURRENCY_MONTHLY'
        return _FUNCTION_KEY, 'Time Series (Digital Currency Monthly)', 'Meta Data'
