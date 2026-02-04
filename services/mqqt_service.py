import json
import time
import threading

from queue import Queue, Empty
import paho.mqtt.client as mqtt

measurement_queue = Queue()

class MQTTPublisherDaemon(threading.Thread):
    def __init__(self, mqtt_cfg):
        super().__init__(daemon=True)
        self.cfg = mqtt_cfg
        self.client = mqtt.Client()
        self.client.connect(
            self.cfg["host"],
            self.cfg["port"],
            keepalive=60
        )

    def run(self):
        batch = []
        last_flush = time.time()

        while True:
            try:
                item = measurement_queue.get(timeout=1)
                batch.append(item)
            except Empty:
                pass

            now = time.time()
            if (
                len(batch) >= self.cfg["batch_size"] or
                now - last_flush >= self.cfg["batch_interval_sec"]
            ):
                if batch:
                    self.flush(batch)
                    batch.clear()
                    last_flush = now

    def flush(self, batch):
        for msg in batch:
            topic = msg["topic"]
            payload = json.dumps(msg)
            self.client.publish(topic, payload)
            print(f"[MQTT] Publish to {topic} : {payload}")

def enqueue_measurement(payload):
    measurement_queue.put(payload)

