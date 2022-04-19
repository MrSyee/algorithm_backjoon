def solution(n_note: int, first_note: int, interval: int, notes: list):
    """
    16162. 3단 고음 (S4)
    https://www.acmicpc.net/problem/16162

    TC: O(n_note)
    """
    # n_note, first_note, interval = list(map(int, input().split()))
    # notes = list(map(int, input().split()))
    sol = 0
    for note in notes:
        if note == first_note:
            first_note += interval
            sol += 1
    print(sol)

solution(3, 1, 2, [1, 3, 5]) # 3
solution(3, 1, 2, [3, 1, 5]) # 1
solution(7, 3, 3, [3, 3, 9, 7, 2, 6, 9]) # 3