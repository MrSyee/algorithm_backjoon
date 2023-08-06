"""
10971. 외판원 순회 2 (S2)
https://www.acmicpc.net/problem/10971

DFS + Bruteforce(Backtracking)
"""

def solution():
    """
    혼자서는 못풀고, 검색한 코드 참고하여 만들었음.
    예제는 맞았으나 틀림.
    """
    import sys

    class DFS:
        def __init__(self, graph: list, n_cities: int, first: int):
            self.graph = graph
            self.n_cities = n_cities
            self.first = first
            self.visited = [False] * n_cities
            self.total_cost = 1_000_000

        def visit_city(self, start: int, cost: int, depth: int):
            # print(f"start: {start}, cost: {cost}, depth: {depth}")
            # 모든 도시를 다 돌았다면
            if depth == self.n_cities:
                for next, next_cost in self.graph[start]:
                    # 첫번째로 다시 돌아가고 cost 계산
                    if next == self.first:
                        self.total_cost = min(self.total_cost, cost + next_cost)
                        # print("total_cost", self.total_cost)
                    return

            # print("visited", self.visited)
            if self.visited[start]:
                return

            self.visited[start] = True

            for next, next_cost in self.graph[start]:
                if not self.visited[next]:
                    # print("cost", cost, "next_cost", next_cost)
                    self.visit_city(next, cost + next_cost, depth=depth+1)
                    self.visited[next] = False


    # Input
    n_cities = int(sys.stdin.readline())
    graph = [[] for _ in range(n_cities)]
    for n in range(n_cities):
        # Create graph
        costs = list(map(int, sys.stdin.readline().split()))
        for j in range(n_cities):
            if costs[j] == 0: continue
            graph[n].append((j, costs[j]))

    # 차례로 방문
    min_costs = 1_000_000
    for start_city in range(n_cities):
        dfs = DFS(graph, n_cities, start_city)
        # print(f"VISIT_CITY start: {start_city}")
        dfs.visit_city(start=start_city, cost=0, depth=1)
        min_costs = min(min_costs, dfs.total_cost)
    print(min_costs)


def solution2():
    """
    중간에 이미 total_cost가 min_cost를 넘을 경우, early stop 하는 로직이 필요함.
    """
    import sys

    n_cities = int(sys.stdin.readline())
    graph = [[] for _ in range(n_cities)]
    for n in range(n_cities):
        # Create graph
        costs = list(map(int, sys.stdin.readline().split()))
        for j in range(n_cities):
            graph[n].append(costs[j])
    # print(graph)

    def dfs(curr_city, total_cost, min_cost, start, depth):
        if depth == n_cities:
            if graph[curr_city][start] != 0:
                total_cost += graph[curr_city][start]
                # print("depth", depth, "min_cost", min_cost, "total_cost", total_cost)
                return min(min_cost, total_cost)
            return min_cost

        for next_city, cost in enumerate(graph[curr_city]):
            # print("next_city, cost", next_city, cost)
            if cost != 0 and next_city not in visited and total_cost < min_cost:
                # print(curr_city, next_city, visited, total_cost, cost)
                visited.append(next_city)
                min_cost = dfs(next_city, total_cost + cost, min_cost, start, depth + 1)
                visited.pop()
        return min_cost

    min_cost = 1_000_000 * n_cities
    for city in range(n_cities):
        visited = [city]
        min_cost = dfs(city, 0, min_cost, city, 1)
        # print(min_cost)

    print(min_cost)

solution2()
