board = []

def level(size):
    wall = '||'
    path = ' - '
    monster = '^^'
    chest = '$$'

    for num in range(size):
        row1 = [path, wall, chest, wall, '\n']
        row2 = [monster, monster, path, wall, '\n']
        row3 = [path, path, monster, chest, '\n']
        row4 = [wall, path, path, path, '\n']
        board.append(row1)
        board.append(row2)
        board.append(row3)
        board.append(row4)

level(1)
