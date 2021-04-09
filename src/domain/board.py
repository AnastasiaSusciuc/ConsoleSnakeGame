from src.domain.cell import Cell


class Board:

    def __init__(self, dim, empty_value, apples):
        self.dimension = int(dim)
        self.__empty_value = empty_value
        self.__board = self.__create_board()
        self.__snake_head = (0, 0)
        self.__snake_body = []
        self.__apples = int(apples)
        self.__direction = "up"

    @property
    def empty_value(self):
        return self.__empty_value

    @property
    def dim(self):
        return self.dimension

    def get_apples(self):
        return self.__apples

    def get_direction(self):
        return self.__direction

    def get_snake_head(self):
        return self.__snake_head

    def get_snake_body(self):
        return self.__snake_body

    def get_cell_value(self, line, column):
        return self.__board[line][column].value

    def set_snake_body(self, snake):
        self.__snake_body = snake

    def set_snake_head(self, line, column):
        self.__snake_head = (line, column)

    def set_cell_value(self, line, column, value):
        self.__board[line][column].value = value

    def set_direction(self, direction):
        self.__direction = direction

    def __create_board(self):
        """
        this function creates a board
        :return:
        """
        return [[Cell(line, column, self.__empty_value) for column in range(self.dim)]
                for line in range(self.dim)]

    def return_board(self):
        """
        is used for printing the board
        :return: the board
        """
        return self.__board

    def add_body(self, cell):
        """
        adds to the body of the snake a cell
        :param cell: a list of the coordinates of the cell to be added
        :return: -
        """
        self.__snake_body.append(cell)
