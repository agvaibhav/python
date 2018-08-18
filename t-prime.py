import time
num=input()
user_input=input().split()
start_time=time.time()
if __name__ == '__main__':
   
    for i in user_input:
        count = 0
        i = int(i)
        for j in range(2,(i//2)+1):
            if i%j == 0:
                count+=1
            
        if count == 1:
            print("YES")
        else:
            print("NO")
    
    print("---%s seconds ---"%(time.time()-start_time))
    
