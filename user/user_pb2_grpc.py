# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import user_pb2 as user__pb2


class UserServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getUserId = channel.unary_unary(
                '/com.deepwisdom.grpc.user.UserService/getUserId',
                request_serializer=user__pb2.IdRequest.SerializeToString,
                response_deserializer=user__pb2.IdResponse.FromString,
                )
        self.getUserMobiles = channel.unary_unary(
                '/com.deepwisdom.grpc.user.UserService/getUserMobiles',
                request_serializer=user__pb2.UserIdsRequest.SerializeToString,
                response_deserializer=user__pb2.UserMobilesResponse.FromString,
                )
        self.getUserByToken = channel.unary_unary(
                '/com.deepwisdom.grpc.user.UserService/getUserByToken',
                request_serializer=user__pb2.UserTokenRequest.SerializeToString,
                response_deserializer=user__pb2.UserInfoResponse.FromString,
                )


class UserServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getUserId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getUserMobiles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getUserByToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getUserId': grpc.unary_unary_rpc_method_handler(
                    servicer.getUserId,
                    request_deserializer=user__pb2.IdRequest.FromString,
                    response_serializer=user__pb2.IdResponse.SerializeToString,
            ),
            'getUserMobiles': grpc.unary_unary_rpc_method_handler(
                    servicer.getUserMobiles,
                    request_deserializer=user__pb2.UserIdsRequest.FromString,
                    response_serializer=user__pb2.UserMobilesResponse.SerializeToString,
            ),
            'getUserByToken': grpc.unary_unary_rpc_method_handler(
                    servicer.getUserByToken,
                    request_deserializer=user__pb2.UserTokenRequest.FromString,
                    response_serializer=user__pb2.UserInfoResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.deepwisdom.grpc.user.UserService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getUserId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.deepwisdom.grpc.user.UserService/getUserId',
            user__pb2.IdRequest.SerializeToString,
            user__pb2.IdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getUserMobiles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.deepwisdom.grpc.user.UserService/getUserMobiles',
            user__pb2.UserIdsRequest.SerializeToString,
            user__pb2.UserMobilesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getUserByToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.deepwisdom.grpc.user.UserService/getUserByToken',
            user__pb2.UserTokenRequest.SerializeToString,
            user__pb2.UserInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
