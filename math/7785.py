import doctest

def solution(log: str):
    """
    7785. 회사에 있는 사람 (S5)
    https://www.acmicpc.net/problem/7785
    
    TC: O(n_log)

    Example
    -------
    >>> solution("4\nBaha enter\nAskar enter\nBaha leave\nArtem enter")
    ['Askar', 'Artem']
    """
    import sys
    logs = []
    for i, line in enumerate(sys.stdin):
        if i == 0:
            n_log = int(line)
        else:
            logs.append(line)

    log = log.split("\n")
    n_log, logs = log[0], log[1:]
    print(n_log)
    print(logs)

    in_office = dict()
    for log in logs:
        name, action = log.split()
        if action == "enter":
            in_office[name] = action
        else:
            del in_office[name]  # dict: O(1), list: O(N)
    in_office = sorted(in_office.keys(), reverse=True)
    for name in in_office:
        print(name)


solution("4\nBaha enter\nAskar enter\nBaha leave\nArtem enter")