import sqlite3
from sqlite3 import Error

def create_connection(df_file):
    """create a database connection tot he Sqlite database
        specified by df_file
    :param db_file: database file
    :return: Connection object or None
    """
    
    conn = None
    try:
        conn = sqlite3.connect(df_file)
        return conn
    except Error as e:
        print(e)
    
    return conn

def create_table(conn, create_table_sql):
    """craete a table from create_table_sql statement
    :param conn: Connection object
    : param create_table_sql: a CREATE TABLE statement
    :return:
    """
    
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = r"/home/pi/Documents/gettoknow/reactiongame/gamedb.db"
    
    sql_create_game_table = """CREATE TABLE IF NOT EXISTS games (
                                id integer PRIMARY KEY,
                                game_id text NOT NULL,
                                date timestamp DEFAULT CURRENT_TIMESTAMP,
                                player1 text NOT NULL,
                                player2 text NOT NULL,
                                player1_agg_score integer,
                                player2_agg_score integer,
                                rounds integer
                                );"""
    
    sql_create_game_rounds_table = """CREATE TABLE IF NOT EXISTS rounds(
                                        round_id integer PIMARY KEY,
                                        game_id text NOT NULL,
                                        round integer,
                                        light integer, 
                                        player1_score integer,
                                        player2_score integer,
                                        reactiontime float,
                                        FOREIGN KEY (game_id) REFERENCES games (game_id)
                                        );"""
    # create a db connection
    conn = create_connection(database)
    
    # create tables
    if conn is not None:
        
        # create games table
        create_table(conn, sql_create_game_table)
        
        # create rounds table
        create_table(conn, sql_create_game_rounds_table)
        
if __name__ == '__main__':
    main()
