# Smart Home System - Kontrolna Tačka 1

Implementacija pametne kuće sa simulatorima za Raspberry PI uređaje.

## Struktura Projekta

```
Project1/
├── main.py              # Glavna aplikacija
├── settings.py          # Učitavanje konfiguracije
├── console.py           # Konzolni interfejs za kontrolu
├── test.py             # Test skript
├── settings.json       # Konfiguracija uređaja
├── components/         # Komponente (senzori i aktuatori)
│   ├── ds.py           # Door Sensor (DS1)
│   ├── dus.py          # Door Ultrasonic Sensor (DUS1)
│   ├── dpir.py         # Door PIR Motion Sensor (DPIR1)
│   ├── dms.py          # Door Membrane Switch (DMS)
│   ├── dl.py           # Door Light (DL)
│   └── db.py           # Door Buzzer (DB)
└── simulators/         # Simulatori uređaja
    ├── ds.py           # Simulator door sensor-a
    ├── dus.py          # Simulator ultrazvučnog senzora
    ├── dpir.py         # Simulator PIR senzora
    ├── dms.py          # Simulator membrane switch-a
    ├── dl.py           # Simulator door light-a
    └── db.py           # Simulator door buzzer-a
```

## Uređaji (PI1)

### Senzori
- **DS1** - Door Sensor (Button) - Detektuje otvaranje/zatvaranje vrata
- **DUS1** - Door Ultrasonic Sensor - Meri udaljenost (5-200 cm)
- **DPIR1** - Door PIR Motion Sensor - Detektuje pokret
- **DMS** - Door Membrane Switch - Prekidač sa pritiskom

### Aktuatori
- **DL** - Door Light (LED) - Kontrola svetla na vratima
- **DB** - Door Buzzer - Kontrola zujalice

## Pokretanje Sistema

1. **Test sistema:**
```bash
python test.py
```

2. **Pokretanje glavne aplikacije:**
```bash
python main.py
```

## Konfiguracija

Edituj `settings.json` da bi uključio/isključio simulaciju za svaki uređaj:

```json
{
    "PI1": {
        "DS1": {
            "simulated": true,
            "name": "Door Sensor 1"
        }
    }
}
```

## Kontrola Aktuatora

Kada se sistem pokrene, dostupni su sledeći konzolni komandatori:

### Door Light (DL)
- `dl on` - Uključi svetlo
- `dl off` - Isključi svetlo
- `dl toggle` - Promeni stanje svetla
- `dl status` - Prikaži trenutno stanje

### Door Buzzer (DB)
- `db buzz [vreme]` - Aktiviraj zujalicu (default 1 sekunda)
- `db start` - Kontinuirano zvuk
- `db stop` - Zaustavi zvuk
- `db status` - Prikaži trenutno stanje

### Ostale komande
- `help` - Prikaži meni
- `quit` ili `exit` - Izlaz iz aplikacije

## Primer Pokretanja

```bash
C:\IoT\Project1> python main.py

============================================================
SMART HOME SYSTEM - PI1
============================================================
Settings loaded successfully

==================================================
CURRENT CONFIGURATION
==================================================

PI1:
  DS1: Door Sensor 1 - SIMULATED
  DL: Door Light - SIMULATED
  DUS1: Door Ultrasonic Sensor 1 - SIMULATED
  DB: Door Buzzer - SIMULATED
  DPIR1: Door Motion Sensor 1 - SIMULATED
  DMS: Door Membrane Switch - SIMULATED

Initializing actuators...
Initializing DL simulator
DL simulator initialized
Initializing DB simulator
DB simulator initialized

Starting sensors...
Starting DS1 simulator
DS1 simulator started
Starting DUS1 simulator
DUS1 simulator started
Starting DPIR1 simulator
DPIR1 simulator started
Starting DMS simulator
DMS simulator started

4 sensor threads started successfully!
System is running. Use console commands to control actuators.
Press Ctrl+C to stop the system.

Starting console control interface...
Type 'help' for available commands

SmartHome> help

========================================
ACTUATOR CONTROL MENU
========================================
Door Light (DL) Commands:
  dl on     - Turn door light ON
  dl off    - Turn door light OFF
  dl toggle - Toggle door light
  dl status - Show door light status

Door Buzzer (DB) Commands:
  db buzz [duration] - Buzz for duration (default 1 sec)
  db start  - Start continuous buzzing
  db stop   - Stop buzzing
  db status - Show buzzer status

Other Commands:
  help      - Show this menu
  quit/exit - Exit application
========================================

SmartHome> dl on
[DL SIMULATOR] Door Light turned ON

SmartHome> db buzz 2
[DB SIMULATOR] Buzzer ON for 2 seconds
[DB SIMULATOR] Buzzer OFF

SmartHome> quit
```

## Napomene

- Sistem koristi simulatore jer nema Raspberry Pi hardware
- Podaci sa senzora se prikazuju u realnom vremenu u konzoli
- Kontrola aktuatora se vrši kroz konzolni interfejs
- Za izlaz koristite Ctrl+C ili komandu `quit`
- Web kamera nije implementirana (nije potrebna za Kontrolnu Tačku 1)

## Proširenja

Za prelazak na pravi hardware:
1. Postaviti `"simulated": false` u settings.json
2. Implementirati pravo čitanje senzora u components/ fajlovima
3. Dodati GPIO pin konfiguracije u settings.json
