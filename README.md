<h2> Cloud-based IoT System with Virtual Sensors </h2>

This is a project for building a cloud-based IoT system that collects data from a set of virtual sensors using the MQTT protocol. The system will also have a simple web application to display the latest sensor data values and historical data values from all environmental stations.

<h3> Virtual Sensors </h3>

The system uses standalone computer programs to represent virtual environment IoT stations that periodically generate a set of random virtual sensor values for the following sensors:

1. Temperature (Range: -50 to 50 Celsius)
2. Humidity (Range: 0 to 100%)
3. CO2 sensor (Range: 300ppm to 2000ppm)
4. Rain height (Range: 0 to 50 mm/h)
5. Wind direction (Range: 0 to 360 degrees)
6. Wind intensity (Range: 0 to 100 m/s)

Each virtual environmental station has a unique ID to publish the random sensor data values on an MQTT channel. At least two virtual stations are running and publishing their values on the MQTT channel.

<h3> Cloud-based IoT Backend </h3>

The MQTT is controlled by a cloud-based backend. The following technologies can be used to implement the cloud-based backend:

AWS IoT
Azure IoT
Google IoT 
ThingsBoard

The dashboard displays the sensor data values received during the last five hours from all environmental stations of a specified sensor.

 <h3> Conclusion </h3>

This project demonstrates how to build a cloud-based IoT system using virtual sensors. It provides a good starting point for building more complex IoT systems that can be used for monitoring and controlling various applications.


<img width="468" alt="image" src="https://user-images.githubusercontent.com/47717859/231624756-5112ff18-bb3c-4991-b4a5-d46cbba0b0be.png">

<img width="468" alt="image" src="https://user-images.githubusercontent.com/47717859/231624644-9c1adfd9-5f7c-400e-8760-6ca5b1efcf72.png">
