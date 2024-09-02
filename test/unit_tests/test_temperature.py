import pytest
import sys
from api.classes.temperature import Temperature

class TestTemperature():

    # Positive tests

    @pytest.mark.parametrize('temperature_value, origin_system, destination_system, expected', [
        (0, Temperature.CELSIUS, Temperature.FAHRENHEIT, 32),
        (10, Temperature.CELSIUS, Temperature.FAHRENHEIT, 50),
        (100, Temperature.CELSIUS, Temperature.FAHRENHEIT, 212),          # Boiling point of water
        (-10, Temperature.CELSIUS, Temperature.FAHRENHEIT, 14),
        (-17.78, Temperature.CELSIUS, Temperature.FAHRENHEIT, 0),
        (-273.15, Temperature.CELSIUS, Temperature.FAHRENHEIT, -459.67),  # Absolute zero
        (-195.8, Temperature.CELSIUS, Temperature.FAHRENHEIT, -320.44),   # Boiling point of liquid nitrogen
        (-78, Temperature.CELSIUS, Temperature.FAHRENHEIT, -108.4),       # Sublimation point of dry ice
        (-40, Temperature.CELSIUS, Temperature.FAHRENHEIT, -40),          # Celsius and Fahrenheit intersection
        (20, Temperature.CELSIUS, Temperature.FAHRENHEIT, 68),            # Room temperature
        (37, Temperature.CELSIUS, Temperature.FAHRENHEIT, 98.6),          # Average human body temperature
        (1000, Temperature.CELSIUS, Temperature.FAHRENHEIT, 1832),
        (-1000, Temperature.CELSIUS, Temperature.FAHRENHEIT, -1768),
        (10000, Temperature.CELSIUS, Temperature.FAHRENHEIT, 18032),
        (-10000, Temperature.CELSIUS, Temperature.FAHRENHEIT, -17968),
        (100000, Temperature.CELSIUS, Temperature.FAHRENHEIT, 180032),
        (-100000, Temperature.CELSIUS, Temperature.FAHRENHEIT, -179968)
    ])
    def test_convert_celsius_to_fahrenheit_passes(self, temperature_value, origin_system, destination_system, expected):
        temperature = Temperature(temperature_value, origin_system)
        assert temperature.convert(destination_system) == expected

    @pytest.mark.parametrize('temperature_value, origin_system, destination_system, expected', [
        (0, Temperature.FAHRENHEIT, Temperature.CELSIUS, -17.78),
        (32, Temperature.FAHRENHEIT, Temperature.CELSIUS, 0),             # Melting point of water              
        (50, Temperature.FAHRENHEIT, Temperature.CELSIUS, 10),
        (212, Temperature.FAHRENHEIT, Temperature.CELSIUS, 100),          # Boiling point of water
        (14, Temperature.FAHRENHEIT, Temperature.CELSIUS, -10),
        (-459.67, Temperature.FAHRENHEIT, Temperature.CELSIUS, -273.15),  # Absolute zero
        (-320.44, Temperature.FAHRENHEIT, Temperature.CELSIUS, -195.8),   # Boiling point of liquid nitrogen
        (-108.4, Temperature.FAHRENHEIT, Temperature.CELSIUS, -78),       # Sublimation point of dry ice
        (-40, Temperature.FAHRENHEIT, Temperature.CELSIUS, -40),          # Fahrenheit and Celsius intersection
        (68, Temperature.FAHRENHEIT, Temperature.CELSIUS, 20),            # Room temperature
        (98.6, Temperature.FAHRENHEIT, Temperature.CELSIUS, 37),          # Average human body temperature
        (1832, Temperature.FAHRENHEIT, Temperature.CELSIUS, 1000),
        (-1768, Temperature.FAHRENHEIT, Temperature.CELSIUS, -1000),
        (18032, Temperature.FAHRENHEIT, Temperature.CELSIUS, 10000),
        (-17968, Temperature.FAHRENHEIT, Temperature.CELSIUS, -10000),
        (180032, Temperature.FAHRENHEIT, Temperature.CELSIUS, 100000),
        (-179968, Temperature.FAHRENHEIT, Temperature.CELSIUS, -100000)
    ])
    def test_convert_fahrenheit_to_celsius_passes(self, temperature_value, origin_system, destination_system, expected):
        temperature = Temperature(temperature_value, origin_system)
        assert temperature.convert(destination_system) == expected

    # Repeat for the other 4 types of conversion
    # ...

    def test_exception_invalid_origin_system(self):
        with pytest.raises(ValueError):
            temperature = Temperature(0, 'L')
    
    def test_exception_invalid_destination_system(self):
        temperature = Temperature(0, 'K')
        with pytest.raises(ValueError):
            temperature.convert('L')

