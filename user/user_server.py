from concurrent import futures
import copy

from loguru import logger

import grpc

import user_pb2
import user_pb2_grpc

userdb = [{"user_id": 1, "user_name": "leilei", "email": "wanglei311600@qq.com", "mobile": "10086", "token": "11111"},
          {"user_id": 2, "user_name": "pork", "email": "pork@qq.com", "mobile": "10010", "token": "22222"},
          {"user_id": 3, "user_name": "poker", "email": "poker@qq.com", "mobile": "12315", "token": "33333"}]


def get_user_id(email=None):
    logger.debug(email)
    for user in userdb:
        if user["email"] == email:
            logger.debug(user)
            return user["user_id"]


def get_user_mobiles(ids: list):
    res = []
    ids.sort()
    for user in userdb:
        if user["user_id"] in ids:
            res.append(user["mobile"])
    return res


def get_user_by_token(token):
    for user in userdb:
        if user["token"] == token:
            _user = copy.deepcopy(user)
            _user.pop("token")
            return _user


def get_user_mobile(id):
    for user in userdb:
        if user["user_id"] == id:
            return user["mobile"]


class UserServer(user_pb2_grpc.UserServiceServicer):

    def getUserId(self, request, context):
        id = get_user_id(request.email)
        logger.debug(id)
        return user_pb2.IdResponse(userId=id)

    def getUserMobiles(self, request, context):
        logger.debug(request.userId)
        mobiles = get_user_mobiles(request.userId)
        logger.debug(mobiles)
        return user_pb2.UserMobilesResponse(mobile=mobiles)

    def getUserByToken(self, request, context):
        logger.debug(request.token)
        res = get_user_by_token(request.token)
        logger.debug(res)
        return user_pb2.UserInfoResponse(**res)
        # return user_pb2.UserInfoResponse(user_id=res["user_id"],user_name=res["user_name"],email=res["email"],mobile=res["mobile"])

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(UserServer(), server)
    server.add_insecure_port("[::]:50053")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
