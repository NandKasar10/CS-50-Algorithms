from collections import deque


grid = [
    [0,1,0],
    [0,0,1],
    [1,0,0]
]

rows = len(grid)
cols = len(grid[0])

queue = deque([(0,0)])

actions = [(0,1),(1,0),(0,-1),(-1,0)]

visited = set()

parent = {(0,0):None}

path = []

while queue:
    r, c = queue.popleft()

    if (r,c) in visited: continue

    visited.add((r,c))

    if(r==2) and (c==2):
        while(parent[(r,c)]):
            path.append((r,c))
            r,c = parent[r,c]
        path.append((0,0))
        break

    for direction in actions :
        r1, c1 = direction
        new_state = (r+r1,c+c1)
        if(r+r1<0) or (c+c1<0) or (r+r1>=rows) or (c+c1>=cols) : continue
        
        if(grid[r+r1][c+c1] == 1) : continue

        if new_state not in visited:
            queue.append(new_state)
            parent[new_state] = (r,c)


path.reverse()
print(path)

    

