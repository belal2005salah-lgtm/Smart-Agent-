class SmartThermostat :                            
    def __init__( self) :    
        # Initial internal state
        self.heating_on = False
        self.cooling_on = False
        self.fan_mode=  "Auto" # "Auto" or "Quiet"

    def perceive_and_act ( self, current_temp, target_temp , is_occupied ,time_of_day) :
        """
        Perceive inputs from the environment and decide on an action using IF-THEN rules.
        """
        print (f"\n New Percept ")
        print(f"Current Temp:{current_temp}°C, Target Temp:{target_temp}°C")
        print  (f"Occupied: {is_occupied}, Time: {time_of_day}")
        
        # Reset fan mode to Auto at each percept unless a rule overrides it
        self.fan_mode = "Auto"
        action_taken = ""

        # RULE 1: IF not occupied AND current < 10 THEN turn heating ON (freeze prevention)
        if not is_occupied and current_temp < 10   :       
            self.heating_on =True
            self.cooling_on =False
            action_taken=    "Heating ON (Freeze Prevention)"
            
        # RULE 2: IF not occupied AND current >= 10 THEN turn system OFF (energy saving)
        elif not is_occupied and current_temp >= 10:     
            self.heating_on=False
            self.cooling_on =   False
            action_taken    ="System OFF (Energy Saving Mode)"
            
        # RULE 3: IF occupied AND current < target THEN turn heating ON
        elif is_occupied and current_temp < target_temp:
            self.heating_on= True
            self.cooling_on = False
            action_taken  = "Heating ON"
            
        # RULE 4: IF occupied AND current > target THEN turn cooling ON
        elif is_occupied and current_temp > target_temp:
            self.heating_on  = False
            self.cooling_on =True
            action_taken   = "Cooling ON"
            
        # RULE 5: IF current == target THEN turn system OFF
        elif current_temp == target_temp:
            self.heating_on =False
            self.cooling_on = False
            action_taken =  "System OFF (Target Reached)"

        # RULE 6: IF night time AND system is running THEN use quiet fan mode
        if time_of_day == "Night" and (self.heating_on or self.cooling_on):
            self.fan_mode = "Quiet"
            action_taken += ", Fan Mode: Quiet"

        # Output the decision clearly
        print(f"-> DECISION: {action_taken}")

# Test the agent with different scenarios
if __name__ == "__main__":
    agent = SmartThermostat()

    # Scenario 1: Occupied, cold
    agent.perceive_and_act(current_temp=18, target_temp=22, is_occupied=True, time_of_day="Day")
    
    # Scenario 2: Occupied, hot, night time
    agent.perceive_and_act(current_temp=26, target_temp=22, is_occupied=True, time_of_day="Night")
    
    # Scenario 3: Not occupied, very cold (freeze risk)
    agent.perceive_and_act(current_temp=5, target_temp=22, is_occupied=False, time_of_day="Night")
    
    # Scenario 4: Not occupied, normal temp
    agent.perceive_and_act(current_temp=15, target_temp=22, is_occupied=False, time_of_day="Day")
    
    # Scenario 5: Occupied, target reached
    agent.perceive_and_act(current_temp=22, target_temp=22, is_occupied=True, time_of_day="Day")
