# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
aset = set(map(int, input().split()))
n = int(input())
for i in range(n):
    cmd, l = input().split()
    nset = set(map(int, input().split()))
    getattr(aset,cmd)(nset)
print(sum(aset))
