"""
1012. 유기농 배추 (S2)
https://www.acmicpc.net/problem/1012

Grid 탐색하는 dfs 문제 (4방향)
"""

def solution():
    import sys

    sys.setrecursionlimit(10000)


    def dfs(x, y, max_x, max_y, visited, whole_map):
        visited[y][x] = True
        dx = [1, 0, 0, -1]
        dy = [0, 1, -1, 0]

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if 0 <= tx < max_x and 0 <= ty < max_y:
                if visited[ty][tx] == False and whole_map[ty][tx] == 1:
                    dfs(tx, ty, max_x, max_y, visited, whole_map)

    n_test = int(sys.stdin.readline())

    for _ in range(n_test):
        W, H, K = list(map(int, sys.stdin.readline().split()))

        # 배추밭
        field = []
        for _ in range(H):
            field.append([0] * W)

        # 배추 위치
        for _ in range(K):
            x, y = list(map(int, sys.stdin.readline().split()))
            field[y][x] = 1
        visited = [[False] * W for _ in range(H)]

        # 인접 배추 탐색
        n_worms = 0
        for y in range(H):
            for x in range(W):
                if visited[y][x] == False and field[y][x] == 1:
                    dfs(x, y, W, H, visited, field)
                    n_worms += 1
        print(n_worms)

solution()