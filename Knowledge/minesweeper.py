class Sentence :

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def known_mines(self):

        if len(self.cells) == self.count:
            return self.cells
        
        else :
            return set()
        
    def known_safes(self):

        if self.count == 0:
            return self.cells
        
        else :
            return set()
        
    def mark_mine(self, cell):
        
        if cell in self.cells :
            self.cells.remove(cell)
            self.count -= 1

    def mark_safe(self, cell):

        if cell in self.cells :
            self.cells.remove(cell)


class MinesweeperAI :

    def __init__(self, height = 8, width = 8):

        self.height = height
        self.width = width
        self.moves_made = set()
        self.mines = set()
        self.safes = set()
        self.knowledge = []

    def mark_mine(self, cell):

        self.mines.add(cell)

        for sentence in self.knowledge :
            sentence.mark_mine(cell)


    def mark_safe(self, cell):

        self.safes.add(cell)

        for sentence in self.knowledge :
            sentence.mark_safe(cell)

    def add_knowledge(self,cell, count):

        self.moves_made.add(cell)

        self.mark_safe(cell)

        directions = [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1)]

        neighbours = []

        for neighbour in directions:
            x1, y1 = neighbour
            x2, y2 = cell
            if self.height > x1+x2 >= 0 and self.width > y1+y2 >= 0: 
                new_cell = (x1+x2,y1+y2)

                if new_cell in self.mines :
                    count -= 1

                elif new_cell in self.safes :
                    continue

                else : 
                    neighbours.append(new_cell)


            else :
                continue

        new_sentence = Sentence(neighbours, count)
        self.knowledge.append(new_sentence)
        




        