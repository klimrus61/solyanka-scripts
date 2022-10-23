from os import path
import sqlite3


DB_NAME = 'avitoFilters.db'



def create_database():

    if not path.exists(DB_NAME):

        print('Created Database!')

        conn = sqlite3.connect('avitoFilters.db')
        cur = conn.cursor()

        cur.execute("""CREATE TABLE list_filters (
            ID INT PRIMARY KEY NOT NULL,
            title varchar(50) 
            );
            """
        )
        cur.execute("""CREATE TABLE marks(
            id INT PRIMARY KEY,
            id_filter INT NOT NULL, 
            name VARCHAR(50) NOT null,
            FOREIGN KEY (id_filter) REFERENCES list_filters (id)
            );

        
        """)

        conn.close()

create_database()