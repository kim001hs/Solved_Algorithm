from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# n: 세로 크기, m: 가로 크기
n, m = map(int, input().split())
arr = []  # 빙산 정보를 담을 배열
rotate = [[1,0],[0,1],[-1,0],[0,-1]]  # 상하좌우 탐색 방향
needcount = 0  # 현재 남아 있는 빙산 칸 개수

# 초기 빙산 지도 입력
for i in range(n):
    data = list(map(int, input().split()))
    for idx, j in enumerate(data):
        if j > 0:  # 빙산이 존재하는 칸
            needcount += 1
            next_i, next_j = i, idx  # 시작점 후보 저장
    arr.append(data)

total = 0  # 시간(년) 카운트

def bfs(i, j, needcount):
    """빙산 덩어리 탐색 및 동시에 녹이기"""
    nxi, nxj = i, j
    global arr
    count = 1  # 연결된 빙산 칸 개수
    visited = [[False] * m for _ in range(n)]

    queue = deque()
    queue.append((i, j))
    visited[i][j] = True

    if arr[i][j] == 0:  # 시작 지점이 빙산이 아니면 무효
        return 0, 0, 0, 0

    while queue:
        i, j = queue.popleft()
        for k in range(4):
            ni, nj = i + rotate[k][0], j + rotate[k][1]
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                if arr[ni][nj] > 0:  # 빙산 칸이면 연결 탐색
                    visited[ni][nj] = True
                    queue.append((ni, nj))
                    count += 1
                else:  # 바닷물이면 현재 칸 녹음
                    arr[i][j] -= 1
                    if arr[i][j] == 0:
                        needcount -= 1
        if arr[i][j] > 0:
            nxi, nxj = i, j  # 다음 BFS 시작점 갱신
    return count, needcount, nxi, nxj

# 메인 루프 (빙산이 분리되거나 다 녹을 때까지 반복)
while True:
    count, temp, next_i, next_j = bfs(next_i, next_j, needcount)

    if temp <= 0:  # 빙산이 전부 녹은 경우
        print(0)
        break

    if count != needcount:  # 빙산이 두 덩어리 이상으로 분리된 경우
        print(total)
        break

    needcount = temp
    total += 1  # 1년 경과
