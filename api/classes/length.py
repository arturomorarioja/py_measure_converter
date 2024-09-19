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
        self.measure = abs(float(measure))
        self.system = system

    def convert(self) -> float:
        if self.system == self.METRIC:
            ret = round(self.measure / self.CONVERSION_FACTOR, 2)
        else:
            ret = round(self.measure * self.CONVERSION_FACTOR, 2)
        # This way 1500.0 returns as 1500
        if ret == int(ret):
            ret = int(ret)
        return ret