from collections import defaultdict

with open('day_5_input.txt') as day_input:
  convert = lambda x : x.split(',')
  vent_coordinates = [list(map(convert, vent_coord.split(' -> '))) for vent_coord in day_input.read().strip().split('\n')]

vents = defaultdict(int)
for vent in vent_coordinates:
  start, end = vent
  x1, x2 = start
  y1, y2 = end
  x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
  y_range = range(x2, y2 + (1 if x2 < y2 else -1), 1 if x2 < y2 else -1)
  x_range = range(x1, y1 + (1 if x1 < y1 else -1), 1 if x1 < y1 else -1)
  if x1 == y1: # vertical 
    for y in y_range: vents[(x1, y)] += 1
  elif x2 == y2: # horizontal
    for x in x_range: vents[(x, x2)] += 1
  elif abs(x1-y1) == abs(x2-y2):
    for x,y in zip(x_range, y_range): vents[(x, y)] += 1
    

print(len(list(filter(lambda x : x > 1, vents.values()))))
