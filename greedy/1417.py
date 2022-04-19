"""
1417. 국회의원 선거 (S5)
https://www.acmicpc.net/problem/1417

TC: O(N * result)
72 ms
"""

def solution(N, cands):
    import sys

    N = int(sys.stdin.readline())
    cands = []
    for _ in range(N):
        cands.append(int(sys.stdin.readline()))

    cnt = 0
    other_cands = sorted(cands[1:], reverse=True)
    if len(cands) == 1:
        print(0)
        sys.exit(0)

    while cands[0] <= other_cands[0]:
        other_cands[0] -= 1
        cands[0] += 1
        cnt += 1
        
        other_cands = sorted(other_cands, reverse=True)

    print(cnt)
    
solution(3, [5, 7, 7])