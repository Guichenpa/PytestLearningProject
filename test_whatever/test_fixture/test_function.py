import pytest
import requests


# @pytest.fixture(autouse=True)
# def func():
#     print("我是前置步骤")


def test_mobile(get_param):
    # params = {
    #     'tel': '13947948806'
    # }
    r = requests.get('https://tenapi.cn/v2/phone', params=get_param)
    print(r.status_code)
    assert r.status_code == 200
    results = r.json()
    assert results['code'] == 200
    assert results['msg'] == '获取成功'
    assert results['data']['local'] == '内蒙古自治区锡林郭勒盟'
    assert results['data']['num'] == "1394794"


def test_mobile2():
    params = {
        'tel': '17640439751'
    }
    r = requests.get('https://tenapi.cn/v2/phone', params=params)
    print(r.status_code)
    assert r.status_code == 200
    results = r.json()
    assert results['code'] == 200
    assert results['msg'] == '获取成功'
    assert results['data']['local'] == '中国'
    assert results['data']['num'] == "1764043"


if __name__ == '__main__':
    pytest.main()
