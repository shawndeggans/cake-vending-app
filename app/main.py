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


def getHoustonData():
    data = {
        "CakeInventoryFilled": 0,
        "CakeInventoryPurchased": getPurchaseAmount(),
        "FridgeTemperature": getTemperature(),
        "LocationLatitude": 29.76328,
        "LocationLongitude": -95.36327
    }
    return json.dumps(data)

def getAustinData():
    data = {
        "CakeInventoryFilled": 0,
        "CakeInventoryPurchased": getPurchaseAmount(),
        "FridgeTemperature": getTemperature(),
        "LocationLatitude": 30.26715,
        "LocationLongitude": -95.36327
    }
    return json.dumps(data)

DEVICE_ID_AUSTIN = os.environ.get("DEVICE_ID_AUSTIN")
ID_SCOPE_AUSTIN = os.environ.get("ID_SCOPE_AUSTIN")
PRIMARY_KEY_AUSTIN = os.environ.get("PRIMARY_KEY_AUSTIN")

DEVICE_ID_HOUSTON = os.environ.get("DEVICE_ID_HOUSTON")
ID_SCOPE_HOUSTON = os.environ.get("ID_SCOPE_HOUSTON")
PRIMARY_KEY_HOUSTON = os.environ.get("PRIMARY_KEY_HOUSTON")

# Create our three different clients
dallas_client = IoTCClient(
    DEVICE_ID_DALLAS,
    ID_SCOPE_DALLAS,
    IOTCConnectType.IOTC_CONNECT_DEVICE_KEY,
    PRIMARY_KEY_DALLAS,
    None,
    None)

austin_client = IoTCClient(
    DEVICE_ID_AUSTIN,
    ID_SCOPE_AUSTIN,
    IOTCConnectType.IOTC_CONNECT_DEVICE_KEY,
    PRIMARY_KEY_AUSTIN,
    None,
    None
)

houston_client = IoTCClient(
    DEVICE_ID_HOUSTON,
    ID_SCOPE_HOUSTON,
    IOTCConnectType.IOTC_CONNECT_DEVICE_KEY,
    PRIMARY_KEY_HOUSTON,
    None,
    None
)

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
        await asyncio.sleep(3)
        
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
        await asyncio.sleep(3)
        
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
    await sendDallasTelemetry()
    await sendHoustonTelemetry()
    await sendAustinTelemetry()

asyncio.run(main())