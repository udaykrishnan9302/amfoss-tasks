def largepfactor(num):
    pfactor = 1 
    i = 2

    while i <= num / i:
        if num % i == 0:
            pfactor = i
            num /= i
        else:
            i += 1

    if pfactor < num: 
        pfactor = num

    return int(pfactor)
rep=int(input())
for repea in range(rep):
     num=int(input())
     print(largepfactor(num))
