import string


class Grid:

    def __init__(self, size):
      self._array = [[None for j in range(size)] for i in range(size)]
      self.fill_in_figures()

    # def draw(self):
    #   for i in range(2 * len(self._array)):
    #     if i % 2 == 0:
    #       print("---------------------------------")
    #     else:
    #       radek = "|"
    #       for j in range(len(self._array)):
    #         radek += " . |"
    #       print(radek)
    #   print("---------------------------------")

    def draw(self, figures):
      print("    1 2 3 4 5 6 7 8")
      print("  -------------------")
      for i in range(len(self._array)):
        radek = str(i + 1) + " |"
        for j in range(len(self._array)):
          if (i, j) in map(lambda f: f["location"], figures):
            figure_color = list(filter(lambda f: f["location"] == (i, j), figures))[0]["color"]
            radek += " " + ("x" if figure_color == 0 else "o")
          else:
            radek += "  "
        print(radek + " |")
      print("  -------------------")

    def fill_in_figures(self):
      self._array[3][5] = "x"