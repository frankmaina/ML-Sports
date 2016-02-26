from __future__ import division


def odds_stats(odds):
    # we fist calculate the total of odds at stake
    # so there are only three possible outcomes in a match,either 1,2,3
    hometeam_percentage = (odds[0] * 100) / (odds[0] + odds[1])
    awayteam_percentage = (odds[1] * 100) / (odds[0] + odds[1])
    print 'According to betting odds Percentages of home team and away team losing are', hometeam_percentage, awayteam_percentage
    return {'H': hometeam_percentage, 'A': awayteam_percentage}


def get_best_odds(odds):
    # return value of team most likely to win,or rather highest odds/chances(rarely a draw)
    value = odds.index(min(odds))
    if value == 0:
        return ('H', value)
    elif value == 1:
        return ('D', value)
    else:
        return ('A', value)


def get_match_winner(self, actual_scores):
    if actual_scores[0] > actual_scores[1]:
        # the home team won
        return {'W': 'H', 'L': 'A', 'D': 0}
    elif actual_scores[1] > actual_scores[0]:
        return {'W': 'A', 'L': 'H', 'D': 0}
    else:
        return {'W': 0, 'L': 0, 'D': 1}


def elo_rating_analytics(home_team, away_team):
    r1 = (pow(10, (home_team['rating'] / 400)))
    r2 = (pow(10, (away_team['rating'] / 400)))
    e1 = (r1 / (r1 + r2))
    e2 = (r2 / (r1 + r2))
    if e1 == e2:
        print "teams are equally balanced out therefore there is a high percent chance for a draw."
    else:
        print "Chances of wining are;", e1* 100, e2* 100
    return {'H': e1, 'A': e2}


##post match math
def apply_elo_rating(home_team, away_team, actual_scores):
    if actual_scores[0] > actual_scores[1]:
        analytics = elo_rating_analytics(home_team, away_team)
        rating1 = home_team['rating'] + (32 * (1 - analytics['H']))
        rating2 = away_team['rating'] + (32 * (0 - analytics['A']))
    elif actual_scores[1] > actual_scores[0]:
        analytics = elo_rating_analytics(home_team, away_team)
        rating1 = home_team['rating'] + (32 * (0 - analytics['H']))
        rating2 = away_team['rating'] + (32 * (1 - analytics['A']))
    elif actual_scores[0] == actual_scores[1]:
        analytics = elo_rating_analytics(home_team, away_team)
        rating1 = home_team['rating'] + (32 * (0.5- analytics['H']))
        rating2 = away_team['rating'] + (32 * (0.5 - analytics['A']))
    print "New rating, ", rating1, rating2
    return (rating1,rating2)


