"""
1927. 최소 힙 (S2)
https://www.acmicpc.net/problem/1927

TC: 
116 ms
"""

def solution():
    import heapq
    import sys

    n = int(sys.stdin.readline())
    heap = []
    for _ in range(n):
        value = int(sys.stdin.readline())
        if value == 0:
            if not heap:
                print(0)
            else:
                print(heapq.heappop(heap))
        else:
            heapq.heappush(heap, value)

solution()