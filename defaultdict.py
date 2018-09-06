from collections import defaultdict

#program 1

n,m = list(map(int,input().split()))
ninp = defaultdict(list)
for i in range(n):
    ninp[input()].append(i+1)
    

for j in range(m):
        minp = input()
        if ninp[minp]==[]:
            print(-1)
        else:
            out=' '.join(map(str,ninp[minp]))
            print(out)


#program 2

ice_cream = defaultdict(lambda: 'vanilla')
ice_cream['sarah']='choco'
ice_cream['ankit']='coco'
print(ice_cream)
print(ice_cream['vaibhav'])
print(ice_cream['sarah'])



#program 3

food_list = 'spam spam spam spam spam spam eggs spam'.split()
food_count = defaultdict(int) # default value of int is 0
for food in food_list:
    food_count[food] += 1 # increment element's value by 1

print(food_count)




#program 4

city_list = [('TX','Austin'), ('TX','Houston'), ('NY','Albany'), ('NY', 'Syracuse'), ('NY', 'Buffalo'), ('NY', 'Rochester'), ('TX', 'Dallas'), ('CA','Sacramento'), ('CA', 'Palo Alto'), ('GA', 'Atlanta')]
cities_by_state = defaultdict(list)  #default value of list is an empty list
for state,city in city_list:
    cities_by_state[state].append(city)

print(cities_by_state)
