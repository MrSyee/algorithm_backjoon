"""
1463. 1로 만들기 (S3)
https://www.acmicpc.net/problem/1463

TC: 
 ms
"""

import sys
sys.setrecursionlimit(10 ** 6)

def solution(number: int):
    """
    처음에 Greedy 문제로 생각했는데, 예시의 10의 문제로 봤을때 완전 탐색이라 생각이 들어
    재귀를 이용해 완전탐색을 만들어봄.
    최악일때 <=O(3^n?)
    결과는 나오지만 Time over
    """
    def search(x: int, count: int):
        # x == 1
        if x == 1:
            return count

        min_count = float("inf")
        # / 3
        if x % 3 == 0:
            new_x = x // 3
            c = search(new_x, count + 1)
            min_count = min(min_count, c)
        # / 2
        if x % 2 == 0:
            new_x = x // 2
            c = search(new_x, count + 1)
            min_count = min(min_count, c)
        # -1
        new_x =  x - 1
        c = search(new_x, count + 1)
        min_count = min(min_count, c)

        return min_count
    # number = int(input())
    cnt = search(number, 0)
    print(cnt)

solution(10)


def solution2(number: int):
    """
    검색해보니 DP로 푼 예제가 많아 구현과 함께 이해해봄.
    T_C: O(N)
    """
    number = int(input())
    dp = [0] * (number + 1)  # dp[n]: n 을 만들때 필요한 최소 횟수, dp[1]은 1을 만들때 필요한 횟수이므로 0.

    for i in range(2, number + 1):
        # - 1
        dp[i] = dp[i - 1] + 1

        # / 3
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

        # / 2
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)

    print(dp[number])
solution2(10)
