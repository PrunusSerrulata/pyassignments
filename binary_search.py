import math
import random
import numpy as np


class search:
    @staticmethod
    def binarySearch(obj: int, array: list) -> int:
        lowlim, uplim = 0, len(array) - 1
        order = -1
        isDone = False

        while not isDone:
            mid = lowlim + math.ceil((uplim - lowlim) / 2)

            #print("Lower limit: " + str(lowlim) + ", Upper limit: " +
            #      str(uplim) + ", Middle: "+str(mid))

            if obj == array[lowlim]:
                order, isDone = lowlim + 1, True
            elif obj == array[uplim]:
                order, isDone = uplim + 1, True
            elif obj == array[mid]:
                order, isDone = mid + 1, True
            elif obj < array[mid]:
                if uplim == lowlim + 1:
                    isDone = True
                uplim = mid
            else:
                if uplim == lowlim + 1:
                    isDone = True
                lowlim = mid

        return order

array = sorted(list(np.random.randint(0, high=10000, size=5000)))
randnum = random.randint(0, 9999)

#print(array); print(str(randnum) + "\n")
order = search.binarySearch(randnum, array)
#print()

print("Order from method binary search: " + str(order))
print(("array[" + str(order - 1) + "] is: " + str(array[order - 1])) if order != -1 else "This array doesn't contain object number.")

# def getOrder(obj: object) -> int:
#     # Return the order of given object.

# def binarySearch(obj: object, array: list) -> int:
#     lowlim, uplim = 0, len(array)
#     order = -1
#     isDone = False

#     while not isDone:
#         mid = lowlim + math.ceil((uplim - lowlim) / 2)
#         if getOrder(obj) == array[lowlim]:
#             order, isDone = lowlim + 1, True
#         elif getOrder(obj) == array[uplim]:
#             order, isDone = uplim + 1, True
#         elif getOrder(obj) == array[mid]:
#             order, isDone = mid + 1, True
#         elif getOrder(obj) < array[mid]:
#             if uplim == lowlim + 1:
#                 isDone = True
#             uplim = mid
#         else:
#             if uplim == lowlim + 1:
#                 isDone = True
#             lowlim = mid
#     return order