t=int(input())
for i in range(t):
  n=int(input())
  p=1
  for i in range(1,n+1):
    while True:
      if p%i!=0:
          p+=1
      else:
          print(p)
          break
