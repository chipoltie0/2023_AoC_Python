from rich import print
from rich.pretty import pprint
# import re
# from collections import defaultdict
# from itertools import groupby

with open(r'2023_aoc_python/day3/day3.txt','r') as f:
    datalines = f.readlines()

class Part:
    self.part_number = 0
    self.number_locations = []
    self.schematic_char = ''
    self.schematic_point = ()


class PartFactory:

    def from_schematic_point()

blueprint = {}
points_of_interest = []
number_spots = []
for y, row in enumerate(datalines):
    for x, column in enumerate(row[0:-1]):
        blueprint[(x,y)] = column
        if (column not in ['.',r'\\n'] and not column.isnumeric()):
            points_of_interest.append((x,y))
        elif column.isnumeric():
            number_spots.append((x,y))
        

pprint(list(zip(points_of_interest,[blueprint[(point[0],point[1])] for point in points_of_interest])))
