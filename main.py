from training.main import create_ratings, train_ratings,get_upset_rate_against_odds
from engine.main import *

mode = "train"

if mode == "predict":

    # prepare command line arguments passed in
    hometeam = {'team_name': "Newcastle", 'upset_potential': 0, 'rating': 1084, 'games_played': 1}
    awayteam = {'team_name': "Norwich", 'upset_potential': 0, 'rating': 1104, 'games_played': 1}

    odds = [11.95, 3.26, 1.84]
    actual_scores = [2, 1]
    # odds_percentage = odds_stats(odds)
    apply_prediction(hometeam, awayteam, odds)
    apply_prediction(hometeam, awayteam, odds)
elif mode == "train":
    create_ratings('E0.csv')
    actual_scores = [0, 0]
    csv_files = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    train_ratings(csv_files,actual_scores)
    '''
    get_upset_rate_against_odds(csv_files)'''
