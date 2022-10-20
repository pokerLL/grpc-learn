import grpc

import user_pb2
import user_pb2_grpc


class UserClient:

    def __init__(self):
        self.host = "localhost"
        self.port = "50053"

    def get_user_id(self, email):
        with grpc.insecure_channel(self.host + ":" + self.port) as channel:
            grpc_client = user_pb2_grpc.UserServiceStub(channel=channel)
            res = grpc_client.getUserId(user_pb2.IdRequest(email=email))
            return res.userId

    def get_user_mobiles(self, ids: list):
        with grpc.insecure_channel(self.host + ":" + self.port) as channel:
            grpc_client = user_pb2_grpc.UserServiceStub(channel=channel)
            res = grpc_client.getUserMobiles(user_pb2.UserIdsRequest(userId=ids))
            return res

    def get_user_by_token(self, token):
        with grpc.insecure_channel(self.host + ":" + self.port) as channel:
            grpc_client = user_pb2_grpc.UserServiceStub(channel=channel)
            res = grpc_client.getUserByToken(user_pb2.UserTokenRequest(token=token))
            return res


if __name__ == "__main__":
    client = UserClient()
    res = client.get_user_id("pork@qq.com")
    ids = [1, 2]
    res = client.get_user_mobiles(ids)
    print(res.mobile)
    tk = "11111"
    res = client.get_user_by_token(tk)
    print(res)
