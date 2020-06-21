def winCheck(tileList, lastMoveIndex):
    values = [[tile.value for tile in tileList[:3]],
              [tile.value for tile in tileList[3:6]],
              [tile.value for tile in tileList[6:9]]]
    index = (lastMoveIndex // 3, lastMoveIndex % 3)

    ## Check for horizontal win
    if values[index[0]][0] == values[index[0]][1] and values[index[0]][0] == values[index[0]][2]:
        return True

    ## Check for vertical win
    if values[0][index[1]] == values[1][index[1]] and values[1][index[1]] == values[2][index[1]]:
        return True

    ## Check for diagonal win
    if (index[0] + index[1]) % 2 == 0:
        if index[0] != index[1]:
            if values[2][0] == values[1][1] and values[1][1] == values[0][2]:
                return True
        elif index[0] == index[1] and index[1] != 1:
            if values[0][0] == values[1][1] and values[1][1] == values[2][2]:
                return True
        else:
            if values[0][0] == values[1][1] and values[1][1] == values[2][2]:
                return True
            if values[2][0] == values[1][1] and values[1][1] == values[0][2]:
                return True
