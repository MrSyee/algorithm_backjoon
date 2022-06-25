"""
1388. 바닥 장식 (S3)
https://www.acmicpc.net/problem/1388
"""

import sys

def solution():
    """
    brute force
    """
    N, M = list(map(int, sys.stdin.readline().split()))
    answer = 0
    floor = list()
    for _ in range(N):
        floor.append(sys.stdin.readline().split("\n")[0])
    # print(floor)

    for col_idx in range(N):
        for row_idx in range(M):
            # print(floor[col_idx][row_idx], end="")
            if floor[col_idx][row_idx] == "|" and (col_idx > 0 and floor[col_idx][row_idx] == floor[max(0, col_idx - 1)][row_idx]):
                # print("| same")
                pass
            elif row_idx == 0:
                answer += 1
                # print("row 0")
            elif floor[col_idx][row_idx] == "-" and (row_idx > 0 and floor[col_idx][row_idx] == floor[col_idx][max(0, row_idx - 1)]):
                # print("- same")
                pass
            else:
                # print("none")
                answer += 1
    print(answer)

solution()
