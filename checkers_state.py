@staticmethod
def evaluate_states(self):
    t1 = time.time()
    current_state = Node(deepcopy(self.matrix))

    first_computer_moves = current_state.get_children(True, self.mandatory_jumping)
    if len(first_computer_moves) == 0:
        if self.player_pieces > self.computer_pieces:
            print(
                ansi_yellow + "Computer has no available moves left, and you have more pieces left.\nYOU WIN!" + ansi_reset)
            exit()
        else:
            print(ansi_yellow + "Computer has no available moves left.\nGAME ENDED!" + ansi_reset)
            exit()
    dict = {}
    for i in range(len(first_computer_moves)):
        child = first_computer_moves[i]
        value = Checkers.minimax(child.get_board(), 4, -math.inf, math.inf, False, self.mandatory_jumping)
        dict[value] = child
    if len(dict.keys()) == 0:
        print(ansi_green + "Computer has cornered itself.\nYOU WIN!" + ansi_reset)
        exit()
    new_board = dict[max(dict)].get_board()
    move = dict[max(dict)].move
    self.matrix = new_board
    t2 = time.time()
    diff = t2 - t1
    print("Computer has moved (" + str(move[0]) + "," + str(move[1]) + ") to (" + str(move[2]) + "," + str(
        move[3]) + ").")
    print("It took him " + str(diff) + " seconds.")
