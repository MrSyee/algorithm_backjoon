def solution(n: int, k: int, weight_list: list):
    """
    18429. 근손실 (S3)
    https://www.acmicpc.net/problem/18429

    TC: 
    116 ms
    """
    # n, k = list(map(int, input().split()))
    # weight_list = list(map(int, input().split()))

    def backtracking(reduce, kit_index, kit_list, target_weight) -> int:
        weight = kit_list.pop(kit_index)
        target_weight = target_weight + weight - reduce
        if target_weight < 0:
            return 0
        
        elif not kit_list:
            return 1

        else:
            n_ok = 0
            for i in range(len(kit_list)):
                n_ok += backtracking(reduce, i, kit_list.copy(), target_weight)
            return n_ok

    n_ok = 0
    for ind in range(len(weight_list)):
        n_ok += backtracking(k, ind, weight_list.copy(), 0)

    print(f"{n_ok}")

solution(3, 4, [3, 7, 5])
