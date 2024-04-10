board = []

def level(size):
    wall = '||'
    path = ' - '
    monster = '^^'
    chest = '$$'

    for num in range(size):
        row1 = [wall, wall, wall, wall, '\n']
        row2 = [wall, monster, wall, wall, '\n']
        row3 = [path, path, wall, chest, '\n']
        row4 = [wall, path, path, path, '\n']
        board.append(row1)
        board.append(row2)
        board.append(row3)
        board.append(row4)

level(1)
