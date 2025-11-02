t=int(input())
for _ in range(t):
    a = input()
    b = input()
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    print(f"Hamming distance is {count}.")
    