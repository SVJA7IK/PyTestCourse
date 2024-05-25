from main import Calculator
import pytest

from tests.unit.conftest import TCalculatorInput


class TestCalculator:
    """ Группировка тестов """

    @pytest.mark.usefixtures("divide_inputs")
    def test_divide(self, divide_inputs: list[TCalculatorInput]):
        for i in divide_inputs:
            with i.expectation:
                assert Calculator().divide(i) == i.res

    # Не обязательно писать usefixtures при работе с фикстурами (главное, чтобы был параметр с названием нужной фикстуры)
    def test_add(self, add_inputs: list[TCalculatorInput]):
        for i in add_inputs:
            with i.expectation:
                assert Calculator().add(i) == i.res


def test_solo_add(add_inputs: list[TCalculatorInput]):
        for i in add_inputs:
            with i.expectation:
                assert Calculator().add(i) == i.res