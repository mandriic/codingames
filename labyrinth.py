import sys
import math
import threading
import queue

class Node:
    def __init__(self,y,x,visited=False, teleport=False, ch=""):
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        self.y = y
        self.x = x
        self.visited = visited
        self.checked = False
        self.parent = None
        self.char = ch
        self.teleport = teleport
        self.c = False
        self.distance = 0
        self.back = []
        self.cost = 0
        self.unit = False

def printMap():
    for indexR,row in enumerate(listNodes):
        for indexN,node in enumerate(row):
            print(node.char, file=sys.stderr, end=" ")
        print(file=sys.stderr)
    print("fin",file=sys.stderr)


def checkNode(node, map):
    if (map[node.y][node.x + 1] == '.' or map[node.y][node.x + 1] == 'C') and node.right is None:
        node.visited = True
        node.right = Node(node.y,node.x + 1)
        node.right.parent = node
        node.right.left = node
        node.right.distance = node.distance + 1
        node.right.cost = node.cost + 1
        if map[node.y][node.x + 1] == 'C':
            node.right.c = True
    if (map[node.y][node.x - 1] == '.' or map[node.y][node.x - 1] == 'C') and node.left is None:
        node.left = Node(node.y, node.x - 1)
        node.visited = True
        node.left.parent = node
        node.left.right = node
        node.left.distance = node.distance + 1
        node.left.cost = node.cost + 1
        if map[node.y][node.x - 1] == 'C':
            node.left.c = True
    if (map[node.y + 1][node.x] == '.' or map[node.y + 1][node.x] == 'C') and node.down is None:
        node.down = Node(node.y + 1, node.x)
        node.down.parent = node
        node.down.up = node
        node.down.distance = node.distance + 1
        node.down.cost = node.cost + 1
        if map[node.y + 1][node.x] == 'C':
            node.down.c = True
    if (map[node.y - 1][node.x] == '.' or map[node.y - 1][node.x] == 'C') and node.up is None:
        node.up = Node(node.y - 1, node.x)
        node.up = node
        node.up.down = node
        node.up.distance = node.distance + 1
        node.up.cost = node.cost + 1
        if map[node.y - 1][node.x] == 'C':
            node.up.c = True

def goBack(node, map):
    print("check", file=sys.stderr)
    if node.right == node.parent:
        print("RIGHT")
        return node.right
    elif node.left == node.parent:
        print("LEFT")
        return node.left
    elif node.up == node.parent:
        print ("UP")
        return node.up
    elif node.down == node.parent:
        print("DOWN")
        return node.down

def createNodes(all_map):
    for ind, rows in enumerate (all_map):
            print(ind ,end=" | ", file=sys.stderr)
            rowlst = []
            for let in enumerate(rows):
                print(let[0], let[1] ,end=" | ", file=sys.stderr)
                rowlst.append(Node(ind,let[0],ch=let[1]))
            listNodes.append(rowlst)
            print(file=sys.stderr)

def   update_nodes(all_map):
    for indexR,row in enumerate(listNodes):
        for indexN,node in enumerate(row):
            node.char = all_map[indexR][indexN]
            print(node.char, file=sys.stderr, end="")
        print(file=sys.stderr)
    print("fin",file=sys.stderr)

def parseNodes():
    i = 0
    while(i < r):
        i2 = 0
        while(i2 < c):
            if listNodes[i][i2].char == 'X':
                listNodes[i][i2].unit = True
            if listNodes[i][i2].char == 'T':
                listNodes[i][i2].teleport = True
            if listNodes[i][i2].char == 'C':
                listNodes[i][i2].c = True
            if i != 0:
                listNodes[i][i2].up = listNodes[i - 1][i2]
            if i2 + 1 != c:
                listNodes[i][i2].right = listNodes[i][i2 + 1]
            if i + 1 != r:
                listNodes[i][i2].down = listNodes[i + 1][i2]
            if i2 != 0:
                listNodes[i][i2].left = listNodes[i][i2 - 1]
            i2 += 1
        i+= 1
