
grid = [
    [0,1,0],
    [0,0,1],
    [1,0,0]
]

rows = len(grid)
cols = len(grid[0])

stack = [(0,0)]

actions = [(0,1),(1,0),(0,-1),(-1,0)]

visited = set()

path = []

while stack:
    r, c = stack.pop(0)

    if (r,c) in visited: continue

    visited.add((r,c))
    path.append((r,c))

    for direction in actions :
        r1, c1 = direction
        new_state = (r+r1,c+c1)
        if(r+r1<0) or (c+c1<0) or (r+r1>=rows) or (c+c1>=cols) : continue
        
        if(grid[r+r1][c+c1] == 1) : continue

        if new_state not in visited:
            stack.append(new_state)


print(path)
    

