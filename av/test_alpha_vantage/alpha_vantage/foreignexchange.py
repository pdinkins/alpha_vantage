from .alphavantage import AlphaVantage as av


class ForeignExchange(av):

    def __init__(self, *args, **kwargs):

        super(ForeignExchange, self).__init__(*args, **kwargs)
        self._append_type = False
        if self.output_format.lower() == 'csv' or self.output_format.lower() == 'pandas':
            raise ValueError("Output format {} is not compatible with the ForeignExchange class".format(
                self.output_format.lower()))

    @av._output_format
    @av._call_api_on_func
    def get_currency_exchange_rate(self, from_currency, to_currency):

        _FUNCTION_KEY = 'CURRENCY_EXCHANGE_RATE'
        return _FUNCTION_KEY, 'Realtime Currency Exchange Rate', None
