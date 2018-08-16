def merge_the_tools(string, k):
    # your code goes here
    for i in zip(*[iter(string)]*k):
        d={}
        print(''.join(d.setdefault(c,c) for c in i if c not in d))
            
