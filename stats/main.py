def odds_stats(odds):
    # we fist calculate the total of odds at stake
    hometeam_percentage = (odds[0] * 100) / sum(odds)
    awayteam_percentage = (odds[1] * 100) / sum(odds)
    draw_percentage = (odds[2] * 100) / sum(odds)
    print 'Percentages of home team and away team losing are',hometeam_percentage,awayteam_percentage
    print 'Percentage of a draw is ', draw_percentage
    return {'H':hometeam_percentage,'A':awayteam_percentage,'D':draw_percentage}



def get_best_odds(odds):
    #erturn value of team most likely to win,or rather highest odds/chances(rarely a draw)
    value = odds.index(min(odds))
    if value == 0:
        return ('H',value)
    elif value == 1:
        return ('D',value)
    else:
        return ('A',value)

#here we calculate the rate at which a team causes an upset or not cause one for that matter
#the upset rate is calculated in percentage over total number of games played in a specific set
#the higher the number, the higher the chances the team might cause an upset in the future
#it is used in data analysis of team history data for the future
def calculate_team_upset_rate(actual_scores,odds,hometeam,awayteam):
    #first we check if result is a draw
    if actual_scores[0] == actual_scores[1]:
        #result is a draw so we get who had the lowest odds and award for causing an upset, 1 point
        print ''

