"""
20 min
The LeagueTable class tracks the score of each player in a league. After each
game, the player records their score with the record_result function.
The player's rank in the league is calculated using the following logic:
* The player with the highest score is ranked first (rank 1). The player with the lowest score is ranked last.
* If two players are tied on score, then the player who has played the fewest games is ranked higher.
* If two players are tied on score and number of games played,
  then the player who was first in the list of players is ranked higher.
Implement the player_rank function that returns the player at the given rank.
For example:
table = LeagueTable(['Mike', 'Chris', 'Arnold'])
table.record_result('Mike', 2)
table.record_result('Mike', 3)
table.record_result('Arnold', 5)
table.record_result('Chris', 5)
print(table.player_rank(1))
All players have the same score. However, Arnold and Chris have played fewer
games than Mike, and as Chris is before Arnold in the list of players, he is
ranked first. Therefore, the code above should display "Chris".
    from collections import Counter
    from collections import OrderedDict
    class LeagueTable:
        def __init__(self, players):
            self.standings = OrderedDict([(player, Counter()) for player in players])
        def record_result(self, player, score):
            self.standings[player]['games_played'] += 1
            self.standings[player]['score'] += score
        def player_rank(self, rank):
            return None
    table = LeagueTable(['Mike', 'Chris', 'Arnold'])
    table.record_result('Mike', 2)
    table.record_result('Mike', 3)
    table.record_result('Arnold', 5)
    table.record_result('Chris', 5)
    print(table.player_rank(1))
"""

from collections import Counter
from collections import OrderedDict
class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])
    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score
    def player_rank(self, rank):
        for player in self.standings:
            self.standings[player]['avg_score'] = -(self.standings[player]['score'] / self.standings[player]['games_played'])

        ranks = [(counter['avg_score'],i, name) for i, (name, counter) in enumerate(self.standings.items())]
        return sorted(ranks)[rank-1][2]

    def player_rank_solution2(self, rank):
        for player in self.standings:
            self.standings[player]['avg_score'] = -(self.standings[player]['score'] / self.standings[player]['games_played'])
        
        scoresTable = dict()
        for player in self.standings:
            avg_score = self.standings[player]['avg_score']
            scoresTable[avg_score] = scoresTable.get(avg_score,[]) + [player]
        
        print(scoresTable)
        sortedScoresTable = sorted(scoresTable)
        print(sortedScoresTable)

        if rank <= len(sortedScoresTable):
            scoreForRank = sortedScoresTable[rank-1]
            print(rank-1)
            print(scoreForRank)
            return scoresTable[scoreForRank][0]

table = LeagueTable(['Mike', 'Chris', 'Arnold'])
table.record_result('Mike', 2)
table.record_result('Mike', 30)
table.record_result('Arnold', 5)
table.record_result('Chris', 5)
print(table.player_rank(1))

"""
Mike -> 2.5
Chris -> 5
Arnold -> 5

[
2.5 -> [Mike]
5 -> [Chris, Arnold]
]
"""