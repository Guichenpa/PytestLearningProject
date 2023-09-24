# import requests
#
# #
# # params = {
# #     'tel': '13947948806'
# # }
# # r = requests.get('https://tenapi.cn/v2/phone', params=params)
# # print(r.status_code)
# # print(r.json())
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
