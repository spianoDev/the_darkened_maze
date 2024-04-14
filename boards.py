board = []

def level(size):
    wall = '||'
    path = ' - '
    monster = '^^'
    chest = '$$'

    for num in range(size):
        row1 = [path, wall, chest, wall, '\n']
        row2 = [path, monster, path, wall, '\n']
        row3 = [wall, path, path, chest, '\n']
        row4 = [wall, path, monster, path, '\n']
        board.append(row1)
        board.append(row2)
        board.append(row3)
        board.append(row4)

level(1)
