from rich import print
from rich.pretty import pprint
import re

with open(r'2023_aoc_python/day1/day1.txt','r') as f:
    datalines = f.readlines()

# pprint(datalines)
output = []
for line in datalines:
    # search   
    found_digits = re.findall(r'\d', line)
    output.append(found_digits)

#pprint(output)

# get the first and last digits of each line
final_num_list = []
for line in output:
    # get first and last digit
    first_digit = str(line[0])
    last_digit = str(line[-1])
    final_number = int(first_digit + last_digit)
    final_num_list.append(final_number)

#pprint(final_num_list)

final_output = sum(final_num_list)
pprint(final_output)

# 2nd puzzle

find_text = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
output_rd2 = []
for line in datalines:
    # search   
    found_digits = re.findall(r'(?=(1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine))',line[0:-1])
    corrected_find = [find_text[x] for x in found_digits]
    if corrected_find:
        output_rd2.append(corrected_find)

# pprint(output_rd2)

# get the first and last digits of each line
final_num_list_2 = []
for line in output_rd2:
    # get first and last digit
    first_digit = str(line[0])
    last_digit = str(line[-1])
    final_number = int(first_digit + last_digit)
    final_num_list_2.append(final_number)

#pprint(list(zip(datalines,output_rd2,final_num_list_2)))

#pprint(final_num_list_2)
final_output_2 = sum(final_num_list_2)
pprint(final_output_2)