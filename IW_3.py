f=open("Input.txt")
x=f.read().split()
z=[]
y=[]
Ысыах=[]
n=len(x)
flag = True
c = 0
for i in range(0, n - 1, 2):
    y.append((int(x[i]) + int(x[i + 1])))
    Ысыах.append((int(x[i]) + int(x[i + 1])) * 0.05)
if (n % 2 == 1):
    y.append(int(x[len(x)-1]))
n = len(y)
print(y)
if len(y) == 1:
    flag = False
while flag == True:
    if c == 1:
        y=[]
        for i in range(0, len(z) - 1, 2):
            y.append((int(z[i]) + int(z[i + 1])))
            Ысыах.append((int(z[i]) + int(z[i + 1])) * 0.05)
        if (len(z) % 2 == 1):
            y.append(int(z[len(z)-1]))
        if len(y) == 1:
            flag = False
        print(y)
        c=0
        del z
    elif (flag == True) and (c==0):
        z=[]
        for i in range(0, len(y) - 1, 2):
            z.append((int(y[i]) + int(y[i + 1])))
            Ысыах.append((int(y[i]) + int(y[i + 1])) * 0.05)
        if (len(y) % 2 == 1):
            z.append(int(y[len(y)-1]))
        if len(z) == 1:
            flag = False
        print(z)
        c=1
        del y

print(sum(Ысыах))
f.close()
