from flask import Flask, request
from flask_restful import Resource, Api
from config import config
import psycopg2

params = config()
app = Flask(__name__)
api = Api(app)

class StartYear(Resource):
    def get(self,startYear):
        try:
            # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)
            # create a cursor
            cur = conn.cursor()

            #Query the database
            cur.execute("SELECT title.primarytitle, name.primaryname \
                         FROM title \
                         INNER JOIN known_for \
                         ON title.tconst = known_for.tconst \
                         INNER JOIN name \
                         ON name.nconst = known_for.nconst \
                         WHERE title.startyear='%s' ORDER BY title.primarytitle ASC;"%startYear)

            result = {'Movies from ' + startYear: cur.fetchall()}
            return result

         # close the communication with the PostgreSQL
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

class Genre(Resource):
    def get(self, genre):
        try:
            # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)
            # create a cursor
            cur = conn.cursor()

            #Query the database
            cur.execute("SELECT title.primarytitle, name.primaryname \
                         FROM title \
                         INNER JOIN known_for \
                         ON title.tconst = known_for.tconst \
                         INNER JOIN name \
                         ON name.nconst = known_for.nconst \
                         WHERE title.genres LIKE = '%genre%' ORDER BY title.primarytitle ASC;"%genre)
            result = {'Movies of genre: ' + genre: cur.fetchall()}
            return result

         # close the communication with the PostgreSQL
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

class ActorName(Resource):
    def get(self,actorName):
        try:
            # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)
            # create a cursor
            cur = conn.cursor()

            #Query the database
            cur.execute("SELECT title.primarytitle \
                         FROM title \
                         INNER JOIN known_for \
                         ON title.tconst = known_for.tconst \
                         INNER JOIN name \
                         ON name.nconst = known_for.nconst \
                         WHERE name.primaryname='%s'"%actorName)

            result = {'Movies of ' + actorName: cur.fetchall()}
            return result

         # close the communication with the PostgreSQL
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()


api.add_resource(StartYear, '/startyear/<startYear>')
api.add_resource(Genre, '/genre/<genre>')
api.add_resource(ActorName, '/actorname/<actorName>')

if __name__ == '__main__':
     app.run()
