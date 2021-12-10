with open('day_10_input.txt', 'r') as day_input:
  lines = [list(row) for row in day_input.read().split('\n')]


symbols = {"{": "}", "(": ")", "[": "]", "<": ">"}
wrong_symbol_points = {")" : 3, "]": 57, "}":1197, ">": 25137}
repairing_symbol_points = {")" : 1, "]": 2, "}": 3, ">": 4}

wrong_symbol_total = []
repairing_costs = []
for line in lines:
  symbol_stack = []
  wrong_symbols = []
  for char in line:
    if char not in symbols.keys(): # if character is closing
      if len(symbol_stack) == 0:
        wrong_symbols.append(char)
        break
      if symbols[symbol_stack[-1]] != char:
        wrong_symbols.append(char)
        break
      if symbols[symbol_stack[-1]] == char:
        symbol_stack.pop()
    else: # add opening characters everytime
      symbol_stack.append(char)
  wrong_symbol_total += wrong_symbols

  if len(wrong_symbols) == 0 and len(symbol_stack) > 0: # no wrong symbols, only missing symbols
    total_score = 0
    for char in reversed(symbol_stack): # order matters
      total_score = total_score * 5 + repairing_symbol_points[symbols[char]]
    repairing_costs.append(total_score)

answer_1 = sum(wrong_symbol_points[symbol] for symbol in wrong_symbol_total)
answer_2 = sorted(repairing_costs)[len(repairing_costs)//2]
print(answer_1, answer_2)

