"""
4963. 섬의 개수 (S2)
https://www.acmicpc.net/problem/4963

Grid 탐색하는 dfs 문제 (8방향)
"""

def solution():
    import sys

    sys.setrecursionlimit(10000)

    def dfs(x, y, visited, whole_map):
        visited[y][x] = True
        dx = [1, 1, 0, -1, -1, -1, 0, 1]
        dy = [0, 1, 1, 1, 0, -1, -1, -1]
        for i in range(8):
            tx = x + dx[i]
            ty = y + dy[i]

            if 0 <= tx < w and 0 <= ty < h:
                if visited[ty][tx] == False and whole_map[ty][tx] == 1:
                    dfs(tx, ty, visited, whole_map)

    while True:
        w, h = map(int, sys.stdin.readline().split())
        if w == 0 and h == 0:
            break

        whole_map = list()
        for _ in range(h):
            whole_map.append(list(map(int, sys.stdin.readline().split())))
        visited = [[False] * w for _ in range(h)]

        count = 0
        for y in range(h):
            for x in range(w):
                if visited[y][x] == False and whole_map[y][x] == 1:
                    dfs(x, y, visited, whole_map)
                    count += 1
        print(count)

solution()