import pytest

from calculator import Calculator



class TestCalculator():
    # The Stateless Approach
    @pytest.mark.calculator
    def test_calculator(self):
        assert 9==Calculator.add(4,5)
        assert 9==Calculator.sub(14,5)
        assert 12==Calculator.mul(3,4)

    # The State Approach here the object holds the previous data
    def test_sum(self):
        total=Calculator(10)
        assert 14==total.sum(4)