import sys
import math
from collections import deque
import re
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def split_digits_letters(s):
    return re.findall(r'\d+|\D+', s)
upval = ["J", "Q", "K", "A"]
pl1 = deque()
debg1 = deque()
pl2 = deque()
debg2 = deque()

n = int(input())  # the number of cards for player 1
for i in range(n):
    cardp_1 = input()
    debg1.append(cardp_1)
    # print(split_digits_letters(cardp_1)) # the n cards of player 1
    if len(split_digits_letters(cardp_1)) == 2:
        val = int(split_digits_letters(cardp_1)[0])
    else:
        val = 11 + upval.index(cardp_1[0])
    pl1.append(val)
m = int(input())  # the number of cards for player 2
for i in range(m):
    cardp_2 = input()  # the m cards of player 2
    debg2.append(cardp_2)
    if len(split_digits_letters(cardp_2)) == 2:
        val = int(split_digits_letters(cardp_2)[0])
    else:
        val = 11 + upval.index(cardp_2[0])
    pl2.append(val)
# print(debg1)
# print(debg2)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
# print(pl1, file=sys.stderr)
# print(pl2, file=sys.stderr)
steps = 0
while pl1.__len__() != 0 and pl2.__len__() != 0:
    steps += 1
    if pl1[0] > pl2[0]:
        # print("p1 wins with", pl1)
        # print("p2 lose with", pl2)
        pl1.rotate(-1)
        pl1.append(pl2.popleft())
        # print("p1 wins end", pl1)
        # print("p2 end", pl2)
        # exit()
    elif pl1[0] < pl2[0]:
        # print("p2 wins with", pl1)
        # print("p2 lose with", pl2)
        pl2.append(pl1.popleft())
        pl2.rotate(-1)
        # print("p1 wins end", pl1)
        # print("p2 end", pl2)
        # exit()
    elif pl1[0] == pl2[0]:
        st = 4
        while 1:
            # print("len1 ", pl1.__len__(), "len2", pl2.__len__(), st)
            # print("st", st, pl1, pl2)
            if pl1.__len__() < st + 1 or pl2.__len__() < st + 1:
                print("PAT")
                exit()
            if pl1[st] > pl2[st]:
                # print(st, "p1st", pl1)
                # print(st, "p2st",pl2)
                pl1.rotate(-(st + 1))
                mm = st
                while mm + 1 != 0:
                    pl1.append(pl2.popleft())
                    mm -= 1
                # print(st,"p1end", pl1)
                # print(st, "p2end", pl2)
                # exit()
                # # print(pl1, file=sys.stderr)
                # print(pl2, file=sys.stderr)
                # exit()
                break
            if pl1[st] < pl2[st]:
                # print(st, "SECp1st", pl1)
                # print(st, "SECp2st",pl2)
                mm = st
                while mm + 1 != 0:
                    pl2.append(pl1.popleft())
                    mm -= 1
                pl2.rotate(-(st + 1))
                # print(st, "SECp1st", pl1)
                # print(st, "SECp2st",pl2)
                break
            if pl1[st] == pl2[st]:
                print("dCh", file=sys.stderr)
                # print("p1",pl1, file=sys.stderr)
                # print("p2", pl2, file=sys.stderr)
                st += 4
            else:
                print("ERROR")
                exit()
        # print("exited")
    # print("p1",pl1, file=sys.stderr)
    # print("p2", pl2, file=sys.stderr)

            # exit()
if pl1.__len__() == 0:
    print("2", steps)
else:
    print("1", steps)
# print("PAT")
