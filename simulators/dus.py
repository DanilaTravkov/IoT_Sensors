import time
import random

# Distance sensor simulation

def run_dus_simulator(delay, callback, stop_event):
    distance = 50  # Initial distance
    
    while not stop_event.is_set():
        if random.randint(1, 10) <= 3:  # 30% chance of large movement
            distance = random.randint(5, 200)  # simulate person walking by
        else:
            # small variations due to noise
            distance += random.randint(-2, 2)
            distance = max(5, min(200, distance))
        
        callback(distance, "DUS1")
        time.sleep(delay)