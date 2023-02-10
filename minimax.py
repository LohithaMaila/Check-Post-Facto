@staticmethod
def minimax(board, depth, alpha, beta, maximizing_player, mandatory_jumping):
    if depth == 0:
        return Checkers.calculate_heuristics(board)
    current_state = Node(deepcopy(board))
    if maximizing_player is True:
        max_eval = -math.inf
        for child in current_state.get_children(True, mandatory_jumping):
            ev = Checkers.minimax(child.get_board(), depth - 1, alpha, beta, False, mandatory_jumping)
            max_eval = max(max_eval, ev)
            alpha = max(alpha, ev)
            if beta <= alpha:
                break
        current_state.set_value(max_eval)
        return max_eval
    else:
        min_eval = math.inf
        for child in current_state.get_children(False, mandatory_jumping):
            ev = Checkers.minimax(child.get_board(), depth - 1, alpha, beta, True, mandatory_jumping)
            min_eval = min(min_eval, ev)
            beta = min(beta, ev)
            if beta <= alpha:
                break
        current_state.set_value(min_eval)
        return min_eval


@staticmethod
def make_a_move(board, old_i, old_j, new_i, new_j, big_letter, queen_row):
    letter = board[old_i][old_j][0]
    i_difference = old_i - new_i
    j_difference = old_j - new_j
    if i_difference == -2 and j_difference == 2:
        board[old_i + 1][old_j - 1] = " - "

    elif i_difference == 2 and j_difference == 2:
        board[old_i - 1][old_j - 1] = " - "

    elif i_difference == 2 and j_difference == -2:
        board[old_i - 1][old_j + 1] = " - "

    elif i_difference == -2 and j_difference == -2:
        board[old_i + 1][old_j + 1] = " - "

    if new_i == queen_row:
        letter = big_letter
    board[old_i][old_j] = " - "
    board[new_i][new_j] = letter + str(new_i) + str(new_j)
