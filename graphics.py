from termcolor import colored
from rock import Rock
from queen import Queen


class Graphics:

    ROCK_TYPE_A = "x"
    ROCK_TYPE_B = "o"
    QUEEN_TYPE_A = "X"
    QUEEN_TYPE_B = "O"

    @classmethod
    def draw(self, grid, highlighted):
        print("    1 2 3 4 5 6 7 8")
        print("  -------------------")

        for i in range(len(grid)):
            radek = str(i + 1) + " |"

            for j in range(len(grid)):
                radek += " "
                if isinstance(grid[i][j], Rock):
                    radek += colored(
                        self.ROCK_TYPE_A if grid[i][j].color else self.ROCK_TYPE_B,
                        "green" if grid[i][j] == highlighted else "white"
                    )
                elif isinstance(grid[i][j], Queen):
                    radek += colored(
                        self.QUEEN_TYPE_A if grid[i][j].color else self.QUEEN_TYPE_B,
                        "green" if grid[i][j] == highlighted else "white"
                    )
                else:
                    radek += " "

            print(radek + " |")
        print("  -------------------")