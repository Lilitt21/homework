import glob
# import os
d = dict()

for filename in glob.glob('*.txt'):
#for filename in os.listdir(os.getcwd()):
    with open(filename, 'r') as af:
        l = af.readline()
        while l:
            for letter in l:
                d[letter] = d.get(letter, 0) + 1
            l = af.readline()
# print(d)
