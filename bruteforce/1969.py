def solution(n_dna: int, length: int, dna_list: list):
    """
    1969. DNA (S5)
    https://www.acmicpc.net/problem/1969

    TC: O(length * n_dna)
    """
    import sys
    from collections import defaultdict
    
    # n_dna, length = list(map(int, input().split()))
    # dna_list = []
    # for _ in range(n_dna):
    #      dna_list.append(sys.stdin.readline())

    sol_dna, sol_d = "", 0
    
    for l in range(length):
        char_dict = defaultdict(int)
        for dna in dna_list:
            char_dict[dna[l]] += 1
        sol_char = max(sorted(char_dict), key=char_dict.get)
        sol_dna += sol_char

        del char_dict[sol_char]
        sol_d += sum(char_dict.values())

    print(f"{sol_dna}\n{sol_d}")

solution(5, 8, ["TATGATAC", "TAAGCTAC", "AAAGATCC", "TGAGATAC", "TAAGATGT"])
solution(4, 10, ["ACGTACGTAC", "CCGTACGTAG", "GCGTACGTAT", "TCGTACGTAA"])
solution(6, 10, ["ATGTTACCAT", "AAGTTACGAT", "AACAAAGCAA", "AAGTTACCTT", "AAGTTACCAA", "TACTTACCAA"])
