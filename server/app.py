from flask import Flask
import time
import json
import threading
import paho.mqtt.client as mqtt
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "smarthome/#"

INFLUX_URL = "http://localhost:8086"
INFLUX_TOKEN = "e1JaXtwBCftbX9KtTXt3q0nIkFIINvCWEjk7JmuSw7211ZkqoEbBMRFwppr5TEIx3SsbxSoTxVmklFM_RSL-UA=="
INFLUX_ORG = "my-org"
INFLUX_BUCKET = "smarthome"

app = Flask(__name__)

influx = InfluxDBClient(
    url=INFLUX_URL,
    token=INFLUX_TOKEN,
    org=INFLUX_ORG
)
write_api = influx.write_api(write_options=SYNCHRONOUS)

def on_connect(client, userdata, flags, reasonCode, properties):
    if reasonCode == 0:
        print("[MQTT] Connected successfully")
        client.subscribe(MQTT_TOPIC)
    else:
        print(f"[MQTT] Failed to connect, code {reasonCode}")

def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode()
        print(f"[MQTT] Received {msg.topic} {payload}")
        data = json.loads(payload)

        measurement = f"sensor_{data['code']}"  # DUS1, DPIR1, DMS, DS1
        point = (
            Point(measurement)
            .tag("pi", data["pi"])
            .tag("device", data["device"])
            .tag("simulated", str(data["simulated"]))
            .field("value", data["value"])
            .time(data["timestamp"], write_precision="s")
        )
        write_api.write(bucket=INFLUX_BUCKET, record=point)

        print(f"[InfluxDB] Stored {data}")

    except Exception as e:
        print(f"Failed to process message: {e}")

def start_mqtt_thread():
    client = mqtt.Client(client_id="influx_subscriber", protocol=mqtt.MQTTv5)
    client.on_connect = on_connect
    client.on_message = on_message
    try:
        client.connect(MQTT_BROKER, MQTT_PORT)
        print("[MQTT] Attempting to connect to broker...")
    except Exception as e:
        print(f"Cannot connect to MQTT broker: {e}")
        return

    client.loop_forever()


@app.route("/")
def health():
    return "Health check passed"

if __name__ == "__main__":
    mqtt_thread = threading.Thread(target=start_mqtt_thread)
    mqtt_thread.daemon = True
    mqtt_thread.start()

    print("MQTT subscriber thread started")

    app.run(host="0.0.0.0", port=5000)