from services.mqqt_service import enqueue_measurement
from simulators.dms import run_dms_simulator
import threading
import time

# door membrane

def dms_callback(state, code, settings):
    payload = {
        "pi": "PI1",
        "device": settings["name"],
        "code": code,
        "value": state,
        "simulated": settings["simulated"],
        "timestamp": int(time.time()),
        "topic": f"smarthome/pi1/{settings['topic']}"
    }
    enqueue_measurement(payload)
    # t = time.localtime()
    # print("="*30)
    # print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
    # print(f"Code: {code}")
    # print(f"Switch: {state}")

def run_dms(settings, threads, stop_event):
    if settings['simulated']:
        ds_thread = threading.Thread(
            target=run_dms_simulator,
            args=(3, lambda v, c: dms_callback(v, c, settings), stop_event)
        )
        ds_thread.start()
        threads.append(ds_thread)
    else:
        # print("Real DMS hardware not implemented yet")
        pass