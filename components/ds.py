from simulators.ds import run_ds_simulator
import threading
import time

# Door sensor

def ds_callback(state, code):
    t = time.localtime()
    print("="*30)
    print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
    print(f"Code: {code}")
    print(f"Door State: {state}")

def run_ds(settings, threads, stop_event):
    if settings['simulated']:
        print("Starting DS1 simulator")
        ds_thread = threading.Thread(target=run_ds_simulator, args=(3, ds_callback, stop_event))
        ds_thread.start()
        threads.append(ds_thread)
        print("DS1 simulator started")
    else:
        # print("Real DS1 hardware not implemented yet")
        pass