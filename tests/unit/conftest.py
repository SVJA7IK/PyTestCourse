import pytest
from dataclasses import dataclass
from typing import Any
from main import CalculatorInput
from contextlib import nullcontext as does_not_raise


@dataclass
class TCalculatorInput(CalculatorInput):
    """Модель с тестовыми данными для фикстур"""

    res: Any
    expectation: Any = does_not_raise()


@pytest.fixture
def divide_inputs():
    """Наборы данных для тестирования деления"""
    return [
        TCalculatorInput(1, 2, 0.5),
        TCalculatorInput(1, -1, -1),
        TCalculatorInput(1, 0, 0, pytest.raises(ZeroDivisionError)),
        TCalculatorInput("1", 2, 0.5, pytest.raises(TypeError)),  # type: ignore TypeError
    ]


@pytest.fixture
def add_inputs():
    """Наборы данных для тестирования сложения"""
    return [
        TCalculatorInput(1, 2, 3),
        TCalculatorInput(1, -1, 0),
        TCalculatorInput("1", 2, 3, pytest.raises(TypeError)),  # type: ignore TypeError
    ]
