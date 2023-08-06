import random 
class Field:
    def __init__(self, size, fan_ratio, pitch_conditions, home_advantage):
        """
        Initialize a Field object with the provided attributes.
        
        Args:
            size (str): The size of the field.
            fan_ratio (float): The fan ratio of the field.
            pitch_conditions (str): The pitch conditions of the field.
            home_advantage (float): The home advantage of the field.
        """
        self.size = size
        self.fan_ratio = fan_ratio
        self.pitch_conditions = pitch_conditions
        self.home_advantage = home_advantage