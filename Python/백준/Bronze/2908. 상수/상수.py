import sys
input = sys.stdin.readline  # 편하게 input()처럼 사용
A,B=map(str,input().split())
inverted_A=int(str(A)[::-1])
inverted_B=int(str(B)[::-1])
print(max(inverted_A,inverted_B))