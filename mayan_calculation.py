import sys
import math
ops = {"+": lambda x,y: x + y,
        "-": lambda x,y: x - y,
        "*": lambda x,y: x * y,
        "/": lambda x,y: x / y}
def prDebug(lst):
    for ii in enumerate(lst):
        print(ii, file=sys.stderr)
_map = [[] for _ in range(20)]
l, h = [int(i) for i in input().split()]
for i in range(h):
    numeral = input()
    start = 0
    for n in range(20):
        _map[n].append(numeral[start:start + l])
        start += l
s1 = int(input())
smb1 = [[] for _ in range(int(s1/l))]
for i in range(s1):
    num_1line = input()
    smb1[int(i/l)].append(num_1line)
frstNum = 0
smb1.reverse()
for ld in range(0, len(smb1)):
    pp = math.pow(20, ld)
    frstNum += (int(pp) * _map.index(smb1[ld]))
# print("1num", frstNum, file=sys.stderr)
s2 = int(input())
smb2 = [[] for _ in range(int(s2/l))]
for i in range(s2):
    num_2line = input()
    smb2[int(i/l)].append(num_2line)
# print(smb1, file=sys.stderr)
# print(smb2, file=sys.stderr)
smb2.reverse()
secNum = 0
for i in range(0, len(smb2)):
    pp = math.pow(20, i)
    secNum += (int(pp) * _map.index(smb2[i]))
operation = input()
res = ops[operation](int(frstNum), int(secNum))
# print(res, file=sys.stderr)
lres = []
if res > 20:
    last = res%20
    rr = ""
    while res > 20:
        lres.append(int(res%20))
        print("rrrr", rr, file=sys.stderr)
        res= res/20
    lres.append(int(res%20))
    lres.reverse()
    for lst in lres:
        print("\n".join(_map[lst]))
else:
    print("\n".join(_map[int(res)]))

