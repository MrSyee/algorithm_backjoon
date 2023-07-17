def solution():
    """
    1063. 킹 (S3)
    https://www.acmicpc.net/problem/1063

    TC: O(n_move)
    """
    import sys

    # input
    k_loc, s_loc, n_move = sys.stdin.readline().split()
    n_move = int(n_move)
    moves = []
    for _ in range(int(n_move)):
        moves.append(sys.stdin.readline().split('\n')[0])

    # Constant
    MIN_COL, MAX_COL = 1, 8
    MIN_ROW, MAX_ROW = "A", "H"

    def move(curr_loc: str, action: str):
        row, col = curr_loc[0], int(curr_loc[1])
        d_row, d_col = 0, 0
        if "R" in action:
            d_row = 1
        elif "L" in action:
            d_row = -1

        if "B" in action:
            d_col = -1
        if "T" in action:
            d_col = 1

        next_row = chr(ord(row) + d_row)
        next_col = col + d_col

        if next_col < MIN_COL or next_col > MAX_COL or next_row < MIN_ROW or next_row > MAX_ROW:
            return row + str(col)
        return next_row + str(next_col)

    for m in moves:
        next_k_loc = move(k_loc, m)
        next_s_loc = s_loc
        if next_k_loc == s_loc:
            next_s_loc = move(s_loc, m)

        k_loc, s_loc = (k_loc, next_s_loc) if next_k_loc == next_s_loc else (next_k_loc, next_s_loc)

    print(k_loc)
    print(s_loc)


solution()
