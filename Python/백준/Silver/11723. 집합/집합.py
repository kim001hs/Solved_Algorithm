import sys
input = sys.stdin.readline  # 편하게 input()처럼 사용
n = int(input())
arr = set()

for i in range(n):
    command = input().strip()
    if command == "all":
        arr = set(range(1, 21))    
    elif command == "empty":
        arr = set()
    else:
        cmd, x = command.split()
        x = int(x)
        if cmd == "add":
            arr.add(x)
        elif cmd == "remove":
            arr.discard(x)
        elif cmd == "check":
            print(1 if x in arr else 0)
        elif cmd == "toggle":
            if x in arr:
                arr.remove(x)
            else:
                arr.add(x)