import os
import random
import time

time_duration = 5 * 60 * 60  

start_time = time.time()


while (time.time() - start_time) < time_duration:
    
    temperature = random.randint(-50, 50)
    humidity = random.randint(0, 100)
    co2sensor = random.randint(300, 2000)
    rain_height = random.randint(0, 50)
    wind_direction = random.randint(0, 360)
    wind_intensity = random.randint(0, 100)

    temp1 = f'mosquitto_pub -d -q 1 -h "demo.thingsboard.io" -p "1883" -t "v1/devices/me/telemetry" -u "asdfghjkl1234" -m {{"temperature":{temperature}}}'
    os.system(temp1)

    humidity1 = f'mosquitto_pub -d -q 1 -h "demo.thingsboard.io" -p "1883" -t "v1/devices/me/telemetry" -u "8k6NOnyd6EfX1t8pnNSL" -m {{"humidity":{humidity}}}'
    os.system(humidity1)

    co2_1 = f'mosquitto_pub -d -q 1 -h "demo.thingsboard.io" -p "1883" -t "v1/devices/me/telemetry" -u "e7JY0zKmF4t7Z3fdjGsr" -m {{"co2sensor":{co2sensor}}}'
    os.system(co2_1)

    rain_sensor = f'mosquitto_pub -d -q 1 -h "demo.thingsboard.io" -p "1883" -t "v1/devices/me/telemetry" -u "CtRD1cLM6QAFhkXQKkQt" -m {{"rain_height":{rain_height}}}'
    os.system(rain_sensor)

    wind_direction = f'mosquitto_pub -d -q 1 -h "demo.thingsboard.io" -p "1883" -t "v1/devices/me/telemetry" -u "v7bKqo3SV1aeiQviBFhj" -m {{"wind_direction":{wind_direction}}}'
    os.system(wind_direction)

    wind_intensity = f'mosquitto_pub -d -q 1 -h "demo.thingsboard.io" -p "1883" -t "v1/devices/me/telemetry" -u "fPpQ29xwLEFui1KgtdAf" -m {{"wind_intensity":{wind_intensity}}}'
    os.system(wind_intensity)

    temperature = random.randint(-50, 50)
    humidity = random.randint(0, 100)
    co2sensor = random.randint(300, 2000)
    rain_height = random.randint(0, 50)
    wind_direction = random.randint(0, 360)
    wind_intensity = random.randint(0, 100)

    temp1 = f'mosquitto_pub -d -q 1 -h "demo.thingsboard.io" -p "1883" -t "v1/devices/me/telemetry" -u "53OFEYSpF78uOaUAm5DH" -m {{"temperature2":{temperature}}}'
    os.system(temp1)

    humidity1 = f'mosquitto_pub -d -q 1 -h "demo.thingsboard.io" -p "1883" -t "v1/devices/me/telemetry" -u "Hy5W7ZogqxscjEwKEVwJ" -m {{"humidity2":{humidity}}}'
    os.system(humidity1)

    co2_1 = f'mosquitto_pub -d -q 1 -h "demo.thingsboard.io" -p "1883" -t "v1/devices/me/telemetry" -u "zaUsyfFIYeMKTY0iGc5k" -m {{"co2sensor2":{co2sensor}}}'
    os.system(co2_1)

    rain_sensor = f'mosquitto_pub -d -q 1 -h "demo.thingsboard.io" -p "1883" -t "v1/devices/me/telemetry" -u "JfqYRrya0RHwgefghUjk" -m {{"rain_height2":{rain_height}}}'
    os.system(rain_sensor)

    wind_direction = f'mosquitto_pub -d -q 1 -h "demo.thingsboard.io" -p "1883" -t "v1/devices/me/telemetry" -u "rwNVFVdfFUJ8AM31c8xi" -m {{"wind_direction2":{wind_direction}}}'
    os.system(wind_direction)

    wind_intensity = f'mosquitto_pub -d -q 1 -h "demo.thingsboard.io" -p "1883" -t "v1/devices/me/telemetry" -u "QoBc8rSaGU8FB7fggzPV" -m {{"wind_intensity2":{wind_intensity}}}'
    os.system(wind_intensity)

    time.sleep(10)                
