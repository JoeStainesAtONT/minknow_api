### THIS FILE IS AUTOGENERATED. DO NOT EDIT THIS FILE DIRECTLY ###
from .instance_pb2_grpc import *
from . import instance_pb2
from minknow_api.instance_pb2 import *
from minknow_api._support import MessageWrapper, ArgumentError
import time
import logging

__all__ = [
    "InstanceService",
    "GetVersionInfoRequest",
    "GetVersionInfoResponse",
    "GetOutputDirectoriesRequest",
    "OutputDirectories",
    "GetDefaultOutputDirectoriesRequest",
    "SetOutputDirectoryRequest",
    "SetOutputDirectoryResponse",
    "SetReadsDirectoryRequest",
    "SetReadsDirectoryResponse",
    "FilesystemDiskSpaceInfo",
    "GetDiskSpaceInfoRequest",
    "StreamDiskSpaceInfoRequest",
    "GetDiskSpaceInfoResponse",
    "GetMachineIdRequest",
    "GetMachineIdResponse",
    "GetHostTypeRequest",
    "GetHostTypeResponse",
    "StreamInstanceActivityRequest",
    "DeviceInfo",
    "StreamInstanceActivityResponse",
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


class InstanceService(object):
    def __init__(self, channel):
        self._stub = InstanceServiceStub(channel)
        self._pb = instance_pb2

    def get_version_info(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.get_version_info, _message, _timeout, [], "minknow_api.instance.InstanceService")

        unused_args = set(kwargs.keys())

        _message = GetVersionInfoRequest()

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to get_version_info: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.get_version_info, _message, _timeout, [], "minknow_api.instance.InstanceService")

    def get_output_directories(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.get_output_directories, _message, _timeout, [], "minknow_api.instance.InstanceService")

        unused_args = set(kwargs.keys())

        _message = GetOutputDirectoriesRequest()

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to get_output_directories: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.get_output_directories, _message, _timeout, [], "minknow_api.instance.InstanceService")

    def get_default_output_directories(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.get_default_output_directories, _message, _timeout, [], "minknow_api.instance.InstanceService")

        unused_args = set(kwargs.keys())

        _message = GetDefaultOutputDirectoriesRequest()

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to get_default_output_directories: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.get_default_output_directories, _message, _timeout, [], "minknow_api.instance.InstanceService")

    def set_output_directory(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.set_output_directory, _message, _timeout, [], "minknow_api.instance.InstanceService")

        unused_args = set(kwargs.keys())

        _message = SetOutputDirectoryRequest()

        if "path" in kwargs:
            unused_args.remove("path")
            _message.path = kwargs['path']

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to set_output_directory: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.set_output_directory, _message, _timeout, [], "minknow_api.instance.InstanceService")

    def set_reads_directory(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.set_reads_directory, _message, _timeout, [], "minknow_api.instance.InstanceService")

        unused_args = set(kwargs.keys())

        _message = SetReadsDirectoryRequest()

        if "path" in kwargs:
            unused_args.remove("path")
            _message.path = kwargs['path']

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to set_reads_directory: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.set_reads_directory, _message, _timeout, [], "minknow_api.instance.InstanceService")

    def get_disk_space_info(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.get_disk_space_info, _message, _timeout, [], "minknow_api.instance.InstanceService")

        unused_args = set(kwargs.keys())

        _message = GetDiskSpaceInfoRequest()

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to get_disk_space_info: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.get_disk_space_info, _message, _timeout, [], "minknow_api.instance.InstanceService")

    def stream_disk_space_info(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.stream_disk_space_info, _message, _timeout, [], "minknow_api.instance.InstanceService")

        unused_args = set(kwargs.keys())

        _message = StreamDiskSpaceInfoRequest()

        if "period" in kwargs:
            unused_args.remove("period")
            _message.period = kwargs['period']

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to stream_disk_space_info: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.stream_disk_space_info, _message, _timeout, [], "minknow_api.instance.InstanceService")

    def get_machine_id(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.get_machine_id, _message, _timeout, [], "minknow_api.instance.InstanceService")

        unused_args = set(kwargs.keys())

        _message = GetMachineIdRequest()

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to get_machine_id: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.get_machine_id, _message, _timeout, [], "minknow_api.instance.InstanceService")

    def get_host_type(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.get_host_type, _message, _timeout, [], "minknow_api.instance.InstanceService")

        unused_args = set(kwargs.keys())

        _message = GetHostTypeRequest()

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to get_host_type: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.get_host_type, _message, _timeout, [], "minknow_api.instance.InstanceService")

    def stream_instance_activity(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.stream_instance_activity, _message, _timeout, [], "minknow_api.instance.InstanceService")

        unused_args = set(kwargs.keys())

        _message = StreamInstanceActivityRequest()

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to stream_instance_activity: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.stream_instance_activity, _message, _timeout, [], "minknow_api.instance.InstanceService")