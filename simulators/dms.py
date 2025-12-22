import time
import random

def run_dms_simulator(delay, callback, stop_event):
    while not stop_event.is_set():
        # Simulate random switch press
        if random.randint(1, 10) <= 5:  # 50%
            callback("PRESSED", "DMS")
        
        time.sleep(delay)