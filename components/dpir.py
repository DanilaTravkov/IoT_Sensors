from services.mqqt_service import enqueue_measurement
from simulators.dpir import run_dpir_simulator
import threading
import time

# PIR motion sensor

def dpir_callback(motion_detected, code, settings):
    payload = {
        "pi": "PI1",
        "device": settings["name"],
        "code": code,
        "value": motion_detected,
        "simulated": settings["simulated"],
        "timestamp": int(time.time()),
        "topic": f"smarthome/pi1/{settings['topic']}"
    }
    enqueue_measurement(payload)
    # t = time.localtime()
    # print("="*30)
    # print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
    # print(f"Code: {code}")
    # print(f"Motion Detected: {'YES' if motion_detected else 'NO'}")

def run_dpir(settings, threads, stop_event):
    if settings['simulated']:
        ds_thread = threading.Thread(
            target=run_dpir_simulator,
            args=(3, lambda v, c: dpir_callback(v, c, settings), stop_event)
        )
        ds_thread.start()
        threads.append(ds_thread)
    else:
        # print("Real DPIR1 hardware not implemented yet")
        pass