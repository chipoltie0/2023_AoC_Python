from rich import print
from rich.pretty import pprint
import re
from collections import defaultdict
from itertools import groupby

with open(r'2023_aoc_python/day2/day2.txt','r') as f:
    datalines = f.readlines()


game_limits = {'red':12,'green':13,'blue':14}
# input parsing
parsed_games = []
for line in datalines:
    # Game 1: 4 red, 8 green; 8 green, 6 red; 13 red, 8 green; 2 blue, 4 red, 4 green
    #  GAME Index: SUBGAME ; SUBGAME, that may continue
    linematch = re.search(r'Game (?P<index>\d+?): (?P<subgames>.*)',line)
    index_match = int(linematch.group('index'))
    subgames_match = linematch.group('subgames')
    #pprint([index_match,subgames_match])
    # break up subgames
    subgames_strings = subgames_match.split("; ")
    for sub_index, subgame in enumerate(subgames_strings):
        sub_game_stats = defaultdict(lambda: 0)
        # split up subgames into item lists via the comma, creates items like ['17 blue','5 red']
        sub_game_items = subgame.split(', ')
        for sub_game_item in sub_game_items:
            # split each sub_game_item based on spaces, splits into ['17','blue'] and ['5','red']
            sub_game_split = sub_game_item.split(' ')
            # print(sub_game_split)
            sub_game_item_count = sub_game_split[0]
            sub_game_item_color = sub_game_split[1]
            # add the color to the the subgame list, will start at zero
            sub_game_stats[sub_game_item_color] += int(sub_game_item_count)
        parsed_games.append({'index':index_match,'subindex':sub_index} | sub_game_stats)
# pprint(parsed_games)

# Judge each game/subgame to see if they are possible
possible_games = set([x['index'] for x in parsed_games])
for game in parsed_games:
    for key,limit_value in game_limits.items():
        if limit_value < game[key]:
            possible_games.discard(game['index'])
            # pprint(f"Game {game['index']}, subgame {game['subgame']} is impossible because of {key}, limit is {value} but got {game[key]}")

pprint(f'Final output is: {sum(possible_games)}')

# Part 2 is to get min number of cubes possible per game index

# organize values by their index key
grouped_games = [list(subgames) for key, subgames in groupby(parsed_games,lambda game: game['index'])]

games_min_possible = []
for group in grouped_games:
    # now group contains a list of games
    group_output = {'index': group[0]['index']}
    for color in ['red','green','blue']:
        group_output[color] = max([item[color] for item in group])
    
    games_min_possible.append(group_output)

# pprint(games_min_possible)

pprint(f"Final output of part 2 is {sum([x['red']*x['blue']*x['green'] for x in games_min_possible])}")