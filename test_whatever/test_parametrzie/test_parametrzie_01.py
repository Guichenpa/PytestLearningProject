import pytest


# 单参数.单次循环
@pytest.mark.parametrize("key", ["Zard"])
def test_parametrize(key):
    # print("我是" + key)
    assert key == "Zard"


# 单参数.多次循环
@pytest.mark.parametrize("key", ["Zard", "White", "uzi"])
def test_parametrize(key):
    # print("我是" + key)
    assert key == "Zard"
    assert key == "White"
    assert key == "uzi"
