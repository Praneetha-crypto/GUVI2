n=int(input())
l =list(map(str,input().split()))
for i in l:
  if(l.count(i)>1):
     l.remove(i)
#my = list(dict.fromkeys(l))
for i in l:
  print(i,end=" ")
