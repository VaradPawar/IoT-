Cloud-based IoT System with Virtual Sensors

This is a project for building a cloud-based IoT system that collects data from a set of virtual sensors using the MQTT protocol. The system will also have a simple web application to display the latest sensor data values and historical data values from all environmental stations.

Virtual Sensors

The system uses standalone computer programs to represent virtual environment IoT stations that periodically generate a set of random virtual sensor values for the following sensors:

Temperature (Range: -50 to 50 Celsius)
Humidity (Range: 0 to 100%)
CO2 sensor (Range: 300ppm to 2000ppm)
Rain height (Range: 0 to 50 mm/h)
Wind direction (Range: 0 to 360 degrees)
Wind intensity (Range: 0 to 100 m/s)
Each virtual environmental station has a unique ID to publish the random sensor data values on an MQTT channel. At least two virtual stations are running and publishing their values on the MQTT channel.

Cloud-based IoT Backend

The MQTT is controlled by a cloud-based backend. The following technologies can be used to implement the cloud-based backend:

AWS IoT
Azure IoT
Google IoT ThingsBoard
Web Application

The system has a simple web application that displays the latest sensor data values and historical data values from all environmental stations. The web application will have the following functionalities:

Display the latest sensor data values received from all the sensors of a specified environmental station.
Display the sensor data values received during the last five hours from all environmental stations of a specified sensor.

Conclusion

This project demonstrates how to build a cloud-based IoT system using virtual sensors and a web application to display the collected data. It provides a good starting point for building more complex IoT systems that can be used for monitoring and controlling various applications.
