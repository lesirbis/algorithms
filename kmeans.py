#k-means
import random

def ToCentersEquality(nk, Xc, Yc, NextXc, NextYc):
    CentersEquality = True
    for ik in range(nk):
        if (Xc[ik] != NextXc[ik]) or (Yc[ik] != NextYc[ik]): CentersEquality = False
    if CentersEquality == True: return True
    else: return False

nk = int(input("Количество кластеров: "))
Xc = [random.uniform(10, 100) for i in range(nk)]
Yc = [random.uniform(10, 100) for i in range(nk)]

np = int(input("Количество точек: "))
Xp = [random.uniform(10, 100) for i in range(np)]
Yp = [random.uniform(10, 100) for i in range(np)]

NextXc = [0 for i in range(nk)]
NextYc = [0 for i in range(nk)]
countiteration = 0

while ToCentersEquality(nk, Xc, Yc, NextXc, NextYc) == False:
    countiteration += 1
    Xpk = [[] * nk for i in range(nk)]
    Ypk = [[] * nk for i in range(nk)]
    for ip in range(np):
        mindist = ((Xp[ip]-Xc[0])**2+(Yp[ip]-Yc[0])**2)**(1/2)
        ikmindist = 0
        dist = []
        for ik in range(nk):
            dist.append(((Xp[ip]-Xc[ik])**2+(Yp[ip]-Yc[ik])**2)**(1/2))
            if dist[ik] < mindist:
                mindist = dist[ik]
                ikmindist = ik
        Xpk[ikmindist].append(Xp[ip])
        Ypk[ikmindist].append(Yp[ip])

    countpk = []
    for ik in range(nk):
        countpk.append(len(Xpk[ik]))
        sumX = sum(Xpk[ik])
        sumY = sum(Ypk[ik])
        NextXc[ik] = sumX/countpk[ik]
        NextYc[ik] = sumY/countpk[ik]
    if ToCentersEquality(nk, Xc, Yc, NextXc, NextYc) == False:
        Xc = NextXc.copy()
        Yc = NextYc.copy()
        NextXc = [0 for i in range(nk)]
        NextYc = [0 for i in range(nk)]

print("Количество итераций цикла: ", countiteration)
print("Координаты центров: \n", Xc, "\n", Yc)