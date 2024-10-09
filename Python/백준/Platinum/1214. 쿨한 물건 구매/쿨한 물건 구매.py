D,P,Q = map(int,input().split())
P,Q = max(P,Q),min(P,Q)
MIN = 1e10
for i in range(min(D//P,Q)+1):
    MIN = min(MIN,(Q-(D-P*i)%Q)%Q)
MIN = min(MIN,(P-(D%P))%P)
print(D+MIN)