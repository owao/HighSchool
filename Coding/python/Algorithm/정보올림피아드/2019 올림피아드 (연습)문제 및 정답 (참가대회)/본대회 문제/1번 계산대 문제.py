import heapq
import sys

def main():
	input = sys.stdin.readline
	n, K = map(int, input().split())

	a = []
	b = []
	for i in range(n):
		aa, bb = map(int, input().split())
		a.append(aa)
		b.append(bb)

	h = []
	for i in range(K):
		heapq.heappush(h, (0, i))

	T = [0] * K
	loc = [0] * n
	Num = [i for i in range(n)]
	
	L = []
	for i in range(n):
		t, x = heapq.heappop(h)
		T[x] += b[i]
		heapq.heappush(h, (T[x], x))
		L.append((T[x],-x,i))

	print(sum(a[t[2]] * (i+1) for i, t in enumerate(sorted(L))))

main()
