import requests


def test_mobile():
    params = {
        'tel': '13947948806'
    }
    r = requests.get('https://tenapi.cn/v2/phone', params=params)
    print(r.status_code)
    assert r.status_code == 200
    results = r.json()
    assert results['code'] == 200
    assert results['msg'] == '获取成功'
    assert results['data']['local'] == '内蒙古自治区锡林郭勒盟'
    assert results['data']['num'] == "1394794"
# assert results['code'] == 200
# assert results['msg'] == '获取成功'
# assert results['isp'] == '中国移动'

# params={
#     'tel': '13947948806'
# }
# r=requests.get('https://tenapi.cn/v2/phone', params=params)
# print(r.status_code)
# print(r.json())
# rpost=requests.post('https://tenapi.cn/v2/phone',param=params)
# print(rpost.status_code)
# print(rpost.json())
# doubanUrl = "https://movie.douban.com/j/search_subjects"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
# }
# params = {
#     'tel': '13947948806',
#     'tag': '热门',
#     'page_limit': 50,
#     'page_start': 0
# }
# r = requests.get(doubanUrl, headers=headers, params=params)
#
# print(r.status_code)
# print(r.json())
