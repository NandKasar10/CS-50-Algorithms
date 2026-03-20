paths = {
    'A':['B'],
    'B':['A','D','C'],
    'D':['F'],
    'C':['E'],
    'E':[],
    'F':[],
}

start = 'A'
goal = 'F'

visited = set()
stack = [start]
parent = {start: None}

while stack:
    curr = stack.pop()

    if curr == goal:
        print("Goal Found!")

        path = []
        while curr is not None:
            path.append(curr)
            curr = parent[curr]

        path.reverse()
        print(" -> ".join(path))
        break

    if curr in visited:
        continue

    visited.add(curr)

    for neighbour in reversed(paths[curr]):  # maintain order
        if neighbour not in visited and neighbour not in stack:
            stack.append(neighbour)
            parent[neighbour] = curr

else:
    print("Goal not reachable")