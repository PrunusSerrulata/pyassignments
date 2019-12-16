import math

def BinarySearch(obj: int, ls: list):
    index, count = -1, 0
    ubound, lbound = len(ls) - 1, 0
    while True:
        count += 1
        mid = lbound + math.floor((ubound - lbound) / 2)
        if obj > ls[ubound]: break
        elif obj < ls[lbound]: break
        elif obj == ls[mid]:
            index = mid
            break
        elif obj > ls[mid]: lbound = mid + 1
        else: ubound = mid - 1
    return (index, count)

ls = list(range(0,33))
for i in range(0, 33):
    xls = ls.copy()
    xls.remove(i)
    print(str(i) + ": " +str(BinarySearch(i, xls)))