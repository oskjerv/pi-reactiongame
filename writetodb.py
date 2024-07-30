
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """create a database conenction to the SQlite database
        specified by db_file
    :param db_file: database file
    :return: connection object or None
    """
    
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    
    return conn

def create_game(conn, game):
    """
    Create a new game into the games table
    :param conn:
    :param game:
    :return: id:
    """
    
    sql = ''' INSERT INTO games(game_id, player1, player2, player1_agg_score, player2_agg_score, rounds)
              VALUES(?, ?, ?, ?, ?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, game)
    conn.commit()
    return cur.lastrowid

def create_round(conn, round):
    """
    Create a new round
    :param conn:
    :param taska:
    :return:
    """
    
    sql = '''INSERT INTO rounds(game_id, round, light, player1_score, player2_score, reactiontime)
             VALUES(?, ?, ?, ?, ?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, round)
    conn.commit()
    return cur.lastrowid

def main_game(game_id, player1_name, player2_name, player1_score, player2_score, round):
    database = r"/home/pi/Documents/gettoknow/reactiongame/gamedb.db"
    
    # create a db connection
    conn = create_connection(database)
    
    with conn:
        #create a new game
        game = (game_id, player1_name, player2_name, player1_score, player2_score, round)
        create_game(conn, game)
        
def main_round(game_id, round, light, player1_score, player2_score, reactiontime):
    database = r"/home/pi/Documents/gettoknow/reactiongame/gamedb.db"
    
    # create a db connection
    conn = create_connection(database)
    
    with conn:
        #create a new game
        rounddata = (game_id, round, light, player1_score, player2_score, reactiontime)
        create_round(conn, rounddata)
        
