import random
class Umpire:
    def __init__(self, field):
        """
        Initialize an Umpire object with the provided attributes.
        
        Args:
            field (Field): The Field object representing the field conditions.
        """
        self.field = field
        self.scores = 0
        self.wickets = 0
        self.overs = 0

    def update_score(self, runs):
        """
        Update the score based on the runs scored.
        
        Args:
            runs (int): The runs scored in the ball.
        """
        self.scores += runs

    def update_wickets(self):
        """
        Update the wickets count.
        """
        self.wickets += 1

    def update_overs(self):
        """
        Update the overs count.
        """
        self.overs += 1

    def predict_outcome(self, batsman, bowler):
        """
        Predict the outcome of a ball based on batsman and bowler stats.
        
        Args:
            batsman (Player): The Player object representing the batsman.
            bowler (Player): The Player object representing the bowler.
        
        Returns:
            str: The outcome of the ball (either "OUT" or "NOT OUT").
        """
        batting_prob = batsman.batting * self.field.pitch_conditions * random.random()
        bowling_prob = bowler.bowling * self.field.pitch_conditions * random.random()
        if batting_prob > bowling_prob:
            return "NOT OUT"
        return "OUT"