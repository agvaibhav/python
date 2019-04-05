n = input("Write the number:")
l = len(n)

# if number is 999...
sum = 0
for i in n:
    if i=='9':
        sum+=1
if sum == l:
    print("closest palindrome is:", int(n)+2)


def is_palindrome(n):
    sum = 0
    for i in range(len(n)//2):
        if n[i] == n[len(n)-1-i]:
            sum+=1
    if sum == len(n)//2:
        return True
    else:
        return False


# if number is already a palindrome and odd
if (is_palindrome(n) and l%2!=0 ) :
    middle_index = l//2
    middle_no = int(n[middle_index])
    if middle_no !=9:
        middle_no += 1
        res = n[0:middle_index]+str(middle_no)+n[middle_index+1:]
        print("closest palindrome is:", res)
        print('or')
        middle_no -= 2
        res = n[0:middle_index]+str(middle_no)+n[middle_index+1:]
        print("closest palindrome is:", res)


# if number is already a palindrome and even
elif (is_palindrome(n) and l%2 == 0):
    middle_index = l//2
    middle_no = int(n[middle_index])
    if middle_no != 9:
        middle_no += 1
        res = n[0:middle_index-1]+str(middle_no)*2+n[middle_index+1:]
        print("closest palindrome is:", res)
        print('or')
        middle_no -= 2
        res = n[0:middle_index-1]+str(middle_no)*2+n[middle_index+1:]
        print("closest palindrome is:", res)


# if number is odd
elif l%2!=0:
    middle_index = l//2
    res = n[0:middle_index+1]
    for i in range(middle_index):
        res = res + n[middle_index-1-i]
    print("closest palindrome is:", res)

# if number is even
elif l%2==0:
    middle_index = l//2
    res = n[0:middle_index]
    for i in range(middle_index):
        res = res + n[middle_index-1-i]
    print("closest palindrome is:", res)
        

