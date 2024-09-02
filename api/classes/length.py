from dataclasses import dataclass

@dataclass(frozen=True)
class LengthConstants:
    IMPERIAL = 'I'
    METRIC = 'M'
    CONVERSION_FACTOR = 2.54

class Length(LengthConstants):
    def __init__(self, measure: float, system: str):
        if not system in (self.IMPERIAL, self.METRIC):
            raise ValueError('Unsupported measure system')
        self.measure = float(measure)
        self.system = system

    def convert(self):
        if self.system == self.METRIC:
            return round(self.measure / self.CONVERSION_FACTOR, 2)
        else:
            return round(self.measure * self.CONVERSION_FACTOR, 2)