import sys
import math
from collections import deque
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
upval = ["J", "Q", "K", "A"]
pl1 = deque()
debg1 = deque()
pl2 = deque()
debg2 = deque()

n = int(input())  # the number of cards for player 1
for i in range(n):
    cardp_1 = input()
    debg1.append(cardp_1) # the n cards of player 1
    if cardp_1[0].isdigit():
        if cardp_1[0] == 1:
            val = 10
        else:
            val = int(cardp_1[0])
    else:
        val = 10 + upval.index(cardp_1[0])
    pl1.append(val)
m = int(input())  # the number of cards for player 2
for i in range(m):
    cardp_2 = input()  # the m cards of player 2
    debg2.append(cardp_2)
    if cardp_2[0].isdigit():
        if cardp_2[0] == 1:
            val = 10
        else:
            val = int(cardp_2[0])
    else:
        val = 10 + upval.index(cardp_2[0])
    pl2.append(val)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
# print(pl1, file=sys.stderr)
# print(pl2, file=sys.stderr)
steps = 0
while pl1.__len__() != 0 and pl2.__len__() != 0:
    steps += 1
    if pl1[0] > pl2[0]:
        pl1.rotate(-1)
        # print(pl1, file=sys.stderr)
        pl1.append(pl2[0])
        pl2.popleft()
    elif pl1[0] < pl2[0]:
        pl2.rotate(-1)
        pl2.append(pl1[0])
        pl1.popleft
    elif pl1[0] == pl2[0]:
        # bank = deque()
        print("players", pl1, pl2)
        # bank.append(pl1.popleft())
        # bank.append(pl2.popleft())
        # print(bank)
        # print(pl1, pl2)
        # exit()
        p1len = pl1.__len__()
        p2len = pl2.__len__()
        start = 4
        while p1len > 0 and p2len > 0:
            p1len -= 4
            p2len -= 4
            if pl1[start] > pl2[start]:
                pl1.rotate(-start)
                while start != 0:
                    pl1.append(pl2.popleft())
                    start -= 1
                break
            elif pl1[start] < pl2[start]:
                pl2.rotate(-start)
                while start != 0:
                    pl2.append(pl1.popleft())
                    start -= 1
                break
            else:
                start += 4
                continue
        if p1len == 0 or p1len == 0:
            print("PAT")
            exit()
        # print(pl1, pl2)
        # exit()
            # if pl1.__len__()  < start - 1 or pl2.__len__() < 3:
        # print("stop")
    # pl1.popleft()
    # print("pl1", pl1, file=sys.stderr)
    # print("pl2", pl2, file=sys.stderr)
    # print(steps, file=sys.stderr)
    # exit()
if pl1.__len__() == 0:
    print("2", steps)
else:
    print("1", steps)
# print("PAT")
