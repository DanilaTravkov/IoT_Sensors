import time

class DoorLightSimulator:
    def __init__(self):
        self.state = False  # False = OFF, True = ON
    
    def turn_on(self):
        self.state = True
        print(f"[DL SIMULATOR] Door Light turned ON")
    
    def turn_off(self):
        self.state = False
        print(f"[DL SIMULATOR] Door Light turned OFF")
    
    def toggle(self):
        self.state = not self.state
        status = "ON" if self.state else "OFF"
        print(f"[DL SIMULATOR] Door Light toggled to {status}")
    
    def get_state(self):
        return "ON" if self.state else "OFF"