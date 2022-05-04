"""
16439. 치킨치킨치킨 (S3)
https://www.acmicpc.net/problem/16439
"""

import sys

def solution():
    n_member, n_chick = map(int, sys.stdin.readline().split())

    prior_list = []
    for prior in range(n_member):
        prior_list.append(list(map(int, sys.stdin.readline().split())))

    print(n_member, n_chick, prior_list)
    max_chick = 3

solution()