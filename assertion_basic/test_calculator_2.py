import pytest

from calculator import Calculator


class TestCalculator():

    @pytest.mark.login
    def test_calculator(self):
        assert 9==Calculator.add(4,5)
        assert 9==Calculator.sub(14,5)
        assert 12==Calculator.mul(3,4)


    def test_calculator_2(self):
        assert 11==Calculator.add(6,5)
        assert 4==Calculator.sub(14,10)
        assert 21==Calculator.mul(21,2)