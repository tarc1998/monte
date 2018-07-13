import math
import numpy as np
import random

n = 4
m = 4

pi = np.array([[[0.25]*m]*n]*4)
proba = np.array([[[[[0]*m]*n]*m]*n]*4)
dir_r = [-1, 0, 1, 0]
dir_c = [0, 1, 0, -1]
counter = np.array([[[0.]*m]*n]*4)
sum = np.array([[[0.]*m]*n]*4) #suma rewardow
q = np.array([[[0.]*m]*n]*4)
ile = [[0]*4]*3


def simu(i, j, pi):
    trace = []
    while j > 0:
        #losowanie wyboru akcji
        number = random.uniform(0, 1)
        act = 0
        action = 0
        for a in range(4):
            if act + pi[a][i][j] >= number:
                action = a
                break
            else:
                act += pi[a][i][j]

        #losowanie rzeczywistej akcji
        number = random.uniform(0, 1)
        act = 0
        for r in range(n):
            for c in range(m):
                if proba[action][i][j][r][c] + act >= number:
                    trace.append((i, j, action))
                    i = r
                    j = c
                else:
                    act += proba[action][i][j][r][c]
    if i==0:
        output = 1
    else:
        output = 0
    return (trace, output)

#ustalamy prawdopodobienstwa dla skrajnych klockow
for r in range(n):
    for c in range(m):
        for a in range(4):
            if 0 <= r+dir_r[a] < n and 0 <= c+dir_c[a] < m:
                proba[a][r][c][r+dir_r[a]][c+dir_c[a]] = 1
            else:
                proba[a][r][c][r][c] = 1

#ustalamy prawdopodobienstwa dla lewej krawedzi
for r in range(n):
    for a in range(4):
        for i in range(n):
            for j in range(m):
                proba[a][r][0][i][j] = 0
        proba[a][r][c][r][c] = 1

#liczymy srednie dla pol
for i in range(1000):
    x, out = simu(3, 3, pi)
    for j in range(len(x)):
        counter[x[j][2]][x[j][0]][x[j][1]] += 1
        sum[x[j][2]][x[j][0]][x[j][1]] += out

#ustalamy wartosci q
for i in range(n):
    for j in range(m):
        for a in range(4):
            if counter[a][i][j] == 0:
                q[a][i][j] = 0
            else:
                q[a][i][j]=sum[a][i][j]/counter[a][i][j]

print(q)