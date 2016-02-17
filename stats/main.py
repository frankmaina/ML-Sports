def odds_stats(odds):
    # we fist calculate the total of odds at stake
    # so there are only three possible outcomes in a match,either 1,2,3
    hometeam_percentage = (odds[0] * 100) / (odds[0] + odds[1])
    awayteam_percentage = (odds[1] * 100) / (odds[0] + odds[1])
    print 'According to betting odds Percentages of home team and away team losing are', hometeam_percentage, awayteam_percentage
    return {'H': hometeam_percentage, 'A': awayteam_percentage}


class Match(object):
    def get_best_odds(self, odds):
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
'''

def apply_elo_rating(actual_scores, home_team, away_team):
'''