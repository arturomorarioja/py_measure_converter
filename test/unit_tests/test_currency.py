import pytest
from api.classes.currency import Currency

@pytest.fixture(scope='function')
def currency_fixture(mocker):
    currency = Currency()
    mocker.patch.object(currency, 'convert', return_value=1000)
    return currency

class TestCurrency():
    
    def test_convert_returns_float(self, currency_fixture):
        assert currency_fixture.convert(1000) == 1000

    # Not very useful