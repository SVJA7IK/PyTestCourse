import pytest

from main import Calculator


def pytest_addoption(parser):
    parser.addoption(
        "--speed",
        default="slow",
        choices=("slow", "quickly")
    )

@pytest.fixture(scope="session")
def speed(request):
    return request.config.getoption("--speed")


@pytest.fixture(scope="session", autouse=True)
def start_calculator(speed):
    """ Предварительный запуск калькулятора перед тестами """
    print(f"\n\nTest speed: {speed}")
    Calculator().start_calculator()
