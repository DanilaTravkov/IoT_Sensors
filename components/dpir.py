from simulators.dpir import run_dpir_simulator
import threading
import time

# PIR motion sensor

def dpir_callback(motion_detected, code):
    t = time.localtime()
    print("="*30)
    print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
    print(f"Code: {code}")
    print(f"Motion Detected: {'YES' if motion_detected else 'NO'}")

def run_dpir(settings, threads, stop_event):
    if settings['simulated']:
        print("Starting DPIR1 simulator")
        dpir_thread = threading.Thread(target=run_dpir_simulator, args=(4, dpir_callback, stop_event))
        dpir_thread.start()
        threads.append(dpir_thread)
        print("DPIR1 simulator started")
    else:
        # print("Real DPIR1 hardware not implemented yet")
        pass