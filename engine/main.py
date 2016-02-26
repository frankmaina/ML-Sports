from stats.main import *


def apply_prediction(home_team, away_team, odds):
    # we first study odds supplied in by bookmarkers
    odds_chances = odds_stats(odds)
    if abs(odds_chances['H'] - odds_chances['A']) < 30:
        print "By bookmarkers odds, there is a high percent chance for a draw or, the ", get_best_odds(odds), " winning"
        print "Bet decision: ", get_best_odds(odds), "or X. Odds deviation are at", abs(odds_chances['H'] - odds_chances['A'])
    else:
        if get_best_odds(odds) == 'H':
            # the team is at home hence higher percent chance of wining
            print "Bet decision: ", get_best_odds(odds)
        elif get_best_odds(odds) == 'A':
            print "Bet decision: ", get_best_odds(odds)
    # we now apply prediction according to elo rating
    elo_chances = elo_rating_analytics(home_team, away_team)
    print "Chances are", elo_chances['H'] * 100, " for HOME and ", elo_chances['A'] * 100, " for AWAY"
    print abs(elo_chances['H']-elo_chances['A'])