import ast
__author__ = 'hanlonn'

sets = open('mediumsets.txt', 'r')

n = sets.readline()

searchSet = {53257: "a", 12546: "b", 83689: "c"}

i = 1
for set in sets.readlines():
    a, b, c = set.split(' ')
    if i in searchSet.keys():
        res = True if int(eval(searchSet[i])) == 1 else False
        print "{0} : {1}".format(searchSet[i], res)
    i += 1