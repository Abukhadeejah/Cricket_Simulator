class Player:
    def __init__(self, name, bowling, batting, fielding, running, keeping, experience):
        """
        Represents a player in a cricket team.
        Initialize a Player object with the provided attributes.
        
        Args:
            name (str): The name of the player.
            bowling (float): The bowling skill of the player.
            batting (float): The batting skill of the player.
            fielding (float): The fielding skill of the player.
            running (float): The running skill of the player.
            experience (float): The experience level of the player.
        """
        self.name = name 
        self.bowling = bowling 
        self.batting = batting 
        self.fielding = fielding 
        self.running = running
        self.keeping = keeping 
        self.experience = experience