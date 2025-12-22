from simulators.dms import run_dms_simulator
import threading
import time

# door membrane

def dms_callback(state, code):
    t = time.localtime()
    print("="*30)
    print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
    print(f"Code: {code}")
    print(f"Switch: {state}")

def run_dms(settings, threads, stop_event):
    if settings['simulated']:
        print("Starting DMS simulator")
        dms_thread = threading.Thread(target=run_dms_simulator, args=(5, dms_callback, stop_event))
        dms_thread.start()
        threads.append(dms_thread)
        print("DMS simulator started")
    else:
        # print("Real DMS hardware not implemented yet")
        pass