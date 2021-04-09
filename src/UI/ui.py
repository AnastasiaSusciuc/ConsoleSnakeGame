import texttable


class UI:

    def __init__(self, service):
        self.__service = service
        self.done = 0

    def print_board(self):
        """
        prints the board in a user friendly manner, using text table library
        :return:
        """
        board = self.__service.draw_board()

        dim = self.__service.get_dimension()
        table = texttable.Texttable(0)
        table.set_cols_align(dim*["c"])
        table.set_cols_dtype(dim*["a"])

        tab = []
        dim_list = []
        for i in range(dim):
            dim_list.append(i)
        tab.append(dim_list)
        for i in range(dim):
            line = []
            for j in range(dim):
                line.append(board[i][j].value)
            tab.append(line)

        table.add_rows(tab)

        print(table.draw())

    def __place_snake(self):
        """
        places the snake on the board
        :return: -
        """
        self.__service.place_initial_snake()

    def __place_apples(self):
        """
        places the apples on the board
        :return: -
        """
        self.__service.place_initial_apples()

    def move(self, *args):
        """
        moves the snake
        :param args: the number of cells to move the snake
        :return: -
        """
        try:
            self.__service.move_snake(*args)
            self.print_board()
        except ValueError as ve:
            print(ve)
            self.done = 1

    def switch_dir(self, direction):
        """
        switches the direction of the snake
        :param direction: the new direction
        :return:
        """
        try:
            self.__service.switch(direction)
            self.print_board()
        except ValueError as ve:
            print(ve)

    def play(self):
        """
        starts the play
        :return: -
        """
        directions = ["up", "right", "down", "left"]
        while self.done == 0:
            cmd = input("insert your command:")
            cmd = cmd.strip()
            cmd = cmd.split()
            if cmd[0] == "move":
                if len(cmd) == 1:
                    self.move()
                elif len(cmd) == 2:
                    try:
                        self.move(cmd[1])
                    except ValueError:
                        print("Invalid command! the second number should be a positive integer")
                else:
                    print("Invalid command!")
            elif cmd[0].lower() in directions:
                self.switch_dir(cmd[0].lower())
            else:
                print("Invalid command!")

    def run(self):
        """
        starts the program
        :return: -
        """
        self.__place_snake()
        self.__place_apples()
        self.print_board()
        while True:
            cmd = input("type 'start' to start the game?")
            if cmd == "start":
                self.play()
                break
