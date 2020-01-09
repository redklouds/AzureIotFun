#IOT HUB -> SEND TO THE IOT HUB


from azure.iot.hub import IoTHubRegistryManager
#from azure.iot.device.iothub.models import MethodRequest, MethodResponse

from azure.iot.hub.protocol.models import CloudToDeviceMethod

iohub_str = "HostName=pythonIotTest.azure-devices.net;SharedAccessKeyName=service;SharedAccessKey=sdQb+03B4y9PIqUa6JNn/dxWQ5YECQNk8Qb6z2cIsNQ="
device_con_str = "HostName=pythonIotTest.azure-devices.net;DeviceId=DannysDevice;SharedAccessKey=uSNG511Rlb0zdvzEZ5nkQyhDEFNAuf4GRyLpHNmW2B4="


device_id = "DannysDevice"

method_name = "method1"
method_payload = {"MethodPayload":"Danny"}

try:
    # Create IoTHubRegistryManager
    registry_manager = IoTHubRegistryManager(iohub_str)
    #deviceMethod = MethodRequest(name=method_name, request_id=1, payload=method_payload)
    deviceMethod = CloudToDeviceMethod(method_name=method_name, payload=method_payload)
    resp = registry_manager.invoke_device_method(device_id, deviceMethod)
    print(resp.payload)


except Exception as ex:
    print("Unexpected error {0}".format(ex))
except KeyboardInterrupt:
    print("iothub_registry_manager_sample stopped")