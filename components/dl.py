from simulators.dl import DoorLightSimulator

# Global instance for different envs (real PI or simulator)
door_light_instance = None

def initialize_dl(settings):
    global door_light_instance
    
    if settings['simulated']:
        print("Initializing DL simulator")
        door_light_instance = DoorLightSimulator()
        print("DL simulator initialized")
    else:
        # print("Real DL hardware not implemented yet")
        # door_light_instance = None
        pass

def control_dl(command):
    global door_light_instance
    
    if door_light_instance is None:
        print("Door light not initialized")
        return
    
    if command.lower() == "on":
        door_light_instance.turn_on()
    elif command.lower() == "off":
        door_light_instance.turn_off()
    elif command.lower() == "toggle":
        door_light_instance.toggle()
    elif command.lower() == "status":
        state = door_light_instance.get_state()
        print(f"Door Light Status: {state}")
    else:
        print("Invalid command. Use: on, off, toggle, status")