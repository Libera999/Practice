def Subsets(set):
    
    allsubsets = []
    max_edge = 1<<len(set)

    for i in range(0,max_edge-1):
        subset= binary_to_set(i,set)
        allsubsets.append(subset)

    return allsubsets


def binary_to_set(x, set):

    subset={}
    index = 0

    for i in range:
        if (i and 1) == 1:
            subset.add(set.get(index))

    index+=1

    return subset