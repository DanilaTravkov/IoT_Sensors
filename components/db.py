from simulators.db import DoorBuzzerSimulator

# global instance for actuator
door_buzzer_instance = None

def initialize_db(settings):

    global door_buzzer_instance
    
    if settings['simulated']:
        print("Initializing DB simulator")
        door_buzzer_instance = DoorBuzzerSimulator()
        print("DB simulator initialized")
    else:
        # print("Real DB hardware not implemented yet")
        # door_buzzer_instance = None
        pass

def control_db(command, duration=1):
    global door_buzzer_instance
    
    if door_buzzer_instance is None:
        print("Door buzzer not initialized")
        return
    
    if command.lower() == "buzz":
        door_buzzer_instance.buzz(duration)
    elif command.lower() == "start":
        door_buzzer_instance.start_buzzing()
    elif command.lower() == "stop":
        door_buzzer_instance.stop_buzzing()
    elif command.lower() == "status":
        state = door_buzzer_instance.get_state()
        print(f"Door Buzzer Status: {state}")
    else:
        print("Invalid command. Use: buzz, start, stop, status")