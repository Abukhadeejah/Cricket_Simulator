import os
from dotenv import load_dotenv
import psycopg2
import random
from player import Player
from team import Team
from field import Field
from umpire import Umpire 
from commentator import Commentator
from match import Match
from stadium import Stadium

# Load environment variables from .env file
load_dotenv()

# Connect to the PostgreSQL database using environment variables
conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

# Create a cursor object to interact with the database
cur = conn.cursor()

# Get the team names from the user
team1_name = input("Enter the name of Team 1: ")
team2_name = input("Enter the name of Team 2: ")

# Retrieve the players for Team 1 from the database
cur.execute("SELECT * FROM Players WHERE team_id IN (SELECT id FROM Teams WHERE name = %s)", (team1_name,))
team1_player_rows = cur.fetchall()

# Retrieve the players for Team 2 from the database
cur.execute("SELECT * FROM Players WHERE team_id IN (SELECT id FROM Teams WHERE name = %s)", (team2_name,))
team2_player_rows = cur.fetchall()

# Create the player objects for Team 1
team1_players = []
for row in team1_player_rows:
    team1_players.append(Player(row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

# Create the player objects for Team 2
team2_players = []
for row in team2_player_rows:
    team2_players.append(Player(row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

# Create the team objects
team1 = Team(team1_name, team1_players)
team2 = Team(team2_name, team2_players)

# Get the stadium name from the user
stadium_name = input("Enter the name of the stadium: ")

# Retrieve the stadium details from the database
cur.execute("SELECT * FROM Stadiums WHERE name = %s", (stadium_name,))
stadium_rows = cur.fetchall()

# Create the stadium objects
stadiums = []
for row in stadium_rows:
    stadiums.append(Stadium(row[1], row[2], row[3], row[4], row[5]))

# Get the stadium details for the field object constructor
size = stadiums[0].size
pitch_conditions = stadiums[0].pitch
fan_ratio = random.uniform(0.0, 1.0) 
home_advantage = random.uniform(0.0, 1.0)


# Create the field object
field = Field(size, pitch_conditions, fan_ratio, home_advantage)

# Close the cursor and database connection
cur.close()
conn.close()

# Start the match simulation
total_overs = 2
match = Match(team1, team2, field, total_overs)
match.start_match()
