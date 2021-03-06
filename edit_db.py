import sqlite3
import config
import os
import cgi
import leaderboard_db

def add_leaderboard(titleLeaderboardInput, descriptionInput, genreInput, authorInput):
    conn = sqlite3.connect(config.db_filename)
    
    c = conn.cursor()

    titleLeaderboard = titleLeaderboardInput
    description = descriptionInput
    genre = genreInput
    author = authorInput

    users = leaderboard_db.get_users()

    for user in users:
        if user.Username == author:
            c.execute("INSERT INTO Leaderboards(Name, User_Id, Description, Genre) VALUES( ?, ?, ?, ?)", (str(titleLeaderboard),str(user.User_Id),str(description),str(genre)))
        else:
            c.execute("INSERT INTO Leaderboards(Name, User_Id, Description, Genre) VALUES(?, ?, ?, ?)", (str(titleLeaderboard),str((len(users) + 1)),str(description),str(genre)))
 
    #c.execute("INSERT INTO Users(Username, Description, Password) VALUES('Kitty Jacobs','Student at Immaculata Institute', 'aaa')")

    conn.commit()
    c.close()