'''
    1956 운동
    알고리즘:
    1. 시작 지점이 정해지지 않고, 모든 구간에서 확인해야 하니까 플로이드 워셜 최단경로를 이용 
    2. 모든 정점에서 모든 정점을 가는 최단 경로를 확인한다
    3. 사이클 경로니까, i --> i의 경로 중 최소값을 찾는다
'''
import sys
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
graph = [[INF] * (V+1) for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 플로이드 워셜 수행
for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans = INF
for i in range(1, V+1): # 사이클 경로의 최단 길이를 찾아야 하니까, 출발과 도착지가 같은 graph 중 최소를 고른다
    ans = min(ans, graph[i][i])

# 사이클 최단 경로가 INF 이상이면, 경로가 없는 것
if ans >= INF:
    print(-1)
else:
    print(ans)
