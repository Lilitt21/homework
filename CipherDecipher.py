import random
import time

s = time.time()
with open('Key.txt', 'w') as kf:
    k = []
    for i in range(0,255):
        k.append(i)
    random.shuffle(k)
    for i in range (len(k)):
        kf.write(str(k[i]))
        kf.write(" ")
with open('Key.txt', 'r') as kf:
    with open('The_Count_of_Monte_Cristo.txt', 'r') as af:
        with open('The_Count_of_Monte_Cristo-ciph.txt', 'w') as bf:
            k = kf.readline()
            key = k.split()
            line = af.readline()
            while line:
                for i in line:
                    j = key[ord(i)]
                    bf.write(chr(int(j)))
                line = af.readline()
with open('Key.txt', 'r') as kf:
    with open('The_Count_of_Monte_Cristo-ciph.txt', 'r') as bf:
        with open('The_Count_of_Monte_Cristo-deciph.txt', 'w') as cf:
            k = kf.readline()
            key = k.split()
            line = bf.readline()
            while line:
                for i in line:
                    s = key.index(str(ord(i)))
                    cf.write(chr(int(s)))
                line = bf.readline()
f = time.time()
print(f-s)
