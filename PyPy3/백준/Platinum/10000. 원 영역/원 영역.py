import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(100000)
MX = int(1e9)+1
n=int(input())
circles=[]
class Circle:
    def __init__(self,st,en):
        self.st=st
        self.en=en
        self.dia=en-st
        self.children=[]

def append_child(node):
    global index
    while index<n and circles[index][1]<=node.en:
        child=Circle(circles[index][0],circles[index][1])
        node.children.append(child)
        index+=1
        append_child(child)

def calculate(node):
    global count
    count+=1
    sum_dia=0
    for child in node.children:
        sum_dia+=child.dia
        calculate(child)
    if node.dia==sum_dia:
        count+=1

for i in range(n):
    x,r=map(int,input().split())
    circles.append([x-r,x+r])
circles.sort(key=lambda x:(x[0],-x[1]))

root=Circle(-MX,MX)
index,count=0,0
append_child(root)

calculate(root)
print(count)