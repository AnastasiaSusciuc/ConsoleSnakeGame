from src.UI.ui import UI
from src.domain.board import Board
from src.service.service import Service


class Manager:

    def __init__(self):
        self.__text = "settings.txt"
        self.__dim = 0
        self.__apples = 0

    def create_empty_file(self):
        """
        if the file is not created it will be created
        :return:
        """
        file = open(self.__text, "w")
        file.write("")
        file.close()

    def read_settings_from_file(self):
        """
        reads the settings from the file
        :return: -
        """
        try:
            with open(self.__text, "r") as f:
                lines = f.readlines()
                for line in lines:
                    line = line.strip()
                    line = line.split()
                    self.__dim = line[0]
                    self.__apples = line[1]

        except FileNotFoundError:
            self.create_empty_file()

    def run(self):
        """
        builds the entities and
        starts the programme
        :return:-
        """
        self.read_settings_from_file()
        board = Board(self.__dim, 0, self.__apples)
        service = Service(board)
        ui = UI(service)
        ui.run()
