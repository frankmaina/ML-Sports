from peewee import *
from stats.main import apply_elo_rating


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



def train_ratings(file_path,actual_scores):
    import csv
    with open(file_path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            home_team_ratings = TeamRating.get(TeamRating.name==row['HomeTeam'])
            away_team_ratings = TeamRating.get(TeamRating.name==row['AwayTeam'])
            home_team = {'team':row['HomeTeam'],'rating':home_team_ratings.rating}
            away_team = {'team':row['AwayTeam'],'rating':away_team_ratings.rating}
            actual_scores[0] = row['FTHG']
            actual_scores[1] = row['FTAG']
            teams = apply_elo_rating(home_team,away_team,actual_scores)
            print row['HomeTeam'], teams[0]
            home_team = TeamRating.get(TeamRating.name==row['HomeTeam'])
            home_team.rating = teams[0]
            home_team.save()
            away_team = TeamRating.get(TeamRating.name==row['AwayTeam'])
            away_team.rating = teams[1]
            away_team.save()