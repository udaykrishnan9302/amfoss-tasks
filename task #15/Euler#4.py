t=int(input())
for i in range(t):
    n=int(input("e:"))
    for x in range(999, 101, -1):
        for y in range(x, 101, -1):
            num =x*y
            if num > n:
                s = str(num)
                if s == s[::-1]:
                    n = x * y
    print(n)
