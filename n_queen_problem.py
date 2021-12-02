'''
Solution for N-queen problem. 
It solves the N-queen problem recursively by searching through all possible paths.
'''

def calculate_legal_squares(size:int, queens:list, row:int) -> set:
    '''
    helper method. it calculates the legal squares for the 
    given row by using board size and already placed queens 
    on the board.
    '''
    # initially set all squares as legal.
    line = set(range(size))
    for queen in queens:
        queen_row, queen_col = queen
        depth = row - queen_row
        # remove the illegal squares from set. out of board squares will be discarded.
        line.discard(queen_col)
        line.discard(queen_col-depth)
        line.discard(queen_col+depth)
    return line

def number_of_combinations(size, queens=[], row=0) -> int:
    '''
    main solver method. it calculates all the legal squares
    on the given row and recursively calling itself for each
    of the legal square it has. it does depth-first-search by 
    leveraging python list since it can works like a stack 
    with append and pop methods.
    '''
    legal_squares = calculate_legal_squares(size, queens, row)
    
    if row == (size-1): 
        return len(legal_squares)
    
    number_of_paths = 0
    for square in legal_squares:
        ''' this is where depth-first-search is done '''
        queens.append((row, square))
        number_of_paths += number_of_combinations(size, queens, row+1)
        queens.pop()
    
    return number_of_paths
  
# Main demonstration. Since other parameters are initialized as default, we can just pass the size parameter.
result = number_of_combinations(size=8)
print(result)

