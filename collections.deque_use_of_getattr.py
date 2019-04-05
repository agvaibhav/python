# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
n = int(input())
d = deque()
for i in range(n):
    cmd = input().split()
    if len(cmd)>1:
        getattr(d,cmd[0])(int(cmd[-1]))
    else:
        getattr(d,cmd[0])()
print(*d)
