#!/usr/bin/env python
import cgitb
cgitb.enable()
import statistics
import math
import pymysql


def hillClimb(x, y, z):
    A, B, C = 0, 0, 0
    count = 0
    while not newMedian(B, [i + A for i in x] + [i + C for i in y]) \
            or not newMedian(C, [i + A for i in z] + [B - i for i in y]) \
            or not newMedian(A, [B - i for i in x] + [C - i for i in z]):
        B = median([i + A for i in x] + [i + C for i in y])
        C = median([i + A for i in z] + [B - i for i in y])
        A = median([B - i for i in x] + [C - i for i in z])
        count += 1
        if count > 1000:
            print("oops")
            break
    print(math.exp(B - A), math.exp(B - C), math.exp(C - A))

def median(items):
    return statistics.median(items)

def newMedian(P, v):
    v = sorted(v)
    if len(v) & 1:
        return P == median(v)
    front = median(v[1:])
    back = median(v[:-1])
    return back <= P <= front


print("Content-type: text/html")
print

conn = pymysql.connect(
	db = 'research',
	user = 'root',
	passwd = 'gators99',
	host = 'localhost')
c = conn.cursor()

c.execute("SELECT num1,num2,num3 FROM data")
lists = map(list,zip(*c.fetchall()))
hillClimb(lists[0], lists[1], lists[2])

