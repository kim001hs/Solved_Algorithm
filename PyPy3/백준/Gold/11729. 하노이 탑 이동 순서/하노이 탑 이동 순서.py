import sys
input = sys.stdin.readline
n=int(input())

def hannoi(start,sub,end,floor):
    if floor == 1:
        print(str(start)+' '+str(end))
        return 
    
    hannoi(start,end,sub,floor-1)
    print(str(start)+' '+str(end))
    hannoi(sub,start,end,floor-1)
    return

print(2**n-1)
hannoi(1,2,3,n)