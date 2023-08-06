import random
from umpire import Umpire
from commentator import Commentator

class Match:
    def __init__(self, team1, team2, field, total_overs):
        """
        Represents a cricket match between two teams.
        
        Args:
            team1 (Team): The Team object representing the first team.
            team2 (Team): The Team object representing the second team.
            field (Field): The Field object representing the field conditions.
            total_overs (int): The total number of overs in the match.
        """
        self.team1 = team1
        self.team2 = team2
        self.field = field
        self.umpire = Umpire(field)
        self.commentator = Commentator(self.umpire)
        self.total_overs = total_overs

    def start_match(self):
        """
        Starts the cricket match.
        """
        # Selecting the most experienced player as captain for team 1
        team1_captain = max(self.team1.players, key=lambda player: player.experience)
        self.team1.select_captain(team1_captain)

        # Selecting the most experienced player as captain for team 2
        team2_captain = max(self.team2.players, key=lambda player: player.experience)
        self.team2.select_captain(team2_captain)
        self.team1.batting_order = self.team1.players.copy()
        self.team2.batting_order = self.team2.players.copy()
        self.team1.bowlers = self.team1.players.copy()
        self.team2.bowlers = self.team2.players.copy()

        self.commentator.describe_game(self.team1.captain.name, self.team2.captain.name, self.team1.name, self.team2.name, over=self.total_overs)

        batsman_team1 = self.team1.sending_next_player()
        batsman_team2 = self.team2.sending_next_player()
        bowler_team1 = self.team1.choose_bowler()         
        bowler_team2 = self.team2.choose_bowler() 

        # Team 1 playing
        self.commentator.umpire.scores = 0
        self.commentator.umpire.wickets = 0
        self.commentator.umpire.overs = 0           
        self.commentator.describe_start(self.team1.name, batsman_team1.name, bowler_team2.name)
        self.play_innings(self.team1, self.team2)
        self.commentator.describe_end()
        lastScores = self.commentator.umpire.scores


        # Team 2 playing          
        self.commentator.umpire.scores = 0
        self.commentator.umpire.wickets = 0
        self.commentator.umpire.overs = 0
        self.commentator.describe_start(self.team2.name, batsman_team2.name, bowler_team1.name)
        self.play_innings(self.team2, self.team1)
        self.commentator.describe_end()
        newScores = self.commentator.umpire.scores

        # Final outcome
        if lastScores > newScores:
            self.commentator.describe_final_result(self.team1.name, lastScores)
        else:
            self.commentator.describe_final_result(self.team2.name, newScores)


    def play_innings(self, batting_team, bowling_team):
        """
        Simulates the innings of a team.
        
        Args:
            batting_team (Team): The Team object representing the batting team.
            bowling_team (Team): The Team object representing the bowling team.
        """
        ball_count = 1
        over = 0
        bowler = bowling_team.choose_bowler() 
        batsman = batting_team.sending_next_player()
        
        while over < self.total_overs:
            print("\n")
            self.commentator.current_info(ball_count)
            ball_description = self.commentator.describe_ball(batsman, bowler)
            
            print(ball_description)
            if ball_description.endswith("OUT!"):
                batsman = batting_team.sending_next_player()
                if batsman is None:
                    break
                self.umpire.update_wickets()
                print(f"Wickets: {self.umpire.wickets} , Overs: {self.umpire.overs}")
                print(f"New player {batsman.name} is playing...")
            else:
                runs = random.randint(0, 6)
                self.umpire.update_score(runs)

            if ball_count > 5:
                over += 1
                print(f"Over {over} Starting...")
                self.umpire.update_overs()
                bowler = bowling_team.choose_bowler()
                ball_count = 0

            self.commentator.current_info(ball_count)
            ball_count += 1