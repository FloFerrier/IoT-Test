import influxdb_client
import random
import time
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client.domain.write_precision import WritePrecision

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

for index in range(0, 500):
    data = {
        "timestamp": int(time.time()),
        "name": "home",
        "room": "living",
        "type": "temperature",
        "value": random.uniform(-25.0, 40.0),
        "unit": "degree celsius"
    }
    data_formatting = "[{index}] timestamp: {timestamp} - {type}: {value} {unit}".format(index=index, timestamp=data["timestamp"], type=data["type"], value=data["value"], unit=data["unit"])
    print(data_formatting)

    record = influxdb_client.Point.from_dict(data,
        write_precision=WritePrecision.S,
        record_measurement_key="name",
        record_time_key="timestamp",
        record_tag_keys=["room", "type", "unit"],
        record_field_keys=["value"])
    write_api.write(bucket=bucket, org=org, record=record)
    time.sleep(1.0)
