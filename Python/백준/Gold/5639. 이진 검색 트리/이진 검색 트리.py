import sys
sys.setrecursionlimit(10**9)
def input(): return sys.stdin.readline()
arr=[]
while True:
    try:
        temp=int(input())
        arr.append(temp)
    except:
        break

def solve(start, end):
    if start >= end:
        return

    root = arr[start]
    # root보다 커지는 첫 번째 요소의 인덱스를 찾음
    divider_index = end
    for i in range(start + 1, end):
        if arr[i] > root:
            divider_index = i
            break

    # 왼쪽 서브트리 (root보다 작은 값들)
    solve(start + 1, divider_index)
    # 오른쪽 서브트리 (root보다 큰 값들)
    solve(divider_index, end)

    print(root)
    
solve(0,len(arr))