def subsets(in_set):
    
    allsubsets = []
    max_edge = 1<<len(in_set)

    for i in range(0,max_edge-1):
        subset= binary_to_set(i,in_set)
        allsubsets.append(subset)

    return allsubsets


def binary_to_set(iteration, input_set):

    subset=[]
    i = 0
    index=iteration

    while index>0:
        if (index and 1) == 1:
            subset.append(input_set[i])
        i+=1
        index>>=1

    return subset

set_1=[12,2]
print(subsets(set_1))
