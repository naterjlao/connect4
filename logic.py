WINNING_COMBO = 4

class Players:
    # TODO replace with color hex
    EMPTY = 0
    RED = 1
    BLUE = -1

class Board:
    HEIGHT = 6
    WIDTH = 7

    def __init__(self):
        self.board = [[Players.EMPTY] * Board.WIDTH for _ in range(0, Board.HEIGHT)]
        self.players = {}

    def winner(self):
        """
        @brief Returns the winner of the board, None if there is no winner.
        """
        pos_add = lambda a, b: (a[0] + b[0], a[1] + b[1])
        occupied = list(self.players.keys())
        winning_board = False
        idx = 0
        while (not winning_board and idx < len(occupied)):
            origin = occupied[idx]
            player = self.players[origin]

            # Check Left
            if not winning_board:
                winning_board = True
                displace = 1
                while (winning_board and displace < WINNING_COMBO):
                    displacement = pos_add(origin, (0,-displace))
                    winning_board = winning_board and (displacement in self.players) and (self.players[displacement] == player)
                    displace += 1

            # Check Right
            if not winning_board:
                winning_board = True
                displace = 1
                while (winning_board and displace < WINNING_COMBO):
                    displacement = pos_add(origin, (0,displace))
                    winning_board = winning_board and (displacement in self.players) and (self.players[displacement] == player)
                    displace += 1

            # Check Up
            if not winning_board:
                winning_board = True
                displace = 1
                while (winning_board and displace < WINNING_COMBO):
                    displacement = pos_add(origin, (-displace,0))
                    winning_board = winning_board and (displacement in self.players) and (self.players[displacement] == player)
                    displace += 1

            # Check Diagonal Right
            if not winning_board:
                winning_board = True
                displace = 1
                while (winning_board and displace < WINNING_COMBO):
                    displacement = pos_add(origin, (displace,displace))
                    winning_board = winning_board and (displacement in self.players) and (self.players[displacement] == player)
                    displace += 1

            # Check Diagonal Left
            if not winning_board:
                winning_board = True
                displace = 1
                while (winning_board and displace < WINNING_COMBO):
                    displacement = pos_add(origin, (-displace,-displace))
                    winning_board = winning_board and (displacement in self.players) and (self.players[displacement] == player)
                    displace += 1
            
            idx += 1
        if winning_board:
            return player
        else:
            return None
        

    def move(self,player:Players,col):
        if player != Players.RED and player != Players.BLUE:
            raise ValueError(f"Invalid player: {player}")
        elif col < 0 or col >= Board.WIDTH:
            raise ValueError(f"Invalid column selection: {col}")
        elif self.board[0][col] != Players.EMPTY:
            raise ValueError(f"Column {col} already filled")
        else:
            row = Board.HEIGHT - 1
            while (self.board[row][col] != Players.EMPTY):
                row -= 1
            self.board[row][col] = player
            self.players[(row,col)] = player


    def __str__(self):
        retval = ""
        for row in range(0,Board.HEIGHT):
            retval += "|"
            for col in range(0,Board.WIDTH):
                pos = self.board[row][col]
                if pos != Players.EMPTY:
                    retval += "R" if pos == Players.RED else "B"
                else:
                    retval += " "
                retval += "|"
            retval += "\n"
        for idx in range(0,Board.WIDTH):
            retval += f" {idx+1}"
        return retval


if __name__ == "__main__":
    print("CONNECT-4 CLI")
    board = Board()
    turn = Players.RED
    winner = None
    while (winner == None):
        print(board)
        move = int(input(f"Player {'RED' if turn == Players.RED else 'BLUE'}'s turn:")) - 1
        board.move(turn, move)
        winner = board.winner()
        turn = Players.RED if turn == Players.BLUE else Players.BLUE
    print(board)
    print(f"Winner: {'RED' if winner == Players.RED else 'BLUE'}")
    # TODO no stalemate case