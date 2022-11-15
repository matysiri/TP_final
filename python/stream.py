import mysql.connector
import datetime
import random
import time

NORMAL_PARAMS = (10, 20, 2.0)
ANOMALY_PARAMS = (100, 120, 30.0)

def get_sensor_measurement(low_val, high_val, noise_std_dev):
    value = float(random.randint(low_val, high_val))
    value += random.normalvariate(0, noise_std_dev)
    return value

def get_sensor_record(name, anomaly_chance):
    ts = datetime.datetime.utcnow().isoformat(' ')
    is_anomaly = random.random() < anomaly_chance
    params = ANOMALY_PARAMS if is_anomaly else NORMAL_PARAMS
    value = get_sensor_measurement(*params)
    
    response = {
        "event_timestamp": ts,
        "sensor_name": name,
        "sensor_value": value,
        "is_anomaly": is_anomaly
    }

    return response

name     = 'tp_linux'
chance   = 0.09
wait     = 500
wait_std = 100
contador = 0

connection = mysql.connector.connect(
    user='root', password='root', host='mysql', port='3306', database='db'
)

print('Connection succesfull')

cursor = connection.cursor()

query = """
INSERT INTO stream_table (event_timestamp,sensor_name,sensor_value,is_anomaly) VALUES (%s,%s,%s,%s)
"""

while contador<1001:
    data = get_sensor_record(name, chance)
    wait_ms = abs(random.normalvariate(wait, wait_std))
    time.sleep(wait_ms / 1000)
    print(data)
    values = (data['event_timestamp'],data['sensor_name'],data['sensor_value'],data['is_anomaly'])
    cursor.execute(query,values)
    connection.commit()
    print(f'Record {contador} inserted')
    contador += 1


