'''input: abcd
   key = 3
   output: defg'''

a = list(input())
b = list()
key = 3
for i in range (len(a)):
    if (ord(a[i]) + key) > 122:
        b.append(chr((ord(a[i])+key)-26))
    else:
        b.append(chr((ord(a[i]) + key)))
print(''.join(b))
