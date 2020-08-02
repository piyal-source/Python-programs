import random


def printboard(grid):
    k = 1
    j = 1
    print()
    for i in range(8):
        if i == 0 or i == 3 or i == 6:
            print('(', end="")
            print(j, end="")
            print(')', end="")
            print('|', end="")
            print('(', end="")
            print(j+1, end="")
            print(')', end=" ")
            print('|', end="")
            print('(', end="")
            print(j + 2, end="")
            print(')', end="")
            j += 3
        elif i == 1 or i == 4 or i == 7:
            print()
            print('', grid[k], '|', '', grid[k+1], '|', '', grid[k+2])
            k = k+3
        else:
            for _ in range(12):
                print('-', end="")
            print()
    print()


def cont():
    btn = input('Do you want to continue playing? Press Y to continue: ')
    if btn == 'Y' or btn == 'y':
        main()
    else:
        exit()


def boardfull(grid):
    if grid.count(' ') > 1:
        return False
    else:
        return True


def posempty(grid, pos):
    if grid[pos] == ' ':
        return True
    else:
        return False


def win(grid, l, p):
    flag = False
    grid[p] = l
    for i in range(1, 8, 3):
        if grid[i] == l and grid[i+1] == l and grid[i+2] == l:
            return True
    for i in range(1, 4):
        if grid[i] == l and grid[i+3] == l and grid[i+6] == l:
            return True
    if (grid[1] == l and grid[5] == l and grid[9] == l) or (grid[3] == l and grid[5] == l and grid[7] == l):
        return True
    if flag is False:
        return False


def addcomp(grid):
    copygrid = [x for x in grid]
    if not boardfull(grid):
        for i in range(1, 10):
            if posempty(copygrid, i):
                if win(copygrid, 'X', i) or win(copygrid, 'O', i):
                    p = i
                    break
                else:
                    copygrid[i] = ' '
        else:
            r = []
            for j in range(1, 10):
                if posempty(grid, j):
                    r.append(j)
                    p = random.choice(r)
        if win(grid, 'O', p):
            printboard(grid)
            print('You lose')
            cont()
        else:
            grid[p] = 'O'
            printboard(grid)
    else:
        print("It is a tie!")
        cont()


def adduser(grid):
    pos = int(input('Enter position of X: '))
    if 0 < pos < 10:
        if posempty(grid, pos):
            if win(grid, 'X', pos):
                printboard(grid)
                print('Congratulations! You win!!')
                cont()
            else:
                grid[pos] = 'X'
                printboard(grid)
                addcomp(grid)
        else:
            print("This position has already been used")
            adduser(grid)
    else:
        print("Invalid position")


def main():
    print("Welcome to my Tic Tac Toe Game!")
    grid = [" " for _ in range(10)]
    printboard(grid)
    while not boardfull(grid):
        adduser(grid)
    if boardfull(grid):
        print("It is a tie!")
        cont()


main()
