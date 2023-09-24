import pytest

from api.api import mobile_query
from utils.read import baseDataRead


def test_mobile():
    params = {'tel': baseDataRead.read_data()['moblie_belong']}
    results = mobile_query(params)
    assert results['code'] == 200
    assert results['msg'] == '获取成功'
    assert results['data']['local'] == '内蒙古自治区锡林郭勒盟'
    assert results['data']['num'] == "1394794"


if __name__ == '__main__':
    pytest.main()
