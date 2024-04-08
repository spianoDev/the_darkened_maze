board = []

def level(size):
    wall = '||'
    path = ' - '
    monster = '^^'
    chest = '$$'

    for num in range(size):
        row1 = [path, path, path, wall, '\n']
        row2 = [path, monster, wall, path, '\n']
        row3 = [path, chest, path, path, '\n']
        row4 = [monster, path, wall, chest, '\n']
        board.append(row1)
        board.append(row2)
        board.append(row3)
        board.append(row4)

level(1)
