import threading, time
from azure.iot.device import IoTHubDeviceClient
#from azure.iot.device import IoTHubModuleClient

RECEIVED_MESSAGES = 0

CONNECTION_STRING = "HostName=pythonIotTest.azure-devices.net;DeviceId=DannysDevice;SharedAccessKey=uSNG511Rlb0zdvzEZ5nkQyhDEFNAuf4GRyLpHNmW2B4="

def message_listener(client):
    global RECEIVED_MESSAGES
    while True:
        message = client.receive_message()
        RECEIVED_MESSAGES += 1
        print("Message received")
        print( "    Data: <<{}>>".format(message.data) )
        print( "    Properties: {}".format(message.custom_properties))
        print( "    Total calls received: {}".format(RECEIVED_MESSAGES))

def iothub_client_init():
    #client = IoTHubModuleClient.create_from_connection_string(CONNECTION_STRING)
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client

def iothub_client_sample_run():
    try:
        client = iothub_client_init()

        message_listener_thread = threading.Thread(target=message_listener, args=(client,))
        message_listener_thread.daemon = True
        message_listener_thread.start()

        while True:
            time.sleep(1000)

    except KeyboardInterrupt:
        print ( "IoTHubDeviceClient sample stopped" )

if __name__ == '__main__':
    print ( "Starting the IoT Hub Python sample..." )
    print ( "IoTHubDeviceClient waiting for commands, press Ctrl-C to exit" )

    iothub_client_sample_run()