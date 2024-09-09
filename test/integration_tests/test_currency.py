import pytest
from api.classes.currency import Currency

@pytest.fixture(scope='function')
def currency_fixture():
    return Currency()

class TestCurrency():

    #
    # Positive tests
    #

    def test_get_currencies_is_array(self, currency_fixture):
        assert isinstance(currency_fixture.get_all(), dict)

    @pytest.mark.parametrize('amount', [
        (0),
        (1000),
        (1245.2),
        (1245.25)
    ])
    def test_convert_default_currencies_is_float(self, currency_fixture, amount):
        assert isinstance(currency_fixture.convert(amount), float)

    @pytest.mark.parametrize('amount, origin_currency', [
        (0, 'NOK'),
        (1000, 'USD'),
        (1245.2, 'EUR'),
        (1245.25, 'MXN')
    ])
    def test_convert_from_currency_is_float(self, currency_fixture, amount, origin_currency):
        assert isinstance(currency_fixture.convert(amount, origin_currency), float)

    @pytest.mark.parametrize('amount, origin_currency, destination_currency', [
        (0, 'NOK', 'MXN'),
        (1000, 'USD', 'EUR'),
        (1245.2, 'EUR', 'NOK'),
        (1245.25, 'MXN', 'USD')
    ])
    def test_convert_is_float(self, currency_fixture, amount, origin_currency, destination_currency):
        assert isinstance(currency_fixture.convert(amount, origin_currency, destination_currency), float)

    #
    # Negative tests
    #
    
    def test_non_existing_origin_currency_fails(self, currency_fixture):
        assert 'error' in currency_fixture.convert(1000, 'XXX', 'USD')
    
    def test_non_existing_destination_currency_fails(self, currency_fixture):
        assert 'error' in currency_fixture.convert(1000, 'NOK', 'XXX')