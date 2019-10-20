def cipher (a, key):
    b = list()
    for i in range (len(a)):
        if (ord(a[i]) + key) > 122:
            b.append(chr((ord(a[i])+key)-26))
        else:
            b.append(chr((ord(a[i]) + key)))
    return (b)

def decipher (b, key):
    a = list()
    for i in range (len(b)):
        if (ord(b[i]) - key) < 97:
            a.append(chr((ord(b[i])-key)+26))
        else:
            a.append(chr((ord(b[i]) - key)))
    return (a)

def count(a):
    D = dict()
    for i in range (len(a)):
        if a[i] in D:
            D[a[i]] += 1
        else:
            D[a[i]] = 1
    return (D)

a = list(input())
key = int(3)
ciph = cipher (a,key)
print (''.join(ciph))
deciph = decipher (ciph, key)
print (''.join(deciph))
print ('')
print (count(a))
