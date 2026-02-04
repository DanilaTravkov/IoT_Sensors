import threading
import time
from settings import load_settings, print_settings

from components.ds import run_ds
from components.dus import run_dus
from components.dpir import run_dpir
from components.dms import run_dms
from components.dl import initialize_dl, control_dl
from components.db import initialize_db, control_db

from services.mqqt_service import MQTTPublisherDaemon

# try:
#     import RPi.GPIO as GPIO
#     GPIO.setmode(GPIO.BCM)
#     print("GPIO initialized for Raspberry Pi")
# except ImportError:
#     print("RPi.GPIO not available - running in simulation mode")
# except Exception as e:
#     print(f"GPIO initialization failed: {e}")

def start_sensors(pi_settings, threads, stop_event):
    
    # Door Sensor (DS1)
    if 'DS1' in pi_settings:
        run_ds(pi_settings['DS1'], threads, stop_event)
    
    # Door Ultrasonic Sensor (DUS1)
    if 'DUS1' in pi_settings:
        run_dus(pi_settings['DUS1'], threads, stop_event)
    
    # Door PIR Motion Sensor (DPIR1)
    if 'DPIR1' in pi_settings:
        run_dpir(pi_settings['DPIR1'], threads, stop_event)
    
    # Door Membrane Switch (DMS)
    if 'DMS' in pi_settings:
        run_dms(pi_settings['DMS'], threads, stop_event)

def initialize_actuators(pi_settings):
    
    # Door Light (DL)
    if 'DL' in pi_settings:
        initialize_dl(pi_settings['DL'])
    
    # Door Buzzer (DB)
    if 'DB' in pi_settings:
        initialize_db(pi_settings['DB'])

def main():
    print('='*60)
    
    # Load settings
    settings = load_settings()
    if settings is None:
        print("Failed to load settings. Exiting.")
        return
    
    print_settings(settings)

    device_cfg = settings["device"]
    mqtt_cfg = device_cfg["mqtt"]
    
    print("\nStarting MQTT batch daemon")
    mqtt_daemon = MQTTPublisherDaemon(mqtt_cfg)
    mqtt_daemon.start()

    pi1_settings = settings.get('PI1', {})
    if not pi1_settings:
        print("No PI1 configuration found in settings!")
        return
    
    threads = []
    stop_event = threading.Event()
    
    try:
        print("\nInitializing actuators")
        initialize_actuators(pi1_settings)
        
        print("\nStarting sensors")
        start_sensors(pi1_settings, threads, stop_event)
        print(f"\n{len(threads)} sensor threads started successfully")
        print("\nTesting actuators")
        print("Testing Door Light")
        control_dl("on")
        time.sleep(1)
        control_dl("off")
        time.sleep(1)
        control_dl("toggle")
        time.sleep(1)
        print("Testing Door Buzzer")
        control_db("buzz", 2)
        time.sleep(3)
        control_db("start")
        time.sleep(2)
        control_db("stop")
        print("Actuator tests completed.\n")
        
        # Keep main thread alive
        while not stop_event.is_set():
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n\nShutting down")
    except Exception as e:
        print(f"\nError: {e}")
    finally:
        # Stop all threads
        print("Stopping all threads")
        stop_event.set()
        
        for thread in threads:
            thread.join(timeout=2)
            
if __name__ == "__main__":
    main()