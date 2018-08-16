def Solution(sentences,querries):
    result=[]
    for j in range(len(querries)):
        for i in range(len(sentences)):
            count = 0
            for k in querries[j]:
                if k in sentences[i]:
                    count +=1
                if count>=len(querries[j]):
                              
                              result.append(i)
        for a in range(len(result)):
            print(result[a],end=' ')
        print("")
        result=[]

sentences=["i am vaibhav","this is vaibhav","vaibhav is trying to code"]
querries=["vaibhav am","vaibhav"]

Solution(sentences,querries)
    
