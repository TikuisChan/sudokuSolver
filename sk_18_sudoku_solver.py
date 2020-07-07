backstep = 0
testGrid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]]


def locateNextEmptyCell(grid):
    # locate empty cell, return False if no empty cell found
    for i in range(0, 9):
        for j in range(0, 9):
            if grid[i][j] == 0:
                return i, j
    return False


def checkValid(grid, i, j, guess):
    # check row
    if guess in grid[i][:]:
        return False
    # check column
    if guess in [grid[c][j] for c in range(9)]:
        return False
    # check sub-square
    # obtain the sub-square top left corner
    iCorner = (i // 3) * 3
    jCorner = (j // 3) * 3
    # generate a list of contents of the sub-square
    subSquare = [grid[r][c] for r in range(iCorner, iCorner + 3) for c in range(jCorner, jCorner + 3)]
    if guess in subSquare:
        return False
    # all pass
    return True


def sudokuSolver(grid):
    global backstep
    # locate empty cell to fill, return True if all cells were filled
    if locateNextEmptyCell(grid):
        i, j = locateNextEmptyCell(grid)
    else:
        print('finish!')
        return True
    # guessing loop, recursive
    ans = False
    for guess in range(1, 10):
        if checkValid(grid, i, j, guess):
            grid[i][j] = guess
            ans = sudokuSolver(grid)
    if not ans:
        grid[i][j] = 0
        backstep += 1
    else:
        return True


def printGrid(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=' ')
            if j % 3 == 2 and j != 8:
                print('|', end=' ')
        if i % 3 == 2 and i != 8:
            print()
            print('-' * 6 + '+' + '-' * 7 + '+' + '-' * 6)
        else:
            print()


if __name__ == "__main__":
    try:
        sudokuSolver(testGrid)
        printGrid(testGrid)
        print(f'back step = {backstep}')
    except Exception as e:
        print(e)
