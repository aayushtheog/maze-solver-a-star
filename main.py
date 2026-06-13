import heapq

maze = [
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar():
    rows = len(maze)
    cols = len(maze[0])

    pq = []
    heapq.heappush(pq, (0, start))

    came_from = {}
    g_score = {start: 0}

    while pq:
        _, current = heapq.heappop(pq)

        if current == goal:
            path = []

            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)
            path.reverse()

            return path

        x, y = current

        for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0:

                temp_g = g_score[current] + 1

                if (nx, ny) not in g_score or temp_g < g_score[(nx, ny)]:

                    g_score[(nx, ny)] = temp_g

                    f_score = temp_g + heuristic((nx, ny), goal)

                    heapq.heappush(pq, (f_score, (nx, ny)))

                    came_from[(nx, ny)] = current

    return None

path = astar()

if path:
    print("Shortest Path Found:")
    print(path)
else:
    print("No Path Found")