# Cake Vending App for Demo

The goal of this project is to create N cake vending machines. These are simulated devices that have the following parameters:

* CakeInventoryFilled - Telemetry
* CakeInventoryPurchased - Telemetry
* Fridge-Temperature - Telemetry
* Location-Latitude - Telemetry
* Location-Longitude - Telemetry

Our goal is to set up at least 3 machines for the demonstration. We'd like to spread them around the city. We'll use the Lat-Long values to place these items in an area. This will stay rather constant, unless we want to show a machine moving (Mobile Vending?).

Dallas, Austin, and Houston

Dallas = 32.78306, -96.80667
Austin = 30.26715, -97.74306
Houston = 29.76328, -95.36327

CakeInventoryFilled - Each machine holds 250 Cupcakes. When it's filled, the operator is told to fill it all the way. So this event replenishes the machine to a full 250 cupcakes.

CakeInventoryPurchased - Cakes are only purchased one at a time and will deplete the machines inventory. We might want to create a current inventory device parameter that we can query.

Fridge-Temperature - The ideal temperature for the cupcakes is between 45-55 degrees F. We want to add alerts if the temperature varies above 55 degrees.

Here are the various things I think we need to make this work:

* Generic device with parameters that we can pass values to
* Location specific values for machine usage (One device should perform best)
* We should simulate refills - refills are done once a day when needed