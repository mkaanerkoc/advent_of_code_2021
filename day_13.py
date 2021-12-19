def solution():
    with open('data/day_13_input.txt', 'r') as day_input:
        grid_txt, folds_txt = day_input.read().split('\n\n')
        grid = {tuple(int(y) for y in x.split(',')) for x in grid_txt.split('\n')}
        folds = [tuple(y for y in fold.replace('fold along ', '').split('=')) for fold in folds_txt.split('\n')]

    answer_1 = calculate_remaining_marks(grid, folds[:1])
    answer_2 = calculate_remaining_marks(grid, folds)

    print(len(answer_1))
    print_grid(answer_2)


def calculate_remaining_marks(grid, folds: list):
    for folding in folds:
        dimension, level = folding
        level = int(level)
        if dimension == 'x':
            grid = fold(grid, lambda y: (level * 2 - y[0], y[1]), lambda x: x[0] > level)
        elif dimension == 'y':
            grid = fold(grid, lambda y: (y[0], level * 2 - y[1]), lambda x: x[1] > level)
    return grid


def fold(grid, translate, threshold_filter):
    folded_set = set(map(translate, filter(threshold_filter, grid)))
    grid = grid.difference(set(filter(threshold_filter, grid)))
    grid = grid.union(folded_set)
    return grid


def print_grid(grid):
    width, height = 0, 0
    for point in grid:
        width = max(width, point[0])
        height = max(height, point[1])

    for y in range(height+4):
        for x in range(width+4):
            if (x, y) in grid:
                print('# ', end='')
            else:
                print('. ', end='')
        print('')
