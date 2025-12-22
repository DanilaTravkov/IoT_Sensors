import time
import random

# PIR motion sensor

def run_dpir_simulator(delay, callback, stop_event):
    while not stop_event.is_set():
        # Random chance of motion detection
        if random.randint(1, 10) <= 8:  # 80% chance of detecting motion
            motion_detected = True
            callback(motion_detected, "DPIR1")
        
        time.sleep(delay)