class Commentator:
    def __init__(self, umpire):
        """
        Initialize a Commentator object with the provided attributes.
        
        Args:
            umpire (Umpire): The Umpire object providing match information.
        """
        self.umpire = umpire

    def describe_ball(self, batsman, bowler):
        """
        Generate a description of the ball played by the batsman.
        
        Args:
            batsman (Player): The Player object representing the batsman.
            bowler (Player): The Player object representing the bowler.
        
        Returns:
            str: The description of the ball played by the batsman.
        """
        outcome = self.umpire.predict_outcome(batsman, bowler)
        print("Outcome: ", outcome)
        if outcome == "OUT":
            description = f"{batsman.name} is OUT!!!"
        else:
            description = f"{batsman.name} plays the shot."

        return description

    def describe_game(self, captain1, captain2, country1, country2, over):
        """
        Provide a description of the cricket match.
        
        Args:
            captain1 (str): The name of the captain of the first team.
            captain2 (str): The name of the captain of the second team.
            country1 (str): The name of the first team.
            country2 (str): The name of the second team.
            over (int): The total number of overs in the match.
        """
        print("\n--------- Game Information ---------\n")
        print(f"{country1} Vs {country2}")
        print(f"Captain 1 : {captain1}, Captain 2 : {captain2}")
        print(f"Over : {over}")
        print("\n---------------------------------------------\n")

    def describe_start(self, team):
        """
        Provide a description of the start of an innings.
        
        Args:
            team (str): The name of the team currently batting.
        """
        print("\n------------- GAME STARTED ------------------\n")
        print(f"Team {team} playing: ")
        # print(f"Batsman on strike: {batsman}")
        # print(f"Bowler bowling the first over: {bowler}")
        
    
    def describe_end(self):
        """
        Provide a description of the end of an innings.
        """
        print(f"\n\nFinal Run: {self.umpire.scores} Wicket: {self.umpire.wickets} Overs: {self.umpire.overs}")
        print("\n---------------------------------------------\n")

    
    def current_info(self, ball_count):
        """
        Provide the current match information.
        
        Args:
            ball_count (int): The count of balls played in the current over.
        """
        print(f"Balls: {ball_count} Over: {self.umpire.overs} Run: {self.umpire.scores}  Wicket: {self.umpire.wickets}")

    def describe_final_result(self, name, scores):
        """
        Provide a description of the final result of the match.
        
        Args:
            name (str): The name of the winning team.
            scores (int): The```
            score achieved by the winning team.
        """
        print("--------------- Winner -----------------------")
        print(f"TEAM : {name} WON BY SCORE: {scores}")
        print("\n---------------------------------------------\n")