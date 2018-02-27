from collections import OrderedDict

def firstUniqChar(s):
    d = {}
    for i, l in enumerate(s):
        if l in d:
            d[l][1] += 1
        else:
            d[l] = [i, 1]
    for v in d.values():
        if v[1] == 1:
            print(d)
            return(v[0])
    return -1

print("Answer: {}".format(firstUniqChar("loveleetcode")))
