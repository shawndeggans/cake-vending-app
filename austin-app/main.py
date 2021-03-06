from dotenv import load_dotenv
import sys, asyncio, os, json, time
from iotc import (
    IOTCConnectType,
    IOTCLogLevel,
    IOTCEvents,
    Command,
    CredentialsCache,
    Storage,
)
from iotc.aio import IoTCClient
from random import randint, uniform

load_dotenv()

def getPurchaseAmount():
    return randint(1,5)

def getTemperature():
    return round(uniform(8.88, 16.66))

# Load the device connection values
DEVICE_ID_AUSTIN = os.environ.get("DEVICE_ID_AUSTIN")
ID_SCOPE_AUSTIN = os.environ.get("ID_SCOPE_AUSTIN")
PRIMARY_KEY_AUSTIN = os.environ.get("PRIMARY_KEY_AUSTIN")


austin_client = IoTCClient(
    DEVICE_ID_AUSTIN,
    ID_SCOPE_AUSTIN,
    IOTCConnectType.IOTC_CONNECT_DEVICE_KEY,
    PRIMARY_KEY_AUSTIN,
    None,
    None
)
        
async def sendAustinTelemetry():
    await austin_client.connect()
    while austin_client.is_connected():
        print("client connected {}".format(austin_client._device_client.connected))
        await austin_client.send_telemetry(
            {
                "CakeInventoryFilled": 0,
                "CakeInventoryPurchased": getPurchaseAmount(),
                "FridgeTemperature": getTemperature(),
                "LocationLatitude": 30.26715,
                "LocationLongitude": -95.36327
            }
        )
        await asyncio.sleep(900)

async def main():
    await sendAustinTelemetry()

asyncio.run(main())