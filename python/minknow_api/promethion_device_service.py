### THIS FILE IS AUTOGENERATED. DO NOT EDIT THIS FILE DIRECTLY ###
from .promethion_device_pb2_grpc import *
from . import promethion_device_pb2
from minknow_api.promethion_device_pb2 import *
from minknow_api._support import MessageWrapper, ArgumentError
import time
import logging

__all__ = [
    "PromethionDeviceService",
    "WaveformSettings",
    "DeviceSettings",
    "TimingEnginePeriods",
    "PixelBlockSettings",
    "PixelSettings",
    "ChangeDeviceSettingsRequest",
    "ChangeDeviceSettingsResponse",
    "GetDeviceSettingsRequest",
    "GetDeviceSettingsResponse",
    "ChangePixelBlockSettingsRequest",
    "ChangePixelBlockSettingsResponse",
    "GetPixelBlockSettingsRequest",
    "GetPixelBlockSettingsResponse",
    "ChangePixelSettingsRequest",
    "ChangePixelSettingsResponse",
    "GetPixelSettingsRequest",
    "GetPixelSettingsResponse",
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


class PromethionDeviceService(object):
    def __init__(self, channel):
        self._stub = PromethionDeviceServiceStub(channel)
        self._pb = promethion_device_pb2

    def change_device_settings(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.change_device_settings, _message, _timeout, [], "minknow_api.promethion_device.PromethionDeviceService")

        unused_args = set(kwargs.keys())

        _message = ChangeDeviceSettingsRequest()

        if "sampling_frequency" in kwargs:
            unused_args.remove("sampling_frequency")
            _message.settings.sampling_frequency.value = kwargs['sampling_frequency']

        if "ramp_voltage" in kwargs:
            unused_args.remove("ramp_voltage")
            _message.settings.ramp_voltage.value = kwargs['ramp_voltage']

        if "bias_voltage" in kwargs:
            unused_args.remove("bias_voltage")
            _message.settings.bias_voltage = kwargs['bias_voltage']

        if "bias_voltage_waveform" in kwargs:
            unused_args.remove("bias_voltage_waveform")
            _message.settings.bias_voltage_waveform.CopyFrom(kwargs['bias_voltage_waveform'])

        if "saturation_control_enabled" in kwargs:
            unused_args.remove("saturation_control_enabled")
            _message.settings.saturation_control_enabled.value = kwargs['saturation_control_enabled']

        if "fast_calibration_enabled" in kwargs:
            unused_args.remove("fast_calibration_enabled")
            _message.settings.fast_calibration_enabled.value = kwargs['fast_calibration_enabled']

        if "temperature_target" in kwargs:
            unused_args.remove("temperature_target")
            _message.settings.temperature_target.value = kwargs['temperature_target']

        if "timings" in kwargs:
            unused_args.remove("timings")
            _message.settings.timings.CopyFrom(kwargs['timings'])

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to change_device_settings: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.change_device_settings, _message, _timeout, [], "minknow_api.promethion_device.PromethionDeviceService")

    def get_device_settings(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.get_device_settings, _message, _timeout, ["settings"], "minknow_api.promethion_device.PromethionDeviceService")

        unused_args = set(kwargs.keys())

        _message = GetDeviceSettingsRequest()

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to get_device_settings: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.get_device_settings, _message, _timeout, ["settings"], "minknow_api.promethion_device.PromethionDeviceService")

    def change_pixel_block_settings(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.change_pixel_block_settings, _message, _timeout, [], "minknow_api.promethion_device.PromethionDeviceService")

        unused_args = set(kwargs.keys())

        _message = ChangePixelBlockSettingsRequest()

        if "pixel_blocks" in kwargs:
            unused_args.remove("pixel_blocks")
            for key, value in kwargs['pixel_blocks'].items():
                _message.pixel_blocks[key].CopyFrom(value)

        if "pixel_block_default" in kwargs:
            unused_args.remove("pixel_block_default")
            _message.pixel_block_default.CopyFrom(kwargs['pixel_block_default'])

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to change_pixel_block_settings: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.change_pixel_block_settings, _message, _timeout, [], "minknow_api.promethion_device.PromethionDeviceService")

    def get_pixel_block_settings(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.get_pixel_block_settings, _message, _timeout, [], "minknow_api.promethion_device.PromethionDeviceService")

        unused_args = set(kwargs.keys())

        _message = GetPixelBlockSettingsRequest()

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to get_pixel_block_settings: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.get_pixel_block_settings, _message, _timeout, [], "minknow_api.promethion_device.PromethionDeviceService")

    def change_pixel_settings(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.change_pixel_settings, _message, _timeout, [], "minknow_api.promethion_device.PromethionDeviceService")

        unused_args = set(kwargs.keys())

        _message = ChangePixelSettingsRequest()

        if "pixels" in kwargs:
            unused_args.remove("pixels")
            for key, value in kwargs['pixels'].items():
                _message.pixels[key].CopyFrom(value)

        if "pixel_default" in kwargs:
            unused_args.remove("pixel_default")
            _message.pixel_default.CopyFrom(kwargs['pixel_default'])

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to change_pixel_settings: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.change_pixel_settings, _message, _timeout, [], "minknow_api.promethion_device.PromethionDeviceService")

    def get_pixel_settings(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.get_pixel_settings, _message, _timeout, [], "minknow_api.promethion_device.PromethionDeviceService")

        unused_args = set(kwargs.keys())

        _message = GetPixelSettingsRequest()

        if "pixels" in kwargs:
            unused_args.remove("pixels")
            _message.pixels.extend(kwargs['pixels'])
        else:
            raise ArgumentError("get_pixel_settings requires a 'pixels' argument")

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to get_pixel_settings: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.get_pixel_settings, _message, _timeout, [], "minknow_api.promethion_device.PromethionDeviceService")