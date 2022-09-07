from termcolor import colored
from rock import Rock
from queen import Queen

class Graphics:

    ROCK_TYPE_A = "x"
    ROCK_TYPE_B = "o"
    QUEEN_TYPE_A = "x̄"
    QUEEN_TYPE_B = "Ø"

    @classmethod
    def draw(self, grid, highlighted, possible_moves):
        print("    a b c d e f g h")
        print("  -------------------")

        for i in range(len(grid)):
            radek = str(i + 1) + " |"

            for j in range(len(grid)):
                radek += " "
                if isinstance(grid[i][j], Rock):
                    radek += colored(
                        self.ROCK_TYPE_A if grid[i][j]._color else self.ROCK_TYPE_B,
                        "green" if grid[i][j] == highlighted else "yellow" if (i, j) in possible_moves and not highlighted else "white"
                    )
                elif isinstance(grid[i][j], Queen):
                    radek += colored(
                        self.QUEEN_TYPE_A if grid[i][j]._color else self.QUEEN_TYPE_B,
                        "green" if grid[i][j] == highlighted else "yellow" if (i, j) in possible_moves and not highlighted else "white"
                    )
                
                elif (i + j + 1) % 2 == 1:
                    radek += "·"
                else:
                    radek += " "

            print(radek + " |")
        print("  -------------------")
        print("    a b c d e f g h")