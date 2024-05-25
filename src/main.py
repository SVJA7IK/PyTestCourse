from dataclasses import dataclass
from typing import Union


class ZeroReceivedError(Exception):
    pass

def calculate_pnl(spent: Union[int, float], received: Union[int, float]) -> int | float:
        if not isinstance(spent, (int, float)) or not isinstance(spent, (int, float)):
            raise TypeError("spent and received must be int or float")
        if received == 0:
            raise ZeroReceivedError("Received cannot be 0")
        return received - spent



@dataclass
class CalculatorInput:
    x: Union[int, float]
    y: Union[int, float]


class Calculator:
    def start_calculator(self) -> None:
        print("Starting Calculator...")

    def divide(self, calc_input: CalculatorInput) -> int | float:
        if not isinstance(calc_input.x, (int, float)) or not isinstance(calc_input.y, (int, float)):
            raise TypeError("x and y must be int or float")
        if calc_input.y == 0:
            raise ZeroDivisionError("y can't be 0")
        return calc_input.x / calc_input.y

    def add(self, calc_input: CalculatorInput) -> int | float:
        if not isinstance(calc_input.x, (int, float)) or not isinstance(calc_input.y, (int, float)):
            raise TypeError("x and y must be int or float")
        return calc_input.x + calc_input.y


if __name__ == "__main__":
    calculator = Calculator()
