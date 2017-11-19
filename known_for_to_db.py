import psycopg2
import codecs
from config import config

def known_for_to_db(known_for_file):
    """ Transfer known_for data to PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        # create a cursor
        cur = conn.cursor()

        # Create Title Table
        cur.execute("CREATE TABLE known_for( \
                     nconst CHAR(9), \
                     tconst CHAR(9), \
                     FOREIGN KEY (nconst) REFERENCES name(nconst), \
                     FOREIGN KEY (tconst) REFERENCES title(tconst))")


        # Reading from file to Database
        f = codecs.open(known_for_file, 'r','utf-8') #utf-8 parameter allows to read all the data from file
        cur.copy_from(f, 'known_for', sep="\t")
        conn.commit()

     # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    print("Transfering " + known_for_file[:-4] + " to PostgreSQL database succeed.")
