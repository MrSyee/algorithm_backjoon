import doctest

def solution(n: str):
    """
    10162. 전자레인지 (B4)
    https://www.acmicpc.net/problem/10162

    Example
    -------
    >>> solution("100")
    '0 1 4'
    >>> solution("189")
    '-1'
    >>> solution("0")
    '0 0 0'
    >>> solution("60")
    '0 1 0'
    """
    # A: 300, B: 60, C: 10
    n = int(n)

    btn_a, btn_b, btn_c = 300, 60, 10
    num_a, n = n // btn_a, n % btn_a
    num_b, n = n // btn_b, n % btn_b
    num_c, n = n // btn_c, n % btn_c

    if n == 0:
        ans = f"{num_a} {num_b} {num_c}"
    else:
        ans = "-1"
    # print(ans)

    return ans


doctest.testmod()