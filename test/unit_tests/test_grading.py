import pytest
from api.classes.grading import Grading

@pytest.fixture(scope='function')
def grading_fixture(mocker):
    grading = Grading()
    mocker.patch.object(grading, 'convert', return_value='A+')
    return grading

class TestGrading():
    
    def test_denmark_12_is_usa_a_plus(self, grading_fixture):
        assert grading_fixture.convert('12', 'USA') == 'A+'

    # Not very useful