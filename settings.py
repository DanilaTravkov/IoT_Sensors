import json
import os

def load_settings():
    settings_file = "settings.json"
    
    if not os.path.exists(settings_file):
        print(f"Error: {settings_file} not found!")
        return None
    
    try:
        with open(settings_file, 'r') as f:
            settings = json.load(f)
        print("Settings loaded successfully")
        return settings
    except json.JSONDecodeError as e:
        print(f"Error parsing {settings_file}: {e}")
        return None
    except Exception as e:
        print(f"Error loading {settings_file}: {e}")
        return None

def print_settings(settings):
    print("\n" + "="*50)
    print("Current config")
    print("="*50)
    
    for pi_name, devices in settings.items():
        print(f"\n{pi_name}:")
        for device_code, device_config in devices.items():
            status = "SIMULATED" if device_config['simulated'] else "REAL"
            print(f"  {device_code}: {device_config['name']} - {status}")
