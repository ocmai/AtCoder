#ABC185-B
N,M,T =map(int,input().split())
maxn = N
s = 0
for i in range(M):
  a,b = map(int,input().split())
  N -= a - s
  if N <= 0:
    print('No')
    exit()
  N += b - a
  N = min(N,maxn)
  s = b
N -= T - s
if N > 0:
  print('Yes')
else:
  print('No')
 
