### THIS FILE IS AUTOGENERATED. DO NOT EDIT THIS FILE DIRECTLY ###
from .keystore_pb2_grpc import *
from . import keystore_pb2
from minknow_api.keystore_pb2 import *
from minknow_api._support import MessageWrapper, ArgumentError
import time
import logging

__all__ = [
    "KeyStoreService",
    "StoreRequest",
    "StoreResponse",
    "RemoveRequest",
    "RemoveResponse",
    "GetOneRequest",
    "GetOneResponse",
    "GetRequest",
    "GetResponse",
    "WatchRequest",
    "WatchResponse",
    "Lifetime",
    "UNTIL_NEXT_PROTOCOL_START",
    "UNTIL_PROTOCOL_END",
    "UNTIL_INSTANCE_END",
]

def run_with_retry(method, message, timeout, unwraps, full_name):
    retry_count = 20
    error = None
    for i in range(retry_count):
        try:
            result = MessageWrapper(method(message, timeout=timeout), unwraps=unwraps)
            return result
        except grpc.RpcError as e:
            # Retrying unidentified grpc errors to keep clients from crashing
            retryable_error = (e.code() == grpc.StatusCode.UNKNOWN and "Stream removed" in e.details() or \
                                (e.code() == grpc.StatusCode.INTERNAL and "RST_STREAM" in e.details()))
            if retryable_error:
                logging.info('Bypassed ({}: {}) error for grpc: {}. Attempt {}.'.format(e.code(), e.details(), full_name, i))
            else:
                raise
            error = e
        time.sleep(1)
    raise error


class KeyStoreService(object):
    def __init__(self, channel):
        self._stub = KeyStoreServiceStub(channel)
        self._pb = keystore_pb2

    def store(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.store, _message, _timeout, [], "minknow_api.keystore.KeyStoreService")

        unused_args = set(kwargs.keys())

        _message = StoreRequest()

        if "values" in kwargs:
            unused_args.remove("values")
            for key, value in kwargs['values'].items():
                if value.DESCRIPTOR.full_name == 'google.protobuf.Any':
                    _message.values[key].CopyFrom(value)
                else:
                    _message.values[key].Pack(value)
        else:
            raise ArgumentError("store requires a 'values' argument")

        if "lifetime" in kwargs:
            unused_args.remove("lifetime")
            _message.lifetime = kwargs['lifetime']

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to store: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.store, _message, _timeout, [], "minknow_api.keystore.KeyStoreService")

    def remove(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.remove, _message, _timeout, [], "minknow_api.keystore.KeyStoreService")

        unused_args = set(kwargs.keys())

        _message = RemoveRequest()

        if "names" in kwargs:
            unused_args.remove("names")
            _message.names.extend(kwargs['names'])
        else:
            raise ArgumentError("remove requires a 'names' argument")

        if "allow_missing" in kwargs:
            unused_args.remove("allow_missing")
            _message.allow_missing = kwargs['allow_missing']

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to remove: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.remove, _message, _timeout, [], "minknow_api.keystore.KeyStoreService")

    def get_one(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.get_one, _message, _timeout, [], "minknow_api.keystore.KeyStoreService")

        unused_args = set(kwargs.keys())

        _message = GetOneRequest()

        if "name" in kwargs:
            unused_args.remove("name")
            _message.name = kwargs['name']
        else:
            raise ArgumentError("get_one requires a 'name' argument")

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to get_one: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.get_one, _message, _timeout, [], "minknow_api.keystore.KeyStoreService")

    def get(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.get, _message, _timeout, [], "minknow_api.keystore.KeyStoreService")

        unused_args = set(kwargs.keys())

        _message = GetRequest()

        if "names" in kwargs:
            unused_args.remove("names")
            _message.names.extend(kwargs['names'])

        if "allow_missing" in kwargs:
            unused_args.remove("allow_missing")
            _message.allow_missing = kwargs['allow_missing']

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to get: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.get, _message, _timeout, [], "minknow_api.keystore.KeyStoreService")

    def watch(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.watch, _message, _timeout, [], "minknow_api.keystore.KeyStoreService")

        unused_args = set(kwargs.keys())

        _message = WatchRequest()

        if "names" in kwargs:
            unused_args.remove("names")
            _message.names.extend(kwargs['names'])
        else:
            raise ArgumentError("watch requires a 'names' argument")

        if "allow_missing" in kwargs:
            unused_args.remove("allow_missing")
            _message.allow_missing = kwargs['allow_missing']

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to watch: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.watch, _message, _timeout, [], "minknow_api.keystore.KeyStoreService")