# IoT-
Cloud-based IoT System with Virtual Sensors

This is a demo project that simulates a cloud-based IoT system that collects data from virtual sensors using MQTT protocol. The system consists of virtual environmental stations that periodically generate random sensor data values and publish them to an MQTT broker. The system also includes a simple web application that displays the latest sensor data values and the sensor data values received during the last five hours.

Requirements

To run this project, you need:
1. Python 3
2. The virtual environmental Station
3. Cloud-based IoT Backend

Installation

Clone this repository to your local machine.
Install the required dependencies as described above.
Start the MQTT broker. For this demo project, you can use the free broker provided by HiveMQ (https://www.hivemq.com/public-mqtt-broker/).
Start the virtual sensors. In the virtual_sensor.py file, replace the sensor_id variable with a unique ID for each virtual sensor, and update the broker_address variable if needed. Then run the script using python virtual_sensor.py.
Start the Flask web application. In the app.py file, update the broker_address variable if needed. Then run the script using python app.py.
Access the web application at http://localhost:5000

Usage

The web application displays two pages:

Latest Sensor Data
This page displays the latest sensor data values received from all the virtual sensors. The data is updated automatically every few seconds.

Sensor Data History
This page allows you to select a sensor and view the sensor data values received during the last five hours. The data is displayed in a line chart that is updated automatically every few seconds.
