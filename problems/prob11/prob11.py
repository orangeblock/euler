grid = []
with open('grid.txt') as f:
    for line in f:
        grid.append([int(x) for x in line.split()])

def mul(l):
    """ Return the product of the elements in l """
    if len(l) == 0: return 0
    product = 1
    for el in l: 
        product *= el
    return product

def products(grid, x, y):
    prods = []

    # row products
    for r in range(x, x+4):
        prods.append(mul([grid[r][c] for c in range(y, y+4)]))

    # column products
    for c in range(y, y+4):
        prods.append(mul([grid[r][c] for r in range(x, x+4)]))

    # diagonal products
    prods.append(mul([grid[x][y], grid[x+1][y+1], grid[x+2][y+2], grid[x+3][y+3]]))
    prods.append(mul([grid[x+3][y], grid[x+2][y+1], grid[x+1][y+2], grid[x][y+3]]))

    return prods

from itertools import chain
print(max(list(chain(
    *[products(grid, x, y) for x in range(len(grid)-4) for y in range(len(grid)-4)]))))
