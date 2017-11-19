import psycopg2
from config import config
import codecs

def title_to_db(title_file):
    """ Transfer title data to PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        # create a cursor
        cur = conn.cursor()

        # Create Title Table
        cur.execute("CREATE TABLE title( \
                     tconst CHAR(9) PRIMARY KEY, \
                     titleType VARCHAR(255), \
                     primaryTitle TEXT, \
                     originalTitle TEXT, \
                     isAdult BOOLEAN, \
                     startYear SMALLINT, \
                     endYear SMALLINT, \
                     runtimeMinutes INT, \
                     genres VARCHAR(255))")


        # Reading from file to Database
        f = codecs.open(title_file, 'r','utf-8') #utf-8 parameter allows to read all the data from file
        cur.copy_from(f, 'title', sep="\t")
        conn.commit()

     # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    print("Transfering " + title_file[:-4] + " to PostgreSQL database succeed.")
