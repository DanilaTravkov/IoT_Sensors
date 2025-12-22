from simulators.dus import run_dus_simulator
import threading
import time

# Ultrasonic sensor

def dus_callback(distance, code):
    t = time.localtime()
    print("="*30)
    print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
    print(f"Code: {code}")
    print(f"Distance: {distance} cm")

def run_dus(settings, threads, stop_event):
    if settings['simulated']:
        print("Starting DUS1 simulator")
        dus_thread = threading.Thread(target=run_dus_simulator, args=(2, dus_callback, stop_event))
        dus_thread.start()
        threads.append(dus_thread)
        print("DUS1 simulator started")
    else:
        # print("Real DUS1 hardware not implemented yet")
        pass