import random
import copy


class Service:
    def __init__(self, board):
        self.__board = board

    def place_initial_snake(self):
        """
        places the initial snake on the middle of the board
        :return: -
        """
        middle = self.__board.dimension // 2
        self.__board.set_cell_value(middle, middle, "+")
        self.__board.set_cell_value(middle+1, middle, "+")
        self.__board.set_cell_value(middle-1, middle, "*")
        self.__board.set_snake_head(middle-1, middle)
        self.__board.add_body([middle, middle])
        self.__board.add_body([middle+1, middle])

    def draw_board(self):
        """
        :return: the board for the UI to print
        """
        return self.__board.return_board()

    def get_dimension(self):
        """
        :return: the dimension of the board
        """
        return self.__board.dim

    def valid_location(self, lin, col):
        """
        checks if a position is valid to place an apple
        :param lin: a line pos int
        :param col: a col, pos int
        :return: True if the position is valid, False, otherwise
        """
        dx = [-1, 1, 0, 0]
        dy = [ 0, 0,-1, 1]
        for i in range(4):
            new_line = lin+dx[i]
            new_col = col + dy[i]
            if 0 <= new_col < self.__board.dim and 0 <= new_line < self.__board.dim:
                if self.__board.get_cell_value(new_line, new_col) != 0:
                    return False
        return True

    def place_initial_apples(self):
        """
        places randomly the apples at the start of the game
        :return: -
        """
        apples = self.__board.get_apples()
        board_dim = self.__board.dim
        while apples > 0:
            lin = random.randint(0, board_dim-1)
            col = random.randint(0, board_dim-1)

            if self.__board.get_cell_value(lin, col) == 0 and self.valid_location(lin, col) == True:
                self.__board.set_cell_value(lin, col, ".")
                apples = apples-1

    def add_apple(self):
        """
        adds an apple on the board
        :return: -
        """
        board_dim = self.__board.dim
        while True:
            lin = random.randint(0, board_dim - 1)
            col = random.randint(0, board_dim - 1)

            if self.__board.get_cell_value(lin, col) == 0 and self.valid_location(lin, col) == True:
                self.__board.set_cell_value(lin, col, ".")
                break

    def make_a_move(self, dirx, diry):
        """
        the head of the snake will be move a position forward, like all his body pieces
        if an apple was eaten, the the length of the snakes increases by one
        :param dirx: the coordinate x of the direction the snakes moves to
        :param diry: the coordinate y of the direction the snakes moves to
        :return: -
        raises ValueError if the snake made an invalid move
        """
        snake_head = self.__board.get_snake_head()
        snake_body = self.__board.get_snake_body()

        found_apple = 0

        # print("Snake head", snake_head)
        # print("Snake body", snake_body)

        if snake_head[0] + dirx < 0 or snake_head[0] + dirx >= self.__board.dim :
            raise ValueError("Game over! you hit a wall")
        if snake_head[1] + diry < 0 or snake_head[1] + diry >= self.__board.dim :
            raise ValueError("Game over! you hit a wall")

        if self.__board.get_cell_value(snake_head[0] + dirx, snake_head[1] + diry) == "+":
            raise ValueError("Game over! You ate yourself, iuuuuuu")

        old_snake_head = snake_head
        snake_head = (snake_head[0] + dirx, snake_head[1] + diry)

        if self.__board.get_cell_value(snake_head[0], snake_head[1]) == ".":
            found_apple = 1

        self.__board.set_snake_head(snake_head[0], snake_head[1])
        self.__board.set_cell_value(snake_head[0], snake_head[1], "*")

        copy_snake_body = copy.deepcopy(snake_body)
        last_cell = copy_snake_body[-1]

        self.__board.set_cell_value(last_cell[0], last_cell[1], 0)

        for i in range(len(snake_body)-1, 0, -1):
            # print("OLD", snake_body[i], "New", snake_body[i-1])
            snake_body[i] = snake_body[i - 1]

        # for i in range(0, len(snake_body)-1):
        #     snake_body[i] = snake_body[i-1]

        snake_body[0] = [old_snake_head[0], old_snake_head[1]]
        self.__board.set_cell_value(old_snake_head[0], old_snake_head[1], "+")

        self.__board.set_snake_body(snake_body)

        if found_apple == 1:
            self.__board.add_body(last_cell)
            self.__board.set_cell_value(last_cell[0], last_cell[1], "+")
            self.add_apple()

        # print("Found apple", found_apple)
        # snake_head = self.__board.get_snake_head()
        # snake_body = self.__board.get_snake_body()
        # print("new Snake head", snake_head)
        # print("new Snake body", snake_body)

    def switch(self, direction):
        """
        switches the direction of the snake, ie sets the direction of the board to direction
        :param direction: is one of "up", "right", "down", "left"
        :return: -
        raises ValueErrors if this switch would mean a 180 degrees switch
        """
        old_dir = self.__board.get_direction()
        if old_dir == direction:
            return

        if old_dir == "up" and direction == "down":
            raise ValueError("Invalid direction!")

        if old_dir == "down" and direction == "up":
            raise ValueError("Invalid direction!")

        if old_dir == "right" and direction == "left":
            raise ValueError("Invalid direction!")

        if old_dir == "left" and direction == "right":
            raise ValueError("Invalid direction!")

        self.__board.set_direction(direction)

        if direction == "up":
            self.make_a_move(-1, 0)
        elif direction == "right":
            self.make_a_move(0, 1)
        elif direction == "left":
            self.make_a_move(0, -1)
        elif direction == "down":
            self.make_a_move(1, 0)

    def move_snake(self, *args):
        """
        moves the snakes args positions
        :param args: the  number of position the snake has to move
        :return:
        """
        number_moves = 1

        if len(args) != 0:
            number_moves = int(args[0])

        while number_moves > 0:
            direction = self.__board.get_direction()
            if direction == "up":
                # print("UP")
                self.make_a_move(-1, 0)
            elif direction == "right":
                self.make_a_move(0, 1)
            elif direction == "left":
                self.make_a_move(0, -1)
            elif direction == "down":
                self.make_a_move(1, 0)

            number_moves = number_moves-1
