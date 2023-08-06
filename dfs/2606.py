"""
2606. 바이러스 (S3)
https://www.acmicpc.net/problem/2606

graph 사용하여 dfs 구현하는 기본 문제
"""

def solution():
    import sys
    sys.setrecursionlimit(10000)

    n_coms = int(sys.stdin.readline())
    n_nodes = int(sys.stdin.readline())

    graph = {i+1: [] for i in range(n_coms)}
    for _ in range(n_nodes):
        n, m = map(int, sys.stdin.readline().split())
        graph[n].append(m)
        graph[m].append(n)

    start = 1
    visited = []
    def dfs(curr_com, count, start):
        for next_com in graph[curr_com]:
            if next_com not in visited and next_com != start:
                visited.append(next_com)
                count = dfs(next_com, count + 1, start)
        return count

    count = dfs(start, 0, start)
    print(count)

solution()