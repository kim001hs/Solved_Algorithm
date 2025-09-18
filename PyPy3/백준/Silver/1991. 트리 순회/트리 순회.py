import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()
class Node():
    def __init__(self, name):
        self.Name=name
        self.leftChild=None
        self.rightChild=None
        
nodelist={}#딕셔너리 만들기 key:이름 value:노드
N=int(input())

data=list(map(str, input().split()))#첫 번째 입력 처리
root=Node(data[0])#루트 노드 만들어줌
nodelist[data[0]]=root
if data[1]!='.':#왼쪽이 있으면 노드 추가
    temp=Node(data[1])
    root.leftChild=temp
    nodelist[data[1]]=temp
if data[2]!='.':#오른쪽이 있으면 노드 추가
    temp=Node(data[2])
    root.rightChild=temp
    nodelist[data[2]]=temp
    
for i in range(N-1):#그 다음 입력 처리
    data=list(map(str, input().split()))
    parent=nodelist.get(data[0])
    if data[1]!='.':
        temp=Node(data[1])
        parent.leftChild=temp
        nodelist[data[1]]=temp
    if data[2]!='.':
        temp=Node(data[2])
        parent.rightChild=temp
        nodelist[data[2]]=temp

def preorder(root):#전위순회
    #pop하면 오른쪽 왼쪽 순으로 스택에 넣음
    #pop할 때 result에 +=
    stack=[]
    result=""
    stack.append(root)
    while stack:
        temp=stack.pop()
        result+=temp.Name
        if temp.rightChild:
            stack.append(temp.rightChild)
        if temp.leftChild:
            stack.append(temp.leftChild)
    return result

def inorder(root):#중위순회
    #양쪽 노드에 대해서 재귀 호출
    #없으면 0으로 예외처리
    if root==0:
        return ''
    L=root.leftChild if root.leftChild!=None else 0
    R=root.rightChild if root.rightChild!=None else 0
    return inorder(L)+root.Name+inorder(R)

def postorder(root):#후위순회
    #pop하면 왼쪽 오른쪽 순으로 스택에 넣음 -> 마지막에 뒤집기
    #pop할 때 result에 +=
    stack=[]
    result=""
    stack.append(root)
    while stack:
        temp=stack.pop()
        result+=temp.Name
        if temp.leftChild:
            stack.append(temp.leftChild)
        if temp.rightChild:
            stack.append(temp.rightChild)
    return result[::-1]

print(preorder(root))
print(inorder(root))
print(postorder(root))