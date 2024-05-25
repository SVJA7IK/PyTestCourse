import pytest
from main import ZeroReceivedError, calculate_pnl
from contextlib import nullcontext as does_not_raise


@pytest.mark.parametrize(
    "spent, received, res, expectation",
    [
        (5, 10, 5, does_not_raise()),
        (10, 5, -5, does_not_raise()),
        # Обрабатывать ошибки TypeError и ZeroReceivedError
        (5, "-1", -5, pytest.raises(TypeError)),
        (5, 0, -5, pytest.raises(ZeroReceivedError)),
    ],
)
def test_calculate_pnl(spent, received, res, expectation):
    """Тестирование функции через параметризацию"""
    with expectation:
        assert calculate_pnl(spent, received) == res