def findC(y=None,x=None,pointer=None, father=None):
    print("pointer", pointer.char, pointer, file=sys.stderr)
    if pointer.up.char == 'C' or pointer.down.char == 'C' or pointer.left.char == 'C' or pointer.right.char == 'C':
        if pointer.up.char == 'C':
            pointer.up.c = True  
        if pointer.down.char == 'C':
            pointer.down.c = True  
        if pointer.right.char == 'C':
            pointer.right.c = True  
        if pointer.left.char == 'C':
            pointer.left.c = True  
    if pointer.up.up and pointer.up.up.up and pointer.up.up.up.char == '?':
        print(pointer.up.up.up.char, file=sys.stderr)
        if pointer.up.char == "C" or (pointer.up.char == '.' and (pointer.up != pointer.parent or\
            (pointer.down.char == "#" and pointer.right.char == "#" and pointer.left.char == "#"))):
            pointer.up.parent = pointer
            print("UP")
            return False
    if pointer.left.left and pointer.left.left.left and pointer.left.left.left.char == '?':
        if pointer.left.char == "C" or (pointer.left.char == '.'and (pointer.left != pointer.parent or \
        (pointer.down.char == "#" and pointer.right.char == "#" and pointer.right.char == "#"))):
            pointer.left.parent = pointer
            print("LEFT")
            return False
    if pointer.right.right and pointer.right.right.right and (pointer.right.right.right.char == '?' ):
        if pointer.right.char == "C" or (pointer.right.char == '.'and (pointer.right != pointer.parent or \
        (pointer.down.char == "#" and pointer.up.char == "#" and pointer.left.char == "#"))):
            pointer.right.parent = pointer
            print("RIGHT")
       # findC(pointer=pointer.left, father=pointer)
    if pointer.down.down and pointer.down.down.down and pointer.down.down.down.char == '?':
        if pointer.down.char == "C" or (pointer.down.char == '.'and (pointer.down != pointer.parent or \
        (pointer.up.char == "#" and pointer.right.char == "#" and pointer.left.char == "#"))):
            pointer.down.parent = pointer
            print("DOWN")
    print("c not exists", file=sys.stderr)
    return False

def go2home():
    printMap()

def correctPrior(map):
    if map[prior[0]][prior[1]] != '?':
        if prior[0] == 2:
            prior[0] = r
        else:
            prior[0] = 2
        if prior[1] == 2:
            prior[1] = c
        else:
            prior[1] = 2
    print(prior[0], prior[1], file=sys.stderr)
    printMap()
    
def goBack(pointer):
    print(pointer,"\n" ,pointer.left,"\n", pointer.left.parent,"\n",pointer.right,"\n", pointer.right.parent, file=sys.stderr)
    if pointer.parent == pointer.left:
        pointer.visited = True
        print("LEFT")
    if pointer.parent == pointer.up:
        pointer.visited = True
        print("UP")
    if pointer.parent == pointer.right:
        pointer.visited = True
        print("RIGHT")
    if pointer.parent == pointer.down:
        pointer.visited = True
        print("DOWN")
        
def goRight(pointer):
    if (pointer.right.char != '#'and pointer.right.visited != True):
        pointer.right.parent = pointer
        pointer.visited = True
        print("RIGHT")
        return True
    else:
        return False
        
def goUp(pointer):
    if (pointer.up.char != '#' and pointer.up.visited != True):
        pointer.up.parent = pointer
        pointer.visited = True
        print("UP")
        return True
    else:
        return False
        
def goDown(pointer):
    if (pointer.down.char != '#' and pointer.down.visited != True):
        pointer.down.parent = pointer
        pointer.visited = True
        print("DOWN")
        return True
    else:
        return False
        
def goLeft(pointer):
    if (pointer.left.char != '#' and pointer.left.visited != True):
        pointer.left.parent = pointer
        pointer.visited = True
        print("LEFT")
        return True
    else:
        return False
        
def go2prior(y,x, pointer):
    if all_map[2][2] == '?':
        if goUp(pointer) == False and goLeft(pointer) == False and goDown(pointer) == False  and goRight(pointer) == False :
            goBack(pointer)
    elif all_map[2][c - 2] == '?':
        if goRight(pointer) == False and goUp(pointer) == False and goLeft(pointer) == False and goDown(pointer) == False :
            goBack(pointer)
    elif all_map[r - 2][c - 2] == '?':
        if goRight(pointer) == False and goDown(pointer) == False and goLeft(pointer) == False and goUp(pointer) == False:
            goBack(pointer)
    else:
        if goDown(pointer) == False and goLeft(pointer) == False and goRight(pointer) == False and goUp(pointer) == False:
            goBack(pointer)
            
