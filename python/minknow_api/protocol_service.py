### THIS FILE IS AUTOGENERATED. DO NOT EDIT THIS FILE DIRECTLY ###
from .protocol_pb2_grpc import *
from . import protocol_pb2
from minknow_api.protocol_pb2 import *
from minknow_api._support import MessageWrapper, ArgumentError
import time
import logging

__all__ = [
    "ProtocolService",
    "ProtocolRunUserInfo",
    "StartProtocolRequest",
    "StartProtocolResponse",
    "StopProtocolRequest",
    "StopProtocolResponse",
    "ListProtocolsRequest",
    "ProtocolInfo",
    "ListProtocolsResponse",
    "WaitForFinishedRequest",
    "GetRunInfoRequest",
    "Epi2meWorkflowReference",
    "ProtocolRunInfo",
    "ListProtocolRunsRequest",
    "ListProtocolRunsResponse",
    "GetCurrentProtocolRunRequest",
    "GetCurrentProtocolRunResponse",
    "WatchCurrentProtocolRunRequest",
    "GetContextInfoRequest",
    "GetContextInfoResponse",
    "SetContextInfoRequest",
    "SetContextInfoResponse",
    "GetSampleIdRequest",
    "GetSampleIdResponse",
    "SetSampleIdRequest",
    "SetSampleIdResponse",
    "GetProtocolPurposeRequest",
    "GetProtocolPurposeResponse",
    "SetProtocolPurposeRequest",
    "SetProtocolPurposeResponse",
    "AddEpi2meWorkflowRequest",
    "AddEpi2meWorkflowResponse",
    "ListProtocolGroupIdsRequest",
    "ListProtocolGroupIdsResponse",
    "ProtocolState",
    "PROTOCOL_RUNNING",
    "PROTOCOL_WAITING_FOR_TEMPERATURE",
    "PROTOCOL_WAITING_FOR_ACQUISITION",
    "PROTOCOL_COMPLETED",
    "PROTOCOL_STOPPED_BY_USER",
    "PROTOCOL_FINISHED_WITH_ERROR",
    "PROTOCOL_FINISHED_WITH_DEVICE_ERROR",
    "PROTOCOL_FINISHED_UNABLE_TO_SEND_TELEMETRY",
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


class ProtocolService(object):
    def __init__(self, channel):
        self._stub = ProtocolServiceStub(channel)
        self._pb = protocol_pb2

    def start_protocol(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.start_protocol, _message, _timeout, [], "minknow_api.protocol.ProtocolService")

        unused_args = set(kwargs.keys())

        _message = StartProtocolRequest()

        if "identifier" in kwargs:
            unused_args.remove("identifier")
            _message.identifier = kwargs['identifier']
        else:
            raise ArgumentError("start_protocol requires a 'identifier' argument")

        if "args" in kwargs:
            unused_args.remove("args")
            _message.args.extend(kwargs['args'])

        if "user_info" in kwargs:
            unused_args.remove("user_info")
            _message.user_info.CopyFrom(kwargs['user_info'])

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to start_protocol: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.start_protocol, _message, _timeout, [], "minknow_api.protocol.ProtocolService")

    def stop_protocol(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.stop_protocol, _message, _timeout, [], "minknow_api.protocol.ProtocolService")

        unused_args = set(kwargs.keys())

        _message = StopProtocolRequest()

        if "data_action_on_stop" in kwargs:
            unused_args.remove("data_action_on_stop")
            _message.data_action_on_stop = kwargs['data_action_on_stop']

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to stop_protocol: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.stop_protocol, _message, _timeout, [], "minknow_api.protocol.ProtocolService")

    def wait_for_finished(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.wait_for_finished, _message, _timeout, [], "minknow_api.protocol.ProtocolService")

        unused_args = set(kwargs.keys())

        _message = WaitForFinishedRequest()

        if "run_id" in kwargs:
            unused_args.remove("run_id")
            _message.run_id = kwargs['run_id']
        else:
            raise ArgumentError("wait_for_finished requires a 'run_id' argument")

        if "state" in kwargs:
            unused_args.remove("state")
            _message.state = kwargs['state']

        if "timeout" in kwargs:
            unused_args.remove("timeout")
            _message.timeout = kwargs['timeout']

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to wait_for_finished: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.wait_for_finished, _message, _timeout, [], "minknow_api.protocol.ProtocolService")

    def get_run_info(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.get_run_info, _message, _timeout, [], "minknow_api.protocol.ProtocolService")

        unused_args = set(kwargs.keys())

        _message = GetRunInfoRequest()

        if "run_id" in kwargs:
            unused_args.remove("run_id")
            _message.run_id = kwargs['run_id']

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to get_run_info: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.get_run_info, _message, _timeout, [], "minknow_api.protocol.ProtocolService")

    def list_protocol_runs(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.list_protocol_runs, _message, _timeout, [], "minknow_api.protocol.ProtocolService")

        unused_args = set(kwargs.keys())

        _message = ListProtocolRunsRequest()

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to list_protocol_runs: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.list_protocol_runs, _message, _timeout, [], "minknow_api.protocol.ProtocolService")

    def get_current_protocol_run(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.get_current_protocol_run, _message, _timeout, [], "minknow_api.protocol.ProtocolService")

        unused_args = set(kwargs.keys())

        _message = GetCurrentProtocolRunRequest()

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to get_current_protocol_run: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.get_current_protocol_run, _message, _timeout, [], "minknow_api.protocol.ProtocolService")

    def watch_current_protocol_run(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.watch_current_protocol_run, _message, _timeout, [], "minknow_api.protocol.ProtocolService")

        unused_args = set(kwargs.keys())

        _message = WatchCurrentProtocolRunRequest()

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to watch_current_protocol_run: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.watch_current_protocol_run, _message, _timeout, [], "minknow_api.protocol.ProtocolService")

    def list_protocols(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.list_protocols, _message, _timeout, [], "minknow_api.protocol.ProtocolService")

        unused_args = set(kwargs.keys())

        _message = ListProtocolsRequest()

        if "force_reload" in kwargs:
            unused_args.remove("force_reload")
            _message.force_reload = kwargs['force_reload']

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to list_protocols: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.list_protocols, _message, _timeout, [], "minknow_api.protocol.ProtocolService")

    def get_context_info(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.get_context_info, _message, _timeout, [], "minknow_api.protocol.ProtocolService")

        unused_args = set(kwargs.keys())

        _message = GetContextInfoRequest()

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to get_context_info: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.get_context_info, _message, _timeout, [], "minknow_api.protocol.ProtocolService")

    def set_context_info(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.set_context_info, _message, _timeout, [], "minknow_api.protocol.ProtocolService")

        unused_args = set(kwargs.keys())

        _message = SetContextInfoRequest()

        if "context_info" in kwargs:
            unused_args.remove("context_info")
            _message.context_info.update(kwargs['context_info'])
            

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to set_context_info: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.set_context_info, _message, _timeout, [], "minknow_api.protocol.ProtocolService")

    def get_protocol_purpose(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.get_protocol_purpose, _message, _timeout, [], "minknow_api.protocol.ProtocolService")

        unused_args = set(kwargs.keys())

        _message = GetProtocolPurposeRequest()

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to get_protocol_purpose: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.get_protocol_purpose, _message, _timeout, [], "minknow_api.protocol.ProtocolService")

    def set_protocol_purpose(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.set_protocol_purpose, _message, _timeout, [], "minknow_api.protocol.ProtocolService")

        unused_args = set(kwargs.keys())

        _message = SetProtocolPurposeRequest()

        if "purpose" in kwargs:
            unused_args.remove("purpose")
            _message.purpose = kwargs['purpose']

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to set_protocol_purpose: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.set_protocol_purpose, _message, _timeout, [], "minknow_api.protocol.ProtocolService")

    def add_epi2me_workflow(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.add_epi2me_workflow, _message, _timeout, [], "minknow_api.protocol.ProtocolService")

        unused_args = set(kwargs.keys())

        _message = AddEpi2meWorkflowRequest()

        if "run_id" in kwargs:
            unused_args.remove("run_id")
            _message.run_id = kwargs['run_id']
        else:
            raise ArgumentError("add_epi2me_workflow requires a 'run_id' argument")

        if "epi2me_workflow" in kwargs:
            unused_args.remove("epi2me_workflow")
            _message.epi2me_workflow.CopyFrom(kwargs['epi2me_workflow'])
        else:
            raise ArgumentError("add_epi2me_workflow requires a 'epi2me_workflow' argument")

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to add_epi2me_workflow: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.add_epi2me_workflow, _message, _timeout, [], "minknow_api.protocol.ProtocolService")

    def list_protocol_group_ids(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.list_protocol_group_ids, _message, _timeout, [], "minknow_api.protocol.ProtocolService")

        unused_args = set(kwargs.keys())

        _message = ListProtocolGroupIdsRequest()

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to list_protocol_group_ids: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.list_protocol_group_ids, _message, _timeout, [], "minknow_api.protocol.ProtocolService")