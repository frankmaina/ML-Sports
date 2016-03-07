from peewee import *
from stats.main import apply_elo_rating, get_best_odds, get_match_winner
import csv
import os

db = SqliteDatabase('mlsports.db')


class TeamRating(Model):
    name = CharField()
    rating = IntegerField()

    class Meta:
        database = db  # This model uses the "people.db" database.


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
            # search for team in db.
            try:
                home_team = TeamRating.get(TeamRating.name == row['HomeTeam'])
            except Exception as e:
                # the team does not exist in the db hence we create it
                home_team = TeamRating.create(name=row['HomeTeam'], rating=1000)
            # do the same for the away team
            try:
                away_team = TeamRating.get(TeamRating.name == row['AwayTeam'])
            except Exception as e:
                # the team does not exist in the db hence we create it
                away_team = TeamRating.create(name=row['AwayTeam'], rating=1000)
        print 'Successfully created ratings for the provided teams.'


def train_ratings(path, actual_scores):
    for file_path in path:
        file = os.path.abspath('datasets/england/ (' + str(file_path) + ').csv')
        with open(file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader
                try:
                home_team_ratings = TeamRating.get(TeamRating.name == row['HomeTeam'])
                except
                away_team_ratings = TeamRating.get(TeamRating.name == row['AwayTeam'])
                home_team = {'team': row['HomeTeam'], 'rating': home_team_ratings.rating}
                away_team = {'team': row['AwayTeam'], 'rating': away_team_ratings.rating}
                actual_scores[0] = row['FTHG']
                actual_scores[1] = row['FTAG']
                teams = apply_elo_rating(home_team, away_team, actual_scores)
                print row['HomeTeam'], teams[0]
                home_team = TeamRating.get(TeamRating.name == row['HomeTeam'])
                home_team.rating = teams[0]
                home_team.save()
                away_team = TeamRating.get(TeamRating.name == row['AwayTeam'])
                away_team.rating = teams[1]
                away_team.save()


def get_upset_rate_against_odds(csv_file):
    upset = 0
    no_upset = 0
    total = 0
    draw_favour = 0
    total = 0
    actual_scores = ['','']
    odds = ['', '', '']
    print "Compiling data..."
    for file_path in csv_file:
        file = os.path.abspath('datasets/england/ (' + str(file_path) + ').csv')
        print "At ", file
        with open(file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # start by getting odds
                odds[0] = row['B365H']
                odds[1] = row['B365D']
                odds[2] = row['B365A']
                best_odds = get_best_odds(odds)
                actual_scores[0] = row['FTHG']
                actual_scores[1] = row['FTAG']
                match = get_match_winner(actual_scores)
                total += 1
                if best_odds[0] == "H":
                    # odds were in favour for home
                    if match == 'H':
                        # home won, no upset there
                        no_upset += 1
                    elif match == 'A':
                        # an upset occurred
                        upset += 1
                    else:
                        # match was a draw
                        draw_favour += 1
                elif best_odds[0]== "A":
                    # odds were in favour for home
                    if match == 'A':
                        # home won, no upset there
                        no_upset += 1
                    elif match == 'H':
                        # an upset occurred
                        upset += 1
                    else:
                        # match was a draw
                        draw_favour += 1


    print "We analyzed: ", upset + no_upset + draw_favour, total
    print "Percentage of upsets by bet365 bookmarks was:", upset
    print "Draw percentage was: ", (draw_favour * 100) / total
    print "No upset percentage was: ", (no_upset * 100) / total
