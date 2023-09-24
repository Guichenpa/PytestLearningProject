import pytest

from api.api import post_test_json
from utils.read import baseDataRead


def test_post():
    """
    测试post接口
    :return:
    """
    print("\n")
    json_data = baseDataRead.read_data()['json_data']
    results = post_test_json(json_data)
    assert results['id'] == 101


if __name__ == '__main__':
    pytest.main()
