from itertools import product
k,m = list(map(int,input().split()))
out=[None]*k
for i in range(k):
    inp = list(map(int,input().split()))
    out[i] = [x**2 for x in inp[1:]]
result = list(map(lambda x: sum(i for i in x)%m ,list(product(*out))))
print(max(result))
