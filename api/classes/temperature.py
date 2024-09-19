from dataclasses import dataclass

@dataclass(frozen=True)
class TemperatureConstants:
    CELSIUS = 'C'
    FAHRENHEIT = 'F'
    KELVIN = 'K'

class Temperature(TemperatureConstants):
    def __init__(self, measure: float, system: str):
        if not self.__is_valid_system(system):
            raise ValueError('Unsupported measure system')
        self.measure = float(measure)
        self.system = system

    def __is_valid_system(self, system: str) -> bool:
        return system in (self.CELSIUS, self.FAHRENHEIT, self.KELVIN)

    def convert(self, destination_system) -> float:
        if not self.__is_valid_system(destination_system):
            raise ValueError('Unsupported destination measure system')
        conversion = self.system + destination_system

        if conversion[0] == conversion[1]:
            ret = self.measure
        elif conversion == self.CELSIUS + self.FAHRENHEIT:
            ret = round((self.measure * 1.8) + 32, 2)
        elif conversion == self.CELSIUS + self.KELVIN:
            ret = round(self.measure + 273.15, 2)
        elif conversion == self.FAHRENHEIT + self.CELSIUS:
            ret = round((self.measure - 32) / 1.8, 2)
        elif conversion == self.FAHRENHEIT + self.KELVIN:
            ret = round((self.measure + 459.67) * (5 / 9), 2)
        elif conversion == self.KELVIN + self.CELSIUS:
            ret = round(self.measure - 273.15, 2)
        elif conversion == self.KELVIN + self.FAHRENHEIT:
            ret = round((self.measure * (5 / 9)) - 459.67, 2)
        else:
            ret = None
        
        # This way 30.0 returns as 30
        if ret == int(ret):
            ret = int(ret)
        return ret