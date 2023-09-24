from core.rest_client import RestClient


# 归属地接口
class Api(RestClient):
    def __init__(self):
        super().__init__()

    def get_moblie_belong(self, **kwargs):
        return self.get('/v2/phone', **kwargs)

    def post_data(self, **kwargs):
        return self.post('/posts', **kwargs)


api_util = Api()
