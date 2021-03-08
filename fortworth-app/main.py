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

def refillInventory():
    startingInvetory = 0
    return 250

def decrimentInventory(purchasedAmount):
    if (startingInvetory > 0):
        return startingInvetory - purchasedAmount
    else:
        return 0

# Load the device connection values
DEVICE_ID_FORT_WORTH = os.environ.get("DEVICE_ID_FORT_WORTH")
ID_SCOPE_FORT_WORTH = os.environ.get("ID_SCOPE_FORT_WORTH")
PRIMARY_KEY_FORT_WORTH = os.environ.get("PRIMARY_KEY_FORT_WORTH")
startingInvetory = 250

# Create our three different clients
fortworth_client = IoTCClient(
    DEVICE_ID_FORT_WORTH,
    ID_SCOPE_FORT_WORTH,
    IOTCConnectType.IOTC_CONNECT_DEVICE_KEY,
    PRIMARY_KEY_FORT_WORTH,
    None,
    None)

async def on_props(property_name, property_value, component_name):
    print("Received {}:{}".format(property_name, property_value))
    refillInventory()
    return True

fortworth_client.on(IOTCEvents.IOTC_PROPERTIES, on_props)

async def sendFortWorthTelemetry():
    await fortworth_client.connect()
    while fortworth_client.is_connected():
        print("client connected {}".format(fortworth_client._device_client.connected))
        decrimentInventory(getPurchaseAmount())
        await fortworth_client.send_telemetry(
            {
                "CakeInventoryFilled": 0,
                "CakeInventoryPurchased": getPurchaseAmount(),
                "FridgeTemperature": getTemperature(),
                "LocationLatitude": 32.72541,
                "LocationLongitude": -97.32085
            }
        )
        await asyncio.sleep(900)

async def main():
    await sendFortWorthTelemetry()

asyncio.run(main())