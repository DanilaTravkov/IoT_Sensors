from services.mqqt_service import enqueue_measurement
from simulators.dus import run_dus_simulator
import threading
import time

# Ultrasonic sensor

def dus_callback(distance, code, settings):
    # t = time.localtime()
    # print("="*30)
    # print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
    # print(f"Code: {code}")
    # print(f"Distance: {distance} cm")
    payload = {
        "pi": "PI1",
        "device": settings["name"],
        "code": code,
        "value": distance,
        "simulated": settings["simulated"],
        "timestamp": int(time.time()),
        "topic": f"smarthome/pi1/{settings['topic']}"
    }
    enqueue_measurement(payload)

def run_dus(settings, threads, stop_event):
    if settings['simulated']:
        ds_thread = threading.Thread(
            target=run_dus_simulator,
            args=(3, lambda v, c: dus_callback(v, c, settings), stop_event)
        )
        ds_thread.start()
        threads.append(ds_thread)
    else:
        # print("DUS1 hardware not implemented yet")
        pass