def goTeleport(y,x,pointer, root):
    pointer.up.cost = 1
    pointer.down.cost = 1
    pointer.left.cost = 1
    pointer.right.cost = 1
    printMap()
    xm = 0
    ym = 0
    print(len(listNodes[0]), file=sys.stderr)
    cont = True
    while cont:
        ym = 0
        while ym < r - 1:
            xm = 0
            while xm  < c - 1:
                if listNodes[ym][xm].char == '?' or listNodes[ym][xm].char == '#' or listNodes[ym][xm].char == 'C' or listNodes[ym][xm].char == 'T':
                    if listNodes[ym][xm].char == 'T' and (listNodes[ym][xm].up.cost != 0 or listNodes[ym][xm].down.cost != 0\
                    or listNodes[ym][xm].right.cost != 0 or listNodes[ym][xm].left.cost != 0):
                        listNodes[ym][xm].teleport = True ########### Teleport with number
                        cont = False
                        printMap()
                        print("TELEPORT FOUNDED", file=sys.stderr)
                        return (listNodes[ym][xm])
                        break
                    listNodes[ym][xm].cost = 0
                elif listNodes[ym][xm].checked == False and listNodes[ym][xm].cost != 0:
                    if listNodes[ym][xm].up.cost == 0 and listNodes[ym][xm].up.char == '.':
                       listNodes[ym][xm].up.cost = listNodes[ym][xm].cost + 1
                    if listNodes[ym][xm].down.cost == 0 and listNodes[ym][xm].down.char == '.':
                       listNodes[ym][xm].down.cost = listNodes[ym][xm].cost + 1
                    if listNodes[ym][xm].right.cost == 0 and listNodes[ym][xm].right.char == '.':
                        listNodes[ym][xm].right.cost = listNodes[ym][xm].cost + 1
                    if listNodes[ym][xm].left.cost == 0 and listNodes[ym][xm].left.char == '.':
                        listNodes[ym][xm].left.cost = listNodes[ym][xm].cost + 1
                    listNodes[ym][xm].checked = True
                   # print(listNodes[ym][xm].char, file=sys.stderr)            
                xm += 1
            ym += 1
    print(pointer.cost, file=sys.stderr)
    print(pointer.left.cost, file=sys.stderr)
        
def makeRoot(teleport):
    min = 999
    minNode = None
    command = ""
    returnList = []
    #print(teleport.char, teleport.right.cost, teleport.left.char)
    while teleport.cost != 1:
        if teleport.right.cost < min and teleport.right.cost != 0:
            minNode = teleport.right
            returnList.insert(0,"LEFT")
            min = teleport.right.cost
        if teleport.left.cost < min and teleport.left.cost != 0:
            minNode = teleport.left
            returnList.insert(0,"RIGHT")
            min = teleport.left.cost
        if teleport.up.cost < min and teleport.up.cost != 0:
            minNode = teleport.up
            returnList.insert(0,"DOWN")
            min = teleport.up.cost
        if teleport.down.cost < min and teleport.down.cost != 0:
            minNode = teleport.down
            returnList.insert(0,"UP")
            min = teleport.down.cost
        teleport = minNode
    if teleport.right.char == 'C':
        returnList.insert(0,"LEFT")
    if teleport.left.char == 'C':
        returnList.insert(0,"RIGHT")
    if teleport.up.char == 'C':
        returnList.insert(0,"DOWN")
    if teleport.down.char == 'C':
        returnList.insert(0,"UP")
    for i in returnList:
        print(i)

r, c, a = [int(i) for i in input().split()]
print("r",r,"c",c,"a",a, file=sys.stderr)
# game loop
mapOpened = False
q = queue.Queue()
prior = [0,0]
goBackvar = False
listNodes = []
nodesCreated = False
goBackList = []
while True: # x, y for first NODE
    # kr: row where Rick is located.
    # kc: column where Rick is located.
    y, x = [int(i) for i in input().split()]
    print(y,x, file=sys.stderr)
    map = []
    if y > r/2 and x >c/2:
        prior = [2,2]
    elif y > r/2 and x < c/2:
        prior = [2, c - 2]
    elif y < r/2 and x < c/2:
        prior = [r - 2,c - 2]
    elif y < r/2 and x > c/2:
        prior = [r - 2, 2]
    else:
        prior = [2,2]
    all_map =[]
    for i in range(r):
        row = input()  # C of the characters in '#.TC?' (i.e. one line of the ASCII maze).
        all_map.append(list(row))
    if nodesCreated == False:
        createNodes(all_map)
        nodesCreated = True
        print(listNodes[6][6].char, file=sys.stderr)
    else:
        update_nodes(all_map)
    parseNodes()
    correctPrior(all_map)
    if listNodes[y][x].char == 'C':
        print("!!!!c founded!!!!", file=sys.stderr)
        root = []
        teleport = goTeleport(y,x,listNodes[y][x], root)
        makeRoot(teleport)
        print("END", file=sys.stderr)
    else:
        go2prior(y,x, pointer = listNodes[y][x])
