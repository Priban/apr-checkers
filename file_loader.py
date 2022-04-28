import csv


class FileLoader:

    def __init__(self, filename):
        self.filename = filename
        self.columns = {"a": 1,"b": 2,"c": 3,"d": 4,"e": 5,"f": 6, "g": 7,"h": 8}
        self.colors = {"w": 0, "b": 1}

    def index_of(self, dict, value):
        return list(dict.keys())[list(dict.values()).index(value)]

    def load_game(self):

        with open(self.filename, "r") as file:
            reader = csv.DictReader(file, delimiter=",")

            figures = []
            for row in reader:
                figures.append((int(row["position"][1]) - 1,self.columns[row["position"][0]] - 1,self.colors[row["rank_color"]]))
        return figures

    def save_game(self, board):

        with open(self.filename, "w") as file:
            writer = csv.DictWriter(file, delimiter=",", fieldnames=["position" ,"rank_color"], lineterminator="\n")
            writer.writeheader()
            for i in range(len(board)):
                for j in range(len(board)):
                    if board[i][j] != None:
                        writer.writerow({"position": self.index_of(self.columns, j+1) + str(i+1), "rank_color": self.index_of(self.colors, board[i][j]._color)})