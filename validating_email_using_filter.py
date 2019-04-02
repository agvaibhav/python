def fun(s):
    # return True if s is a valid email, else return False
    try:
        username, url = s.split('@')
        website, extension = url.split('.')
    except:
        return False

    newusername = username.replace('-','a').replace('_','a')
    if newusername.isalnum() and website.isalnum():
        if len(extension)<=3:
            return True
    else:
        return False
    



def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
