"""
24479. 알고리즘 수업 - 깊이 우선 탐색 1 (S2)
https://www.acmicpc.net/problem/24479
"""

import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

def solution():
    # Base input
    N, M, start_v = map(int, sys.stdin.readline().split())

    # graph 생성
    graph = {vertex: [] for vertex in range(1, N+1)}
    visited = [False] * (N + 1)
    nodes_cnt = [0] * (N + 1)
    for _ in range(M):
        v1, v2 = map(int, sys.stdin.readline().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    for i in range(1, N+1):
        graph[i] = sorted(graph[i], reverse=True)

    # stack
    cnt = 1
    stack = deque()
    stack.append(start_v)
    while stack:
        print(stack)
        print(cnt)
        curr = stack.pop()
        visited[curr] = True
        if nodes_cnt[curr] == 0:
            nodes_cnt[curr] = cnt
            cnt += 1
        print(nodes_cnt)
        for next_node in graph[curr]:
            if not visited[next_node]:
                stack.append(next_node)

    for cnt in nodes_cnt[1:]:
        print(cnt)

solution()


def solution2():
    def dfs(graph: dict, visited: list, nodes_cnt: list, curr: int, cnt: int):
        visited[curr] = True
        if nodes_cnt[curr] == 0:
            nodes_cnt[curr] = cnt
        for next_node in graph[curr]:
            if not visited[next_node]:
                cnt = dfs(graph, visited.copy(), nodes_cnt, next_node, cnt + 1)
                return cnt
        return cnt

    # dfs 연산
    dfs(graph, visited, nodes_cnt, start_v, 1)