import csv
from queen import Queen
from rock import Rock

class FileLoader:

    def __init__(self, filename):
        self.filename = filename
        self.columns = {"a": 0,"b": 1,"c": 2,"d": 3,"e": 4,"f": 5, "g": 6,"h": 7}
        self.colors = {"w": 0, "ww": 1, "b": 2, "bb": 3}

    def index_of(self, dict, value):
        return list(dict.keys())[list(dict.values()).index(value)]

    def load_game(self):
        with open(self.filename, "r") as file:
            reader = csv.DictReader(file, delimiter=",")

            figures = []
            for row in reader:
                if row["position"].strip() == "" or row["rank_color"].strip() == "":
                    continue

                if (
                    row["position"][0] not in self.columns.keys() or
                    row["rank_color"] not in self.colors.keys() or
                    len(row["position"]) > 2 or
                    not 0 <= (int(row["position"][1]) - 1) < 8 or
                    (self.columns[row["position"][0]] + (int(row["position"][1]) - 1)) % 2 != 0 or
                    len([
                        figure for figure in figures
                        if figure[0] == (int(row["position"][1]) - 1) and figure[1] == self.columns[row["position"][0]]
                    ]) > 0                   
                ):
                    raise Exception("Špatný formát souboru k načtení")

                figures.append((int(row["position"][1]) - 1, self.columns[row["position"][0]],self.colors[row["rank_color"]]))
        return figures

    def save_game(self, board):

        with open(self.filename, "w") as file:
            writer = csv.DictWriter(file, delimiter=",", fieldnames=["position" ,"rank_color"], lineterminator="\n")
            writer.writeheader()
            for i in range(len(board)):
                for j in range(len(board)):
                    if board[i][j] != None:
                        type = "w" if board[i][j]._color == 0 else "b"
                        if isinstance(board[i][j], Queen):
                            type += type
                        writer.writerow({"position": self.index_of(self.columns, j) + str(i+1), "rank_color": type})