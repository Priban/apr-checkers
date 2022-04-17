class Graphics:

  ROCK_TYPE_A = "x"
  ROCK_TYPE_B = "o"
  QUEEN_TYPE_A = "X"
  QUEEN_TYPE_B = "O"

  @staticmethod
  def draw(grid):
    print("    1 2 3 4 5 6 7 8")
    print("  -------------------")

    for i in range(len(grid)):
      radek = str(i + 1) + " |"

      for j in range(len(grid)):
        print(type(grid[i][j]))
                # if (i, j) in map(lambda f: f["location"], figures):
                #   figure_color = list(filter(lambda f: f["location"] == (i, j), figures))[0]["color"]
                #   radek += " " + ("x" if figure_color == 0 else "o")
                # else:
                #   radek += "  "

      print(radek + " |")

    print("  -------------------")
