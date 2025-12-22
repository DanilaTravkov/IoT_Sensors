import time
import random

# door sensor (button)

def run_ds_simulator(delay, callback, stop_event):
    door_open = False
    
    while not stop_event.is_set():
        # Random chance of door state change
        if random.randint(1, 10) <= 7:  # 70% chance every cycle
            door_open = not door_open
            state = "OPEN" if door_open else "CLOSED"
            callback(state, "DS1")
        
        time.sleep(delay)