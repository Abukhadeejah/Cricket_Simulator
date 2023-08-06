import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="cricket_db",
    user="*****",
    password="****"
)

# Create the Teams table
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS Teams (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        country VARCHAR(255) NOT NULL
    );
""")
conn.commit()

# Create the Players table
cur.execute("""
    CREATE TABLE IF NOT EXISTS Players (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        bowling FLOAT NOT NULL,
        batting FLOAT NOT NULL,
        fielding FLOAT NOT NULL,
        running FLOAT NOT NULL,
        keeping FLOAT NOT NULL,
        experience FLOAT NOT NULL,
        team_id INTEGER NOT NULL,
        FOREIGN KEY (team_id) REFERENCES Teams (id)
    );
""")
conn.commit()

# Create the Stadiums table
cur.execute("""
    CREATE TABLE IF NOT EXISTS Stadiums (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        city VARCHAR(255) NOT NULL,
        country VARCHAR(255) NOT NULL
    );
""")
conn.commit()

# Close the database connection
cur.close()
conn.close()
