# Smart Systems Assignment 1 - Intelligent Agent Design

## Overview
**Agent Name:** Smart Thermostat
**Target Scenario:** Smart Thermostat — reads temperature and controls heating/cooling
**Agent Type:** Simple Reflex Agent

A Simple Reflex Agent selects actions based wholly on the current percept, ignoring the rest of the percept history. This makes it perfect for a thermostat, which merely needs to react to current environmental readings (time of day, current temperature, and occupancy) to make decisions instantly using condition-action (IF-THEN) rules.

## Percepts (Inputs)
The agent perceives the following data points from its environment:
- `current_temperature`: The real-time temperature of the room (in °C).
- `target_temperature`: The desired temperature set by the user (in °C).
- `is_occupied`: Boolean indicating if the user is currently present in the home.
- `time_of_day`: The current time period (e.g., "Day" or "Night").

## Actions (Outputs)
Based on the percepts, the agent performs the following actions:
- `Heating ON`: Activates the heater.
- `Cooling ON`: Activates the AC.
- `System OFF`: Deactivates all heating and cooling.
- `Fan Mode`: Adjusts between "Auto" and "Quiet" (e.g., during Night).

## Decision Rules
The intelligent agent employs the following 6 IF-THEN rules to guide its actions:
1. **IF** occupied **AND** current < target **THEN** turn Heating ON.
2. **IF** occupied **AND** current > target **THEN** turn Cooling ON.
3. **IF** not occupied **AND** current < 10°C **THEN** turn Heating ON (Freeze Prevention).
4. **IF** not occupied **AND** current >= 10°C **THEN** turn System OFF (Energy Saving Mode).
5. **IF** current == target **THEN** turn System OFF (Target Reached).
6. **IF** time of day is Night **AND** system is ON **THEN** enable Quiet Fan Mode.

## Sample Output
Below constitutes the terminal output showcasing five corresponding test scenarios that validate all decision paths:

```text
--- New Percept ---
Current Temp: 18°C, Target Temp: 22°C
Occupied: True, Time: Day
-> DECISION: Heating ON

--- New Percept ---
Current Temp: 26°C, Target Temp: 22°C
Occupied: True, Time: Night
-> DECISION: Cooling ON, Fan Mode: Quiet

--- New Percept ---
Current Temp: 5°C, Target Temp: 22°C
Occupied: False, Time: Night
-> DECISION: Heating ON (Freeze Prevention), Fan Mode: Quiet

--- New Percept ---
Current Temp: 15°C, Target Temp: 22°C
Occupied: False, Time: Day
-> DECISION: System OFF (Energy Saving Mode)

--- New Percept ---
Current Temp: 22°C, Target Temp: 22°C
Occupied: True, Time: Day
-> DECISION: System OFF (Target Reached)
```
