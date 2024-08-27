import sys

def draw_revdiag(i, size, map, finmap):
    for l in range(size + 1):
        # print(l, file=sys.stderr)
        step = l - 1
        if step < 0:
            continue
        checkWord = ""
        for let in range(0, l):
            # print(map[let][step], end=" ")
            checkWord += map[let][step]
            step -= 1
        # print("cw", checkWord)
        src = checkWord.find(w[::-1])
        if src != -1:
            # print(src, l, w, checkWord, file=sys.stderr)
            rev = checkWord[::-1].find(w)
            for i in range(len(w)):
                # finmap[l - 1 - i][rev + i] = map[l - 1 - i][rev + i]
                finmap[src + i][l - src - i - 1] = map[src + i ][l - src - i - 1]
        src = checkWord.find(w)
        if src != -1:
            for i in range(len(w)):
                # print( map[src + i][l - i - 1] )
                finmap[src + i][l - src - i - 1] = map[src + i ][l - src - i - 1] 
    for l2 in (range(1,size)): #diag from [0][1], [1][2], [2][3]...
        hstep = size - 1
        checkWord = ""
        for let in range(l2, size):
            checkWord += map[let][hstep]
            # print(map[vstep][let], end= " ")  
            hstep -= 1
        # print(checkWord)
        src = checkWord.find(w[::-1])
        if src != -1:
            # print(src, l2, w, checkWord, len(w), file=sys.stderr)
            # rev = checkWord[::-1].find(w)
            for i in range(len(w)):
                # print(map[l2 + src + i][size - src - i])
                finmap[l2 + src + i][size - 1 - src - i] = map[l2 + src + i][size - 1 - src - i]
        src = checkWord.find(w)
        if src != -1:
            # print("src", src, "l2", l2, w, checkWord, file=sys.stderr)
            for i in range(len(w)):
                # print(map[l2 + i][src  -  i] )
                finmap[src + l2 + i][size - 1 - src - i] = map[src + l2 + i][size - 1 - src  -  i] 

def draw_diag(ind, size, map, finmap):
    for l in reversed(range(size)):
        step = 0
        checkWord = ""
        for let in range(l, size):
            # print(map[let][step], end=" ")
            checkWord += map[let][step]
            step += 1
        # print("cw", checkWord.find(w))
        src = checkWord.find(w[::-1])
        if src != -1:
            print(w, l, src, checkWord, file=sys.stderr)
            for i in range(len(w[::-1])):
                finmap[l + src + i][src + i] = map[l + src + i][src + i]
        src = checkWord.find(w)
        if src != -1:
            # print(w, l, src, checkWord)
            for i in range(len(w)):
                # print(map[l + i][src + i], file=sys.stderr, end=" ")
                finmap[l + src + i][src + i] = map[l + src + i][src + i] 
    for l2 in (range(1,size)): #diag from [0][1], [1][2], [2][3]...
        vstep = 0
        checkWord = ""
        for let in range(l2, size):
            checkWord += map[vstep][let]
            # print(map[vstep][let], end= " ")  
            vstep += 1
        src = checkWord.find(w[::-1])
        if src != -1:
            rev = checkWord[::-1].find(w)
            # print(src, l2, w, checkWord, file=sys.stderr)
            # print(map[src][l2])
            for i in range(len(w)):
                finmap[src + i][src + l2 + i] = map[src + i][src + l2 + i]
        src = checkWord.find(w)
        if src != -1:
            # print(src, l2, w, checkWord, file=sys.stderr)
            for i in range(len(w)):
                finmap[src + i][src + l2 + i] = map[src + i][src + l2 + i] 

def draw_hor(ind, line, lenght, finmap, map, tp):
    if tp == "hor":
        for i in range(lenght):
            # print("map i", map[line], file=sys.stderr)
            finmap[line][ind + i] = map[line][ind + i]
            # print(ind, line, finmap[line][ind + i])
    # print(w[ind])
    # finmap[line][0] = 1
def draw_vert(ind, size, map, finmap):
    for _ in range(size):
        ver = ''.join([s[ind] for s in map]).find(w) # make strings from vert lines and search word
        rever = ''.join([s[ind] for s in map]).find(w[::-1])
        if ver != -1 or rever != -1:
            if ver != -1:
                for l in range(len(w)):
                    finmap[ver + l][ind] = map[ver + l][ind]   # here foo for print vert lines
            else:
                for l in range(len(w)):
                    finmap[rever + l][ind] = map[rever + l][ind]   # here foo for print vert lines
                    # print(rever, i, ''.join([s[i] for s in reversed(map)]),"rever")
size = int(input())
map = []
words = []
for i in range(size):
    row = input()
    map.append(row)
clues = (input().upper()).split(" ")
for i in clues:
    print(i, file=sys.stderr)
# print(clues, file=sys.stderr)
sum = ""
for i in map:
    print(list(i), file=sys.stderr)
    # print("", file=sys.stderr)
finmap = [[' ' for _ in range(size)] for _ in range(size)]
# print(size)
for i in range(size):
    for w in clues:
        norm = map[i].find(w)
        rev = map[i].find(w[::-1])
        # print(verrev, i)
        if norm != -1 or rev != -1:
            if norm != -1:
                draw_hor(norm, i, len(w), finmap, map, "hor")
            else:
                draw_hor(rev, i, len(w), finmap, map, "hor")
        draw_vert(i, size, map, finmap)
        draw_diag(i, size, map, finmap)
        draw_revdiag(i, size, map, finmap)
for i in finmap:
    print("".join(i))
# print()