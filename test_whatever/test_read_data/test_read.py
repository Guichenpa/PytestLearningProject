import pytest
import requests

from utils.read import baseDataRead

url = baseDataRead.read_ini()['host']['api_sit_url']


@pytest.mark.parametrize("tele", baseDataRead.read_data()["moblie_belong"])
def test_mobile(tele):
    params = {
        'tel': tele
    }
    r = requests.get(url, params)
    print(r.status_code)
    assert r.status_code == 200
    results = r.json()
    assert results['code'] == 200
    assert results['msg'] == '获取成功'
    assert results['data']['local'] == '内蒙古自治区锡林郭勒盟'
    assert results['data']['num'] == "1394794"


if __name__ == '__main__':
    pytest.main()
