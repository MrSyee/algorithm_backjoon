"""
1932. 정수 삼각형 (S1)
https://www.acmicpc.net/problem/1932

TC: 
"""
# DP까지는 생각했으나 풀기 실패. 검색해보고 힌트를 얻어서 풀어봄.
def solution():
    import sys

    N = int(sys.stdin.readline())
    memory = []
    for _ in range(N):
        memory.append(list(map(int, sys.stdin.readline().split())))
    
    for i in range(1, N):
        for j in range(len(memory[i])):
            # 맨 처음은 오른쪽 위와 더함
            if j == 0:
                memory[i][j] += memory[i-1][j]
            # 맨 끝은 왼쪽 위와 더함
            elif j == (len(memory[i]) - 1):
                memory[i][j] += memory[i-1][j-1]
            # 가운데는 max(왼쪽위, 오른쪽위)와 더함
            else:
                memory[i][j] += max(memory[i-1][j-1], memory[i-1][j])
    print(max(memory[-1]))
solution()