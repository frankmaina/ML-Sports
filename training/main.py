from peewee import *

db = SqliteDatabase('mlsports.db')

class TeamRating(Model):
    name = CharField()
    rating = IntegerField()

    class Meta:
        database = db # This model uses the "people.db" database.

try:
    db.create_tables([TeamRating])
except OperationalError:
    print "Table exists"



def create_ratings(file_path):
    import csv
    with open(file_path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['HomeTeam'], row['AwayTeam'])
            #search for team in db.
            try:
                home_team = TeamRating.get(TeamRating.name==row['HomeTeam'])
            except Exception as e:
                #the team does not exist in the db hence we create it
                home_team  = TeamRating.create(name=row['HomeTeam'],rating=1000)
            #do the same for the away team
            try:
                away_team = TeamRating.get(TeamRating.name==row['AwayTeam'])
            except Exception as e:
                #the team does not exist in the db hence we create it
                away_team  = TeamRating.create(name=row['AwayTeam'],rating=1000)

         print 'Successfully created ratings for the provided teams.'
