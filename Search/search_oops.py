import sys

class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier:
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        else:
            return self.frontier.pop()
        
class QueueFrontier( StackFrontier ):

    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        else:
            return self.frontier.pop(0)

paths = {
    'A':['B','C'],
    'B':['D'],
    'C':['E'],
    'D':['E'],
    'E':['F'],
    'F':[]
}

frontier = QueueFrontier()

start = Node('A',None,None)

frontier.add(start)

explored = set()

goal_state = 'F'

while True:

    if frontier.empty():
        print("No solution !")
        break

    node = frontier.remove()

    if(node.state == goal_state):
        path = []
        while(node):
            path.append(node.state)
            node = node.parent

        path.reverse()
        print(" -> ".join(path))
        break

    explored.add(node.state)

    for neighbour in reversed(paths[node.state]):

        if (neighbour in explored) or (frontier.contains_state(neighbour)) : continue
        temp_node = Node(neighbour,node,None)
        frontier.add(temp_node)

    
        



