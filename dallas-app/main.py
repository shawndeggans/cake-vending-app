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
DEVICE_ID_DALLAS = os.environ.get("DEVICE_ID_DALLAS")
ID_SCOPE_DALLAS = os.environ.get("ID_SCOPE_DALLAS")
PRIMARY_KEY_DALLAS = os.environ.get("PRIMARY_KEY_DALLAS")

# Create our three different clients
dallas_client = IoTCClient(
    DEVICE_ID_DALLAS,
    ID_SCOPE_DALLAS,
    IOTCConnectType.IOTC_CONNECT_DEVICE_KEY,
    PRIMARY_KEY_DALLAS,
    None,
    None)

async def sendDallasTelemetry():
    await dallas_client.connect()
    while dallas_client.is_connected():
        print("client connected {}".format(dallas_client._device_client.connected))
        await dallas_client.send_telemetry(
            {
                "CakeInventoryFilled": 0,
                "CakeInventoryPurchased": getPurchaseAmount(),
                "FridgeTemperature": getTemperature(),
                "LocationLatitude": 32.78306,
                "LocationLongitude": -96.80667
            }
        )
        await asyncio.sleep(900)

async def main():
    await sendDallasTelemetry()

asyncio.run(main())