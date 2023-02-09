#rashmitha
def calculate_heuristics(board):
    result = 0
    mine = 0
    opp = 0
    for i in range(8):
        for j in range(8):
            if board[i][j][0] == "w" or board[i][j][0] == "W":
                mine += 1

                if board[i][j][0] == "w":
                    result += 5
                if board[i][j][0] == "W":
                    result += 10
                if i == 0 or j == 0 or i == 7 or j == 7:
                    result += 7
                if i + 1 > 7 or j - 1 < 0 or i - 1 < 0 or j + 1 > 7:
                    continue
                if (board[i + 1][j - 1][0] == "b" or board[i + 1][j - 1][0] == "B") and board[i - 1][
                    j + 1] == " - ":
                    result -= 3
                if (board[i + 1][j + 1][0] == "b" or board[i + 1][j + 1] == "B") and board[i - 1][j - 1] == " - ":
                    result -= 3
                if board[i - 1][j - 1][0] == "B" and board[i + 1][j + 1] == " - ":
                    result -= 3

                if board[i - 1][j + 1][0] == "B" and board[i + 1][j - 1] == " - ":
                    result -= 3
                if i + 2 > 7 or i - 2 < 0:
                    continue
                if (board[i + 1][j - 1][0] == "B" or board[i + 1][j - 1][0] == "b") and board[i + 2][
                    j - 2] == " - ":
                    result += 6
                if i + 2 > 7 or j + 2 > 7:
                    continue
                if (board[i + 1][j + 1][0] == "B" or board[i + 1][j + 1][0] == "b") and board[i + 2][
                    j + 2] == " - ":
                    result += 6

            elif board[i][j][0] == "b" or board[i][j][0] == "B":
                opp += 1

    return result + (mine - opp) * 1000
