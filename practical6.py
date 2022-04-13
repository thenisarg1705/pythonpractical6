import collections;

N1 = int(input())
d1 = collections.OrderedDict()

for i in range(N1):
    word = input()
    if word in d1:
        d1[word] +=1
    else:
        d1[word] = 1

print(len(d1))

for k,v in d1.items():
    print(v,end = " ")
