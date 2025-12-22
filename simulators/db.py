import time

class DoorBuzzerSimulator:
    def __init__(self):
        self.is_buzzing = False
    
    def buzz(self, duration=1):
        self.is_buzzing = True
        print(f"[DB SIMULATOR] Buzzer ON for {duration} seconds")
        time.sleep(duration)
        self.is_buzzing = False
        print(f"[DB SIMULATOR] Buzzer OFF")
    
    def start_buzzing(self):
        self.is_buzzing = True
        print(f"[DB SIMULATOR] Buzzer started (continuous)")
    
    def stop_buzzing(self):
        self.is_buzzing = False
        print(f"[DB SIMULATOR] Buzzer stopped")
    
    def get_state(self):
        return "BUZZING" if self.is_buzzing else "SILENT"