import random

class Team:

    def __init__(self, name, players):
        """
        Initialize a Team object with the provided attributes.
        
        Args:
            name (str): The name of the team.
            players (list): The list of Player objects representing the team's players.
        """
        self.name = name 
        self.players = players 
        self.captain = None 
        self.batting_order = players.copy()
        self.bowlers = []

    def select_captain(self, captain):
        """
        Select the captain for the team.
        
        Args:
            captain (Player): The Player object representing the captain of the team.
        """
        self.captain = captain

    def sending_next_player(self):
        """
        Send the next player from the batting order.
        
        Returns:
            Player or None: The next Player object from the batting order, or None if the batting order is empty.
        """
        if len(self.batting_order)>0:
            return self.batting_order.pop(0)
        return None 
    
    def choose_bowler(self):
        """
        Choose a bowler randomly from the team's bowlers.
        
        Returns:
            Player: The Player object representing the chosen bowler.
        """
        return random.choice(self.bowlers)