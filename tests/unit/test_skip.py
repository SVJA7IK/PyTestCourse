import time
import pytest


@pytest.mark.skip(reason="I don't want to run this test (skip)")
def test_slow_test():
    time.sleep(1)


@pytest.mark.skipif('config.getoption("--speed") == "quickly"')
def test_slow_test_with_skip_condition():
    time.sleep(1)
