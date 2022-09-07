from figure import Figure

class Queen(Figure):

    def __init__(self, color):
        super().__init__(color)

    def move_is_valid(self, position, board, current_position=None):
        (x, y) = position
        (current_x, current_y) = current_position if current_position else self.get_position(board)
        
        # když (i + j) % 2 == 0
        if not (x + y) % 2 == 0: return "Táhni jenom na bílý políčka"

        if abs(x - current_x) != abs(y - current_y): return "Mimo dosah"

        # když na poli není figurka
        if board[x][y] != None: return "Na poli už se nachází figura" 
        
        print(current_position)
        print(x, y)
        print(x-current_x, y-current_y)
        # vrací 2 pro rozpoznání možnosti skákání
        (dir_x, dir_y) = (int((x-current_x)/abs(x-current_x)), int((y-current_y)/abs(y-current_y)))
        position_x = current_x + dir_x
        position_y = current_y + dir_y
        jump_count = 0
        while position_x != x:
            if board[position_x][position_y]:
                jump_count += 1
            position_x += dir_x
            position_y += dir_y
        
        if not jump_count:
            return 1
        elif jump_count == 1:
            return 2
        else:
            return "Nemůžeš přeskočit více figurek najednou"