import operator
import time
import collections

s = time.time()
with open('The_Count_of_Monte_Cristo-deciph.txt', 'r') as af:
    with open('Probability.txt', 'r') as kf:
        with open('Pkeys.txt', 'w') as rf:
            P = kf.readline().split()
            for i in range (1,len(P),2):
                P[i] = float(P[i])
            for i in range (0,len(P),2):
                P[i] = int(P[i])

            key = []
            count = 0
            d = {}
            line = af.readline()
            while line:
                for letter in line:
                    count+=1
                    d[letter] = d.get(letter, 0) + 1
                line = af.readline()
            sort = sorted(d.items(), key=operator.itemgetter(1))
            for i in range(len(sort)):
                b = list(sort[i])
                key.append(ord(b[0]))
                key.append(b[1])

            rez = ["none"]*255
            j = 0
            for i in range (1,len(key),2):
                key[i] = float('{:.6f}'.format((key[i]/count)))
            for i in range (0,len(key),2):
                rez[P[i]] = chr(key[i])
            for i in rez:
                rf.write(i)
                rf.write(" ")
f = time.time()
print(f-s)
