# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
t = int(input())
for i in range(t):
    n = int(input())
    l = [float('inf')]
    d = deque(map(int,input().split()))
    for i in range(n):
        if d[-1]>d[0]:
            if l[-1]>=d[-1]:
                l.append(d[-1])
                d.pop()
            else:
                print('No')
                break
        else:
            if l[-1]>=d[0]:
                l.append(d[0])
                d.popleft()
            else:
                print('No')
                break
    if len(l)==n+1:
        print('Yes')
        
OR

for t in range(input()):
    input()
    lst = map(int, raw_input().split())
    l = len(lst)
    i = 0
    while i < l - 1 and lst[i] >= lst[i+1]:
        i += 1
    while i < l - 1 and lst[i] <= lst[i+1]:
        i += 1
    print "Yes" if i == l - 1 else "No"
