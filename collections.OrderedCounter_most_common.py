from collections import Counter,OrderedDict

class OrderedCounter(Counter,OrderedDict):
    pass

if __name__ == '__main__':
    s = sorted(input())
    high = OrderedCounter(s).most_common(3)
    for i in high:
        print(i[0],i[1])
