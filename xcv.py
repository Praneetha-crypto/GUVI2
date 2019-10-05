n=int(input())
l=list(map(int,input().split()))
d=sorted(l,reverse=True)
for i in d:
  print(l.index(i),end=" ")

