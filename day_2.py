with open('day_2_input.txt') as day2_input:
  moves = day2_input.readlines()
  moves = pd.DataFrame([(move.split(' ')[0], int(move.split(' ')[1])) for move in moves], columns=['direction', 'size'])
  moves = moves.pivot(columns='direction', values='size').fillna(0) # convert to pivot to calculate easily recursive operations with cumsum() operator

# Question 1 - Position without Aim
horizontal = moves['forward'].sum()
depth = (moves['down'] - moves['up']).sum()
answer1 = int(horizontal * depth) # 125395


# Question 2 - Position with Aim
# That question requires recursive calculations [!]
# Note: For recursive calculations which are not vectorisable, numba, which uses JIT-compilation and works with lower level objects, often yields large performance improvements.
moves['aim'] = (moves['down'] - moves['up']).cumsum()
moves['horizontal'] = moves['forward'].cumsum()
moves['depth'] = (moves['aim'] * moves['forward']).cumsum()
position = moves.iloc[-1].to_dict()
answer2 = int(position['depth'] * position['horizontal'])
