class Maze:
    def __init__(self, filename):

        with open(filename) as f:
            contents = f.read()

        if contents.count("A") != 1:
            raise Exception("Maze must have exactly one start point")

        if contents.count("B") != 1:
            raise Exception("Maze must have exactly one goal")

        self.height = len(contents.splitlines())
        self.width = max(len(line) for line in contents.splitlines())

        self.walls = []

        lines = contents.splitlines()

        for i in range(self.height):
            row = []
            for j in range(self.width):
                char = lines[i][j]
                if char == "A":
                    self.start = (i,j)
                    row.append(False)
                elif char == "B":
                    self.goal = (i,j)
                    row.append(False)

                elif char == "#":
                    row.append(True)

                else :  row.append(False)
            self.walls.append(row);



    def print_maze(self):
        rows = self.height     
        cols = self.width 
        
        for i in range(rows):
            for j in range(cols):

                if (i,j) == self.start :
                    print(" A ",end="")

                elif (i,j) == self.goal:
                    print(" B ",end="")

                elif self.walls[i][j] == True:
                    print(" █ ",end="")
                
                else :
                    print("   ",end="")
            print("")
                



maze = Maze("./Search/maze1.txt");
maze.print_maze();