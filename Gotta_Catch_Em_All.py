t = int(input())
for i in range(t):
    n,x,y = map(int, input().split())
    A = list(map(int, input().split())) 
    total_cost = sum(min(a*x,y) for a in A)
    print(total_cost)
