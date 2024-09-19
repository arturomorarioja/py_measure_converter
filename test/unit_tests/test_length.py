import pytest
import sys
from api.classes.length import Length

class TestLength():

    # Positive tests
    @pytest.mark.parametrize('length_value, system, expected', [
        (0, Length.IMPERIAL, 0),                                        # Lower valid boundary
        (1, Length.IMPERIAL, 2.54),
        (0.5, Length.IMPERIAL, 1.27),
        (0.25, Length.IMPERIAL, 0.64),
        (7.077532027016991E+307, Length.IMPERIAL, sys.float_info.max),  # Upper valid boundary
        (0, Length.METRIC, 0),                                          # Lower valid boundary
        (2.54, Length.METRIC, 1),                                          
        (1.27, Length.METRIC, 0.5),
        (0.635, Length.METRIC, 0.25),
        (-1, Length.IMPERIAL, 2.54),
        (-2.54, Length.METRIC, 1),
    ])
    def test_convert_passes(self, length_value, system, expected):
        length = Length(length_value, system)
        assert length.convert() == expected
        
    # Negative test
    def test_convert_fails(self):
        length = Length(-1, Length.IMPERIAL)
        assert not length.convert() == -2.54
    
    # Exception test
    def test_exception_invalid_system(self):
        with pytest.raises(Exception):
            length = Length(1, 'K')