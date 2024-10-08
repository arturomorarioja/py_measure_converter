import pytest
from api import create_app
from api.classes.grading import Grading

@pytest.fixture(scope='function', autouse=True)
def get_app_context():
    app = create_app()
    with app.app_context():
        yield

@pytest.fixture(scope='function')
def grading_fixture():
    return Grading()

class TestGrading():

    # Positive tests
    @pytest.mark.parametrize('grade, system, expected', [
        ('12', Grading.DENMARK, 'A+'),
        ('10', Grading.DENMARK, 'A'),
        ('7', Grading.DENMARK, 'B'),
        ('4', Grading.DENMARK, 'C'),
        ('02', Grading.DENMARK, 'D'),
        ('00', Grading.DENMARK, 'F'),
        ('-3', Grading.DENMARK, 'F'),
        ('A+', Grading.USA, '12'),
        ('A', Grading.USA, '10'),
        ('B', Grading.USA, '7'),
        ('C', Grading.USA, '4'),
        ('D', Grading.USA, '02'),
        ('F', Grading.USA, '00')
    ])
    def test_convert_passes(self, grading_fixture, grade, system, expected):
        app = create_app()
        with app.app_context():
            assert grading_fixture.convert(grade, system) == expected
        
    # Negative tests
    @pytest.mark.parametrize('grade, system', [
        ('A', 'Spain'),
        ('10', 'Spain'),
        ('K', Grading.DENMARK),
        ('K', Grading.USA)
    ])
    def test_convert_raises_exception(self, grading_fixture, grade, system):
        with pytest.raises(ValueError):
            grading_fixture.convert(grade, system)