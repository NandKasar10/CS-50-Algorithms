from search_oops import QueueFrontier, Node, StackFrontier
from PIL import Image, ImageDraw


class Maze:
    def __init__(self, filename):

        self.solution = None

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
                    print("███",end="")

                elif self.solution and (i, j) in self.solution:
                    print(" + ", end="")
                
                else :
                    print("   ",end="")
            print("")

    def neighbors(self, state):
        row, col = state

        candidates = [
            (row-1, col),
            (row+1, col),
            (row, col-1),
            (row, col+1)
        ]

        result = []

        for r, c in candidates:
            if 0 <= r < self.height and 0 <= c < self.width:
                if not self.walls[r][c]:
                    result.append((r, c))

        return result
                
    def solve(self):

        start = Node(self.start, None, None)
        frontier = QueueFrontier()
        frontier.add(start)

        explored = set()

        while True:

            if frontier.empty():
                raise Exception("No solution")

            node = frontier.remove()

            if node.state == self.goal:
                path = []
                while node and node.parent:
                    path.append(node.state)
                    node = node.parent
                path.reverse()
                self.solution = path

                break

            explored.add(node.state)

            for state in self.neighbors(node.state):
                if state not in explored and not frontier.contains_state(state):
                    child = Node(state, node, None)
                    frontier.add(child)


    def output_image(self, filename, show_solution=True):

        cell_size = 80
        cell_border = 2

        # create blank image
        img = Image.new(
            "RGB",
            (self.width * cell_size, self.height * cell_size),
            "black"
        )

        draw = ImageDraw.Draw(img)

        for i in range(self.height):
            for j in range(self.width):

                # decide color
                if self.walls[i][j]:
                    fill = (40, 40, 40)  # wall

                elif (i, j) == self.start:
                    fill = (255, 0, 0)   # start (red)

                elif (i, j) == self.goal:
                    fill = (0, 255, 0)   # goal (green)

                elif show_solution and self.solution and (i, j) in self.solution:
                    fill = (220, 235, 113)  # path (yellow)

                else:
                    fill = (237, 240, 252)  # empty

                # draw rectangle
                draw.rectangle(
                    [
                        (j * cell_size + cell_border, i * cell_size + cell_border),
                        ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border)
                    ],
                    fill=fill
                )

        img.save(filename)


maze = Maze("./maze1.txt");
maze.solve();
maze.print_maze();
maze.output_image("maze.png");