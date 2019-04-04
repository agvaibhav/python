from collections import OrderedDict
N = int(input())
order_list = OrderedDict()
for i in range(N):
    item = input().split()
    item[-1]=int(item[-1])
    if " ".join(item[0:-1]) in order_list:
        order_list[" ".join(item[0:-1])]+=item[-1]
    else:
        order_list[" ".join(item[0:-1])]=item[-1]
for key,values in order_list.items():
    print(key,values)
