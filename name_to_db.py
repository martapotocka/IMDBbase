import psycopg2
import codecs
from config import config

def name_to_db(name_file):
    """ Transfer name data to PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        # create a cursor
        cur = conn.cursor()

        # Create Name Table
        cur.execute("CREATE TABLE name( \
                     nconst CHAR(9) PRIMARY KEY, \
                     primaryName VARCHAR(255), \
                     birthYear SMALLINT, \
                     deathYear SMALLINT, \
                     primaryProfession VARCHAR(255))")


        # Reading from file to Database
        f = codecs.open(name_file, 'r','utf-8') #utf-8 parameter allows to read all the data from file
        cur.copy_from(f, 'name', sep="\t")
        conn.commit()

     # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    print("Transfering " + name_file[:-4] + " to PostgreSQL database succeed.")
