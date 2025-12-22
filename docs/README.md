# Smart Home System - PI1 Documentation

## Project Overview

This project implements a smart home system for Raspberry Pi devices with various sensors and actuators. The system is designed to work with simulators for development and testing purposes.

## System Architecture

The system consists of:
- **Sensors**: Automatically generate data and output readings
- **Actuators**: Respond to commands and perform actions
- **Configuration**: JSON-based settings for easy device management
- **Simulators**: Software implementations of hardware devices

## Device Components

### Sensors (Automatic Output)

#### 1. DS1 - Door Sensor (Button)
- **Type**: Digital sensor
- **Function**: Detects door open/close state
- **Simulator Location**: `simulators/ds.py`
- **Component Location**: `components/ds.py`
- **Output Frequency**: Every 3 seconds
- **Trigger Rate**: 70% chance per cycle
- **Sample Output**:
```
==============================
Timestamp: 18:40:31
Code: DS1
Door State: OPEN
==============================
Timestamp: 18:40:34
Code: DS1
Door State: CLOSED
```

#### 2. DUS1 - Door Ultrasonic Sensor
- **Type**: Distance sensor
- **Function**: Measures distance to objects (5-200 cm range)
- **Simulator Location**: `simulators/dus.py`
- **Component Location**: `components/dus.py`
- **Output Frequency**: Every 2 seconds
- **Trigger Rate**: 100% (continuous)
- **Sample Output**:
```
==============================
Timestamp: 18:40:07
Code: DUS1
Distance: 132 cm
```

#### 3. DPIR1 - Door Motion Sensor (PIR)
- **Type**: Passive Infrared sensor
- **Function**: Detects motion/presence
- **Simulator Location**: `simulators/dpir.py`
- **Component Location**: `components/dpir.py`
- **Output Frequency**: Every 4 seconds
- **Trigger Rate**: 80% chance per cycle
- **Sample Output**:
```
==============================
Timestamp: 18:40:15
Code: DPIR1
Motion Detected: YES
==============================
Timestamp: 18:40:19
Code: DPIR1
Motion Detected: NO
```

#### 4. DMS - Door Membrane Switch
- **Type**: Digital button/switch
- **Function**: Detects button press events
- **Simulator Location**: `simulators/dms.py`
- **Component Location**: `components/dms.py`
- **Output Frequency**: Every 5 seconds
- **Trigger Rate**: 50% chance per cycle
- **Sample Output**:
```
==============================
Timestamp: 18:40:47
Code: DMS
Switch: PRESSED
==============================
Timestamp: 18:40:52
Code: DMS
Switch: RELEASED
```

### Actuators (Command-Driven)

#### 5. DL - Door Light (LED)
- **Type**: Light actuator
- **Function**: Controls door lighting
- **Simulator Location**: `simulators/dl.py`
- **Component Location**: `components/dl.py`
- **Commands**:
  - `control_dl("on")` - Turn light ON
  - `control_dl("off")` - Turn light OFF
  - `control_dl("toggle")` - Toggle current state
- **Sample Output**:
```
[DL SIMULATOR] Door Light turned ON
[DL SIMULATOR] Door Light turned OFF
[DL SIMULATOR] Door Light toggled to ON
```

#### 6. DB - Door Buzzer
- **Type**: Audio actuator
- **Function**: Provides audio alerts/notifications
- **Simulator Location**: `simulators/db.py`
- **Component Location**: `components/db.py`
- **Commands**:
  - `control_db("buzz", duration)` - Buzz for specified seconds
  - `control_db("start")` - Start continuous buzzing
  - `control_db("stop")` - Stop buzzing
- **Sample Output**:
```
[DB SIMULATOR] Buzzer ON for 2 seconds
[DB SIMULATOR] Buzzer OFF
[DB SIMULATOR] Buzzer started (continuous)
[DB SIMULATOR] Buzzer stopped
```

## Technical Details

### Threading Model
- Each sensor runs in its own thread
- Main thread coordinates startup/shutdown
- `stop_event` used for clean thread termination

### Simulator Behavior
- **Sensors**: Generate realistic data with random variations
- **Actuators**: Simulate hardware responses to commands
- All simulators respect the `stop_event` for clean shutdown

### Error Handling
- Graceful fallback when RPi.GPIO is not available
- Thread timeout protection during shutdown
- Configuration validation with error reporting
