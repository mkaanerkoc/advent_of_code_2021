from collections import defaultdict

def sum_of_unmarked_numbers(board):
  sum_of_unmarkeds = 0
  for row_set in board['rows']:
    sum_of_unmarkeds += sum(row_set)
  return sum_of_unmarkeds


with open('day_4_input.txt') as day_input:
  input_chunks = day_input.read().split('\n\n')
  numbers = [int(number) for number in input_chunks[0].split(',')]
  boards = [board.split('\n')  for board in input_chunks[1:]]

# Create dictionary to fast-up look for number's positions over the boards
number_addresses = defaultdict(list)
for board_index, board in enumerate(boards):
  for row_index, row in enumerate(board):
    for column_index, number in enumerate(row.split()):
      number_addresses[int(number)].append((board_index, row_index, column_index)) 


# Create dictionary to store unmarked numbers for each row/column and board
unmarked_numbers = {}
for board_index, board in enumerate(boards):
  if board_index not in unmarked_numbers: # initialize missing boards
    unmarked_numbers[board_index] = {'rows':[set() for _ in range(5)], 
                                     'cols':[set() for _ in range(5)]}
  for row_index, row in enumerate(board):
    for column_index, number in enumerate(row.split()):
      unmarked_numbers[board_index]['rows'][row_index].add(int(number))
      unmarked_numbers[board_index]['cols'][column_index].add(int(number))

bingo_boards = {}
for number in numbers:
  positions = number_addresses[number]
  for position in positions:
    if position[0] in bingo_boards:
      continue
    unmarked_numbers[position[0]]['rows'][position[1]].discard(number)
    unmarked_numbers[position[0]]['cols'][position[2]].discard(number)
    
    if len(unmarked_numbers[position[0]]['rows'][position[1]]) == 0:
      sum_of_unmarkeds = sum_of_unmarked_numbers(unmarked_numbers[position[0]])
      bingo_boards[position[0]] = sum_of_unmarkeds*number
    if len(unmarked_numbers[position[0]]['cols'][position[2]]) == 0:
      sum_of_unmarkeds = sum_of_unmarked_numbers(unmarked_numbers[position[0]])
      bingo_boards[position[0]] = sum_of_unmarkeds*number

# Question 1- Answer
print(list(bingo_boards.values())[0])

# Question 2- Answer
print(list(bingo_boards.values())[-1])


