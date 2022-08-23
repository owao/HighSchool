def main():
 D={}
 z=[(i,(1<<i)-1) for i in range(1,30)]
 def q(s,e):
  if (s,e) in D:
   return D[(s,e)]
  v=max([q(max(0,s-c),min(c,e-c))+i for i,c in z if s<=2*c and c<=e],default=0)
  D[(s,e)]=v
  return v
 for i in range(int(input())):
  l,r=map(int,input().split())
  print(q(l,r))

main()
