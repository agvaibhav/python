import string
from datetime import date

def find_days(n):
    new_date = list(map(int,n.split('-')))
    if len(new_date)<3:
        return(False)
    a = date(2019,4,12)
    b = date(new_date[0],new_date[1],new_date[2])
    delta = a-b
    if delta.days <= 89:
        return(False)
    else:
        return(True)

def find_v1(n):
    if n>=100000:
        return('F')
    elif n>=50000 and n<100000:
        return('H')
    elif n>=25000 and n<50000:
        return('S')
    
def digit_sum(n):
    while(len(n)>1):
        sum_digit = 0
        for i in n:
            if i !='.':
                sum_digit += int(i)
        n = str(sum_digit)
    return n
    
def digit_sum_date(n):
    while(len(n)>1):
        sum_digit = 0
        for i in n:
            if i!='-':
                sum_digit += int(i)
        n = str(sum_digit)
    return n

def main(n,l):       
    for i in range(n):
        details = input().split(',')
        if len(details)<5 or len(details[0])!=10:
            l[i].append(details[0])
            l[i].append('N/A')
        elif len(details[1])<=1 or len(details[3])<=7 or details[-1]!='0' or float(details[2])<25000:
            l[i].append(details[0])
            l[i].append('N/A')
        elif find_days(details[3])==False:
            l[i].append(details[0])
            l[i].append('N/A')
        else:
            v1 = str(find_v1(float(details[2])))
            
            alt = str(99999 - int(details[0][0:5]))
            if len(alt)<5:
                alt = alt.rjust(5,'0')
            v2 = str(alt[4])
            v4 = str(alt[3])
            v6 = str(alt[2])
            v8 = str(alt[1])
            v10 = str(alt[0])
            
            letters = string.ascii_letters[26:]
            try:
                ind = letters.index(details[1][0].upper())
                v3 = str(letters[-ind-1])
            except:
                v3 = 'Z'
            
            name = details[1].split()
            last_name = name[-1]
            if last_name == name[0] and len(name)==1:
                v5 = 'Z'
            else:
                try:
                    ind = letters.index(last_name[0].upper())
                    v5 = str(letters[-ind-1])
                except:
                    v5 = 'Z'
            
            v7 = str(digit_sum(details[2]))
            v9 = str(digit_sum_date(details[3]))
            
            ans = v1+v2+v3+v4+v5+v6+v7+v8+v9+v10
            l[i].append(details[0])
            l[i].append(ans)
        
if __name__=='__main__':
    n = int(input())
    l=[[] for i in range(n)]
    main(n,l)
    for row in sorted(l,key=lambda row: row[0]):
        print(row[0]+','+row[1])
    
    
