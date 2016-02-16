def odds_stats(odds):
    # we fist calculate the total of odds at stake
    hometeam_percentage = (odds[0] * 100) / sum(odds)
    awayteam_percentage = (odds[1] * 100) / sum(odds)
    draw_percentage = (odds[2] * 100) / sum(odds)
    print 'Percentages of home team and away team losing are',hometeam_percentage,awsayteam_percentage
    return {'H':home}