"""
1388. 점프 점프 (S2)
https://www.acmicpc.net/problem/14248
"""

import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)

def solution():
    # 입력
    n = int(sys.stdin.readline())
    stones = list(map(int, sys.stdin.readline().split()))
    start = int(sys.stdin.readline())
    start_idx = start - 1

    # 방문 가능 graph 생성
    graph = defaultdict(list)
    for idx, stone in enumerate(stones):
        # 왼쪽
        if idx - stone > -1:
            graph[idx].append(idx - stone)

        # 오른쪽
        if idx + stone < n:
            graph[idx].append(idx + stone)
    
    visited = [start_idx]
    
    def dfs(graph, start, visited):
        if not graph[start]:
            return
        
        for next in graph[start]:
            if next not in visited:
                dfs(graph, next, visited)
                visited.append(next)
        return
    dfs(graph, start_idx, visited)
    print(len(visited))

solution()
