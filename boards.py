def level(size):
    wall = '||'
    path = '  '
    monster = '^^'
    chest = '$$'
    board = []
    for num in range(size):
        row1 = [path, path, path, wall, '\n']
        row2 = [wall, monster, path, path, '\n']
        row3 = [path, chest, path, path, '\n']
        row4 = [monster, path, wall, chest, '\n']
        print(row1, row2, row3)
        board.append(row1)
        board.append(row2)
        board.append(row3)
        board.append(row4)
    for row in board:
        print(row)

    print(board[1][0], len(board))

level(1)
