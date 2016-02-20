"""
Warning: This project and its original source code have been created out of hobby,
and are free to download and use, therefore of non-profit nature.

The Author of this site is not affiliated,
or connected in any other way, with any of the external sites linked from this project.
Their presence on this project is shear act of sharing information related to sports prediction
and betting activities.

Therefore, Webmaster of this site cannot guarantee accuracy of any information
or calculation acquierd from using the project , and does not accept any responsibility for
any losses or damages you may suffer due to the use.

Please bear in mind that sports betting is sensible act,
that may lead you to losing significant money and time,
and/or may lead you to addiction. You should never expose
more money to sports trading and betting than you can afford
to lose, and you should never dedicate time to sports trading a
nd betting when you need to be involved in other personal
 or business activities.

Also odds as used in this project do not stand for actual points
of reference as to who will win, just that it can be a sign of
who is expected to win. The odds against bets are usually placed
for weaker teams as the odds are stacked against them.
Long odds: The likelihood of an event occurring is low.
Short odds: The likelihood of an event occurring is high.
"""
import csv
from stats.main import *
from engine.main import *

# prepare command line arguments passed in
hometeam = {'team_name': "abcd", 'upset_potential': 0, 'rating': 1259, 'games_played': 1}
awayteam = {'team_name': "abcd", 'upset_potential': 0, 'rating': 1200, 'games_played': 1}

odds = [11.95, 3.26, 1.84]
actual_scores = [2, 1]
# odds_percentage = odds_stats(odds)



apply_prediction(hometeam, awayteam, odds)
