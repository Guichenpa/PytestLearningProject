from core.api_util import api_util


# 归属地查血接口
def mobile_query(params):
    response = api_util.get_moblie_belong(params=params)
    return response.json()


def post_test_json(json_data):
    """
    这个方法，测试json传参
    :param json_data:
    :return:
    """
    response = api_util.post_data(json=json_data)
    return response.json()
