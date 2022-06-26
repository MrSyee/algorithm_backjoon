"""
1697. 숨바꼭질 (S1)
https://www.acmicpc.net/problem/1697
"""

import sys
from collections import deque


def solution():
    # 입력
    start, target = list(map(int, sys.stdin.readline().split()))

    moved = [start]
    answer = 0
    
    while answer <= 100000:
        tmp = []
        for m in moved:
            tmp.append(m - 1)
            tmp.append(m + 1)
            tmp.append(2 * m)
        answer += 1
        if target in tmp:
            print(answer)
            return

        moved = tmp


import sys
from collections import deque

def solution():
    # 입력
    start, target = list(map(int, sys.stdin.readline().split()))
    visited = [0] * (int(1e6) + 1)

    q = deque([start])
    while q:
        curr = q.popleft()
        if curr == target:
            print(visited[curr])
            return

        for next in [curr - 1, curr + 1, curr * 2]:
            if 0 <= next <= int(1e6) and not visited[next]:
                visited[next] = visited[curr] + 1
                q.append(next)

solution()
