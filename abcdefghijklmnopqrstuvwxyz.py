import sys
import math
import string
from collections import  deque

def debMap(_map):
    for i in _map:
        print(i, file=sys.stderr)
_map = []
n = int(input())
for i in range(n):
    m = input()
    _map.append(m)
mem = []
i = 0
j = 0
q = deque(string.ascii_lowercase)
debMap(_map)
fake = False
while q.__len__() != 0 or (i == n - 1 and j == len(m) - 1):
    q = deque(string.ascii_lowercase)
    if _map[i][j] == q[0]:
        mem = []
        locI=i
        locJ=j
        mem.append([i,j])
        q.popleft()
        fake = False
        while q.__len__() != 0 and fake == False:
            if locI > 0 and _map[locI - 1][locJ] == q[0]:
                mem.append([locI,locJ])
                q.popleft()
                locI -= 1
            elif locI + 1 < n and _map[locI + 1][locJ] == q[0]:
                mem.append([locI,locJ])
                q.popleft()
                locI += 1
            elif locJ + 1 < len(m) and _map[locI][locJ + 1] == q[0]:
                mem.append([locI,locJ])
                q.popleft()
                locJ +=1
            elif locJ > 0 and _map[locI][locJ - 1] == q[0]:
                mem.append([locI,locJ])
                q.popleft()
                locJ -=1
            else:
                fake = True
    if  q.__len__() == 0:
        mem.append([locI,locJ])
    j += 1
    if j == len(m):
        i +=1
        j = 0    
i = 0
for y in range(n):
    for x in range(len(m)):
        if [y,x] in mem:
            print(_map[y][x], end="")
        else:
            print("-", end="")
    print()
