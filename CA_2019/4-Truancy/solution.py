def solve(content):
    maxTruancy = int(content[1])
    planning = [int(i) for i in content[2:]]
    indexedPlanning = buildTupleIndexOf(planning)
    sortedPlanning = sortByDuration(indexedPlanning)
    lessonToSkip = []
    lessonDurationSkipped = []
    for index, duration in sortedPlanning:
        nList = __insertInt(index, lessonToSkip)
        if(notConsecutive(nList, maxTruancy)):
            lessonToSkip = nList
            lessonDurationSkipped.append(duration)
    return sum(lessonDurationSkipped)

def buildTupleIndexOf(planning):
    ret = []
    for i in range(0, len(planning)):
        ret.append((i, planning[i]))
    return ret

def sortByDuration(indexedPlanning):
    return __sortByDurationTemp(indexedPlanning, [])

def __sortByDurationTemp(indexedPlanning, sortedPlanning):
    if indexedPlanning:
        return __sortByDurationTemp(indexedPlanning[1:], __insertTuple(indexedPlanning[0], sortedPlanning))
    else:
        return sortedPlanning

def __insertTuple(tuple, l):
    if not l:
        return [tuple]
    elif tuple[1] >= l[0][1]:
        return [tuple]+l
    else:
        return [l[0]] + __insertTuple(tuple, l[1:])

def __insertInt(i, l):
    if not l:
        return [i]
    elif i <= l[0]:
        return [i]+l
    else:
        return [l[0]]+ __insertInt(i, l[1:])

def notConsecutive(l, maxConsecutive):
    consecutive = 1
    last = -10
    for i in l:
        if i == last +1:
            consecutive += 1
            if consecutive == maxConsecutive+1:
                return False
        else:
            consecutive = 1
        last = i
    return True
