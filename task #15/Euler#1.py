def eul1():  
  n = 0
  for i in range(1,inp):
     if (i % 5==0 or i % 3==0):
         n+=i
  return n

rep=int(input())
for repea in range(rep):
    inp=int(input())
    print(eul1())

