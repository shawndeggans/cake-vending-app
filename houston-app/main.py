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

DEVICE_ID_HOUSTON = os.environ.get("DEVICE_ID_HOUSTON")
ID_SCOPE_HOUSTON = os.environ.get("ID_SCOPE_HOUSTON")
PRIMARY_KEY_HOUSTON = os.environ.get("PRIMARY_KEY_HOUSTON")

houston_client = IoTCClient(
    DEVICE_ID_HOUSTON,
    ID_SCOPE_HOUSTON,
    IOTCConnectType.IOTC_CONNECT_DEVICE_KEY,
    PRIMARY_KEY_HOUSTON,
    None,
    None
)
        
async def sendHoustonTelemetry():
    await houston_client.connect()
    while houston_client.is_connected():
        print("client connected {}".format(houston_client._device_client.connected))
        await houston_client.send_telemetry(
            {
                "CakeInventoryFilled": 0,
                "CakeInventoryPurchased": getPurchaseAmount(),
                "FridgeTemperature": getTemperature(),
                "LocationLatitude": 32.78306,
                "LocationLongitude": -96.80667
            }
        )
        await asyncio.sleep(3)

async def main():
    await sendHoustonTelemetry()

asyncio.run(main())