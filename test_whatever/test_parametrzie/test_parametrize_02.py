import pytest

from utils.read_data import get_data


# 单参数
# @pytest.mark.parametrize("name", get_data['hero_name'])
# def test_parametrize_02(name):
#     print("\n" + name)

# 多参数
@pytest.mark.parametrize("name,words", get_data['herosall'])
def test_parametrize_02(name, words):
    print(f'\n{name}的台词是{words}')
