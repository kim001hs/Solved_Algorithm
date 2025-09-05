import sys
input = sys.stdin.readline

n = int(input())
count = 0

def solve(arr):
    global count
    
    # 퀸을 모두 배치했으면 경우의 수 증가
    if len(arr) == n:
        count += 1
        return

    # 다음 행(len(arr))에 퀸을 놓을 열(col)을 탐색
    for col in range(n):
        # 현재 위치 (len(arr), col)에 퀸을 놓을 수 있는지 확인
        is_valid = True
        
        # 이전에 놓인 퀸들과 충돌하는지 검사
        for row in range(len(arr)):
            # 1. 같은 열(column)에 있는지 확인
            if arr[row] == col:
                is_valid = False
                break
            
            # 2. 대각선상에 있는지 확인
            if abs(arr[row] - col) == abs(row - len(arr)):
                is_valid = False
                break
        
        # 충돌이 없으면 재귀 호출
        if is_valid:
            arr.append(col)
            solve(arr)
            arr.pop() # 백트래킹
            
solve([])
print(count)