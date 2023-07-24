"""
2303. 숫자 게임 (S5)
https://www.acmicpc.net/problem/2303
"""

import sys

def solution():
    """
    44 ms.
    """
    n_people = int(sys.stdin.readline())
    numbers_list = []
    for _ in range(n_people):
        numbers_list.append(list(map(int, sys.stdin.readline().split())))
    # print(n_people)
    # print(numbers_list)

    def find_max_sum(numbers: list):
        max_sum = 0
        for i in range(len(numbers) - 2):
            for j in range(i + 1, len(numbers) - 1):
                for k in range(j + 1, len(numbers)):
                    # print("i,j,k", i,j,k, "sum", (numbers[i] + numbers[j] + numbers[k]) % 10, "max_sum", max_sum)
                    max_sum = max(max_sum, (numbers[i] + numbers[j] + numbers[k]) % 10)
        return max_sum

    max_sums = []
    for numbers in numbers_list:
        max_sums.append(find_max_sum(numbers))

    largest = max(max_sums)
    for ind, m_s in enumerate(max_sums[::-1]):
        if m_s == largest:
            winner = n_people - ind
            break
    return winner

# print(solution())


from itertools import combinations

def solution2():
    """
    3중 for문을 combination으로 변경해봄.
    """
    n_people = int(sys.stdin.readline())
    numbers_list = []
    for _ in range(n_people):
        numbers_list.append(list(map(int, sys.stdin.readline().split())))

    def find_max_sum(numbers: list):
        max_sum = 0
        for comb in combinations(numbers, 3):
            max_sum = max(max_sum, sum(comb) % 10)
        return max_sum

    largest = 0
    winner = 0
    for person, numbers in enumerate(numbers_list):
        max_sum = find_max_sum(numbers)
        if largest <= max_sum:
            largest = max_sum
            winner = person + 1
    return winner

print(solution2())
