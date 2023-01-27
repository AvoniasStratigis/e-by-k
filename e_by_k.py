import math

Temp = [303.16, 313.16, 318.16, 323.16, 328.16, 333.16]
V = [0.48, 0.50, 0.52, 0.54, 0.56, 0.58, 0.60, 0.62]
Eta = [1.7, 1.66, 1.6, 1.565, 1.53, 1.475]
B = []

for i in range(0,6):
    b = Eta[i]*Temp[i]
    B.append(b)

print (B)

I_c = [2.79E-3 ,3.59E-3 ,7.9E-3 ,14.2E-3 ,25.6E-3 ,45.3E-3 ,55.9E-3 ,61.3E-3]
logIC = []
for i in range (0,8):
    A = math.log10(I_c[i])
    logIC.append(A)

print (logIC)

I_cT = [2.79 ,3.59 ,7.9 ,14.2 ,25.6 ,45.3 ,55.9 ,61.3]
logICT = []
for i in range (0,8):
    A = math.log10(I_cT[i])-3
    logICT.append(A)

print (logICT,"\n\n\n")

def Logg(X):
    Y = []
    for i in range (0,8):
        A = math.log10(X[i])-3
        Y.append(A)
    print(Y)

I30 = [2.28,2.71,3.49,7.42,13,23.65,43.3,51]
I40 = [2.59,3.26,6.62,11.22,21.3,41.4,53.8,59.6]
I45 = [2.79,3.59,7.9,14.2,25.6,45.3,55.9,61.3]
I50 = [3.07,6.24,10.60,20.04,37.1,51.3,58.1,63.8]
I55 = [3.47,7.58,12.81,23.34,41.4,53.1,60.1,64.6]
I60 = [3.76,8.9,17.16,31.21,46.5,55.1,60.4,65.1]

Logg(I30)
Logg(I40)
Logg(I45)
Logg(I50)
Logg(I55)
Logg(I60)
