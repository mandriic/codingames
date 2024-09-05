import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# width: width of the firewall grid
# height: height of the firewall grid
DEBUGR = 0
DEBUGC = 0
def printDebug():
    for i in _map:
        print(i, file=sys.stderr)
def eliminate(r,c):
    _map[r][c] = "B"
    corRD = lambda: 4 if r + 4 < h else h - r 
    corRU = lambda: 3 if r - 4 >= 0 else r
    corCR = lambda: 4 if c + 4 < w else w - c 
    corCL = lambda: 3 if c - 4 >= 0 else c

    for rr in range(r + 1, r + corRD()): 
        if _map[rr][c] == "#":
            break
        if _map[rr][c] == "@":
            _map[rr][c] = "3"
            # nodes.remove([rr,c])
    for rr in reversed(range(r - corRU(), r)):
        if _map[rr][c] == "#":
            break
        if _map[rr][c] == "@":
            _map[rr][c] = "3"
            print("ch", rr,c, file=sys.stderr)
            # nodes.remove([rr,c])
    for cc in range(c + 1, c + corCR()): 
        if _map[r][cc] == "#":
            break
        if _map[r][cc] == "@":
            _map[r][cc] = "3"
            # nodes.remove([r,cc])
    for cc in reversed(range(c - corCL(), c)):
        if _map[r][cc] == "#":
            break
        if _map[r][cc] == "@":
            _map[r][cc] = "3"
            # nodes.remove([r,cc])

    printDebug()
    # exit()
def checkNode(r,c,max):
    dwn=0
    rght=0
    lft=0
    up=0
    corRD = lambda: 4 if r + 4 < h else h - r 
    corRU = lambda: 3 if r - 4 >= 0 else r
    corCR = lambda: 4 if c + 4 < w else w - c 
    corCL = lambda: 3 if c - 4 >= 0 else c

    # corRD = lambda: 4 if r - 4 >=0 else (h-r if r + 4 > h else 3)
    corC = lambda: 3 if c - 4 >=0 and c + 4 > w else w-c
    # print(corRU(),r,h, file=sys.stderr)
    for rr in range(r + 1, r + corRD()): 
        # print(rr, file=sys.stderr)
        if _map[rr][c] == "#":
            break
        if _map[rr][c] == "@":
            dwn += 1
    # print(dwn, "DWN", file=sys.stderr)
    for rr in reversed(range(r - corRU(), r)):
        # print(rr,"rr", file=sys.stderr)
        if _map[rr][c] == "#":
            break
        if _map[rr][c] == "@":
            up +=1
    # print(up, "up", file=sys.stderr)
    for cc in range(c + 1, c + corCR()): 
        # print(rr, file=sys.stderr)
        if _map[r][cc] == "#":
            break
        if _map[r][cc] == "@":
            rght += 1
    for cc in reversed(range(c - corCL(), c)):
        # print(cc,"rr", file=sys.stderr)
        if _map[r][cc] == "#":
            break
        if _map[r][cc] == "@":
            lft +=1

    # print(r,c, "ROW COL", file=sys.stderr)
    # print(up, "up", file=sys.stderr)
    # print(dwn, "dwn", file=sys.stderr)
    # print(lft, "lft", file=sys.stderr)
    # print(rght, "rght", file=sys.stderr)
    return dwn + up + rght + lft
        
def simulator(map, rounds, bombs, max):
    
    pass

def rootine(_map, rounds, bombs, max, simulator=False):
    chk = 0
    br=False

    for l in range(h):
        for s in range(w):
            if _map[l][s] in timer:
                if _map[l][s] == "1":
                    _map[l][s] = "x"
                    nodes.remove([l,s])
                else:
                    _map[l][s] = timer[int(timer.index(_map[l][s])) + 1]
                    # print(timer.index(s))
                # print(timer[l.index(s)], file=sys.stderr)
    while max != 0 and not br and bombs != 0:
        for r in range(h):
            for c in range(w):
                if _map[r][c] not in ["@", "#", "3", "2", "1", "B"]:
                    # chk = checkNode(DEBUGR,DEBUGC,max)
                    chk = checkNode(r,c,max)
                    # print(chk, max, file=sys.stderr)
                    if chk == max:
                        print(chk, file=sys.stderr)
                        if len(walls) > len(nodes) and max == 4:
                            max-=1
                            break
                        if max < len(nodes) and bombs == 1 and rounds > 4:
                            print("WAIT")
                            br = True
                            break
                        else:
                            print(c, r)
                            eliminate(r,c)
                            print(max, file=sys.stderr)
                            br=True
                            break
            if br:
                break
        max-=1
    print(nodes, bombs, file=sys.stderr)
    printDebug()
    if not br:
        print("WAIT")
_map=[]
nodes=[]
walls = []
w,h = [int(i) for i in input().split()]
# print(w,h)
for i in range(h):
    map_row = input()
    ind = map_row.find("@")
    while ind != -1:
        nodes.append([i, ind])
        ind = map_row.find("@",ind + 1)
    wind = map_row.find("#")
    while wind != -1:
        walls.append([i, wind])
        wind = map_row.find("#",wind + 1)
        # print(ind,map_row[ind], file=sys.stderr)
    _map.append(list(map_row))
# print(nodes, file=sys.stderr)
# sim_map = _map.copy()
# print(walls)
for o in _map:
    print(o, file=sys.stderr)
print(f"{10 * '-' }END{10 * '-'}", file=sys.stderr)
timer = ["3", "2", "1"]
simulated = False
while True:
    rounds, bombs = [int(i) for i in input().split()]
    # print(rounds)
    max = len(nodes)
    if not simulated:
        simulator(_map, rounds, bombs, max)
    # if simulated:
    # max = len(nodes)
    # else:
    #     max = len(nodes) - 1
    rootine(_map, rounds, bombs, max, simulator=False)
    
