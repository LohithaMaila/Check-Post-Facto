@staticmethod
def find_available_moves(board, mandatory_jumping):
    available_moves = []
    available_jumps = []
    for m in range(8):
        for n in range(8):
            if board[m][n][0] == "w":
                if Checkers.check_moves(board, m, n, m + 1, n + 1):
                    available_moves.append([m, n, m + 1, n + 1])
                if Checkers.check_moves(board, m, n, m + 1, n - 1):
                    available_moves.append([m, n, m + 1, n - 1])
                if Checkers.check_jumps(board, m, n, m + 1, n - 1, m + 2, n - 2):
                    available_jumps.append([m, n, m + 2, n - 2])
                if Checkers.check_jumps(board, m, n, m + 1, n + 1, m + 2, n + 2):
                    available_jumps.append([m, n, m + 2, n + 2])
            elif board[m][n][0] == "W":
                if Checkers.check_moves(board, m, n, m + 1, n + 1):
                    available_moves.append([m, n, m + 1, n + 1])
                if Checkers.check_moves(board, m, n, m + 1, n - 1):
                    available_moves.append([m, n, m + 1, n - 1])
                if Checkers.check_moves(board, m, n, m - 1, n - 1):
                    available_moves.append([m, n, m - 1, n - 1])
                if Checkers.check_moves(board, m, n, m - 1, n + 1):
                    available_moves.append([m, n, m - 1, n + 1])
                if Checkers.check_jumps(board, m, n, m + 1, n - 1, m + 2, n - 2):
                    available_jumps.append([m, n, m + 2, n - 2])
                if Checkers.check_jumps(board, m, n, m - 1, n - 1, m - 2, n - 2):
                    available_jumps.append([m, n, m - 2, n - 2])
                if Checkers.check_jumps(board, m, n, m - 1, n + 1, m - 2, n + 2):
                    available_jumps.append([m, n, m - 2, n + 2])
                if Checkers.check_jumps(board, m, n, m + 1, n + 1, m + 2, n + 2):
                    available_jumps.append([m, n, m + 2, n + 2])
    if mandatory_jumping is False:
        available_jumps.extend(available_moves)
        return available_jumps
    elif mandatory_jumping is True:
        if len(available_jumps) == 0:
            return available_moves
        else:
            return available_jumps
@staticmethod
def find_player_available_moves(board, mandatory_jumping):
        available_moves = []
        available_jumps = []
        for m in range(8):
            for n in range(8):
                if board[m][n][0] == "b":
                    if Checkers.check_player_moves(board, m, n, m - 1, n - 1):
                        available_moves.append([m, n, m - 1, n - 1])
                    if Checkers.check_player_moves(board, m, n, m - 1, n + 1):
                        available_moves.append([m, n, m - 1, n + 1])
                    if Checkers.check_player_jumps(board, m, n, m - 1, n - 1, m - 2, n - 2):
                        available_jumps.append([m, n, m - 2, n - 2])
                    if Checkers.check_player_jumps(board, m, n, m - 1, n + 1, m - 2, n + 2):
                        available_jumps.append([m, n, m - 2, n + 2])
                elif board[m][n][0] == "B":
                    if Checkers.check_player_moves(board, m, n, m - 1, n - 1):
                        available_moves.append([m, n, m - 1, n - 1])
                    if Checkers.check_player_moves(board, m, n, m - 1, n + 1):
                        available_moves.append([m, n, m - 1, n + 1])
                    if Checkers.check_player_jumps(board, m, n, m - 1, n - 1, m - 2, n - 2):
                        available_jumps.append([m, n, m - 2, n - 2])
                    if Checkers.check_player_jumps(board, m, n, m - 1, n + 1, m - 2, n + 2):
                        available_jumps.append([m, n, m - 2, n + 2])
                    if Checkers.check_player_moves(board, m, n, m + 1, n - 1):
                        available_moves.append([m, n, m + 1, n - 1])
                    if Checkers.check_player_jumps(board, m, n, m + 1, n - 1, m + 2, n - 2):
                        available_jumps.append([m, n, m + 2, n - 2])
                    if Checkers.check_player_moves(board, m, n, m + 1, n + 1):
                        available_moves.append([m, n, m + 1, n + 1])
                    if Checkers.check_player_jumps(board, m, n, m + 1, n + 1, m + 2, n + 2):
                        available_jumps.append([m, n, m + 2, n + 2])
        if mandatory_jumping is False:
            available_jumps.extend(available_moves)
            return available_jumps
        elif mandatory_jumping is True:
            if len(available_jumps) == 0:
                return available_moves
            else:
                return available_jumps
