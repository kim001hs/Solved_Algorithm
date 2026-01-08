import sys
def input(): return sys.stdin.readline().rstrip()


n, b, c = map(int, input().split())
arr = list(map(int, input().split()))
arr += [0, 0]
result = 0
if b <= c:  # b가 더 싸면 모든 라면을 하나씩 삼
    print(b*sum(arr))
    sys.exit(0)

for i in range(n):
    if arr[i+1] > arr[i+2]:
        # 2개 먼저삼 뒤에 합칠거는 남겨놓음
        low = min(arr[i], arr[i+1]-arr[i+2])
        result += (b+c)*low
        arr[i] -= low
        arr[i+1] -= low
        # 남으면 3개짜리 삼
        low = min(arr[i], arr[i+1], arr[i+2])
        result += (b+2*c)*low
        arr[i] -= low
        arr[i+1] -= low
        arr[i+2] -= low
    else:
        # 3개짜리 삼
        low = min(arr[i], arr[i+1], arr[i+2])
        result += (b+2*c)*low
        arr[i] -= low
        arr[i+1] -= low
        arr[i+2] -= low
    # 남은건 하나짜리로 삼
    result += b*arr[i]
print(result)