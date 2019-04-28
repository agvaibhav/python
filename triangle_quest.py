1
22
333
4444
55555
......

for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(10**i//9*i)


1
121
12321
1234321
........

for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(pow(10**i//9,2)) 
