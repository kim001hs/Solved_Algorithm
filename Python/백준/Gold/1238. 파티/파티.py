import sys
from queue import PriorityQueue

input = sys.stdin.readline  # 편하게 input()처럼 사용
n, m, x = map(int, input().split())
line= [[] for _ in range(n + 1)]    
lint_back = [[] for _ in range(n + 1)]  # 돌아오는 길을 위한 리스트
for i in range(1, m + 1):
    a,b,c= map(int, input().split())
    line[b].append((a, c))  # b에서 a로 가는 길이 c
    lint_back[a].append((b, c))  # a에서 b로 가는 길이 c (왕복이므로 양방향)
def dijkstra(start, array):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    pq = PriorityQueue()
    pq.put((0, start))  # (거리, 노드)
    while not pq.empty():
        current_dist, current_node = pq.get()
        if current_dist > dist[current_node]:
            continue
        for neighbor, weight in array[current_node]:
            distance = current_dist + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                pq.put((distance, neighbor))
    return dist
go_result = dijkstra(x, line)
back_result = dijkstra(x, lint_back)
dijkstra_result = [go_result[i] + back_result[i] for i in range(1, n + 1)]  # 왕복 거리 계산
print(max(dijkstra_result[1:]))  # x에서 다른 모든 노드까지의 최단 거리 중 최대값 출력
