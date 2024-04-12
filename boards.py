board = []

def level(size):
    wall = '||'
    path = ' - '
    monster = '^^'
    chest = '$$'

    for num in range(size):
        row1 = [path, path, chest, path, '\n']
        row2 = [path, monster, path, wall, '\n']
        row3 = [path, path, monster, chest, '\n']
        row4 = [path, path, path, path, '\n']
        board.append(row1)
        board.append(row2)
        board.append(row3)
        board.append(row4)

level(1)
