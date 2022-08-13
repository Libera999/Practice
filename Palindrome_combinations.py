from itertools import permutations


def pali_combinations(str):

    list = [*str]
    mir = []

    center = False

    if len(str) == 1:  # only 1 element
        return str

    for i in list:
        print(i)
        if list.count(i) % 2 == 0:
            mir.append(i)
            list.remove(i)

        elif list.count(i) == 1 and len(str) % 2 != 0 and center == False:
            mir[len(list)//2] = i
            center = True
        # middle element
        else:
            return False  # no polidrome options

    m = (len(list)-1)//2  # half of a list
    half = mir[0:m]

    if m == 1 or m == 0:  # 2 or 3 elements in a string
        return "".join(mir)

    elif center == False:  # even length
        all_lists = permutations(m)
        print(all_lists)


s = input("Input the string: ")
pali_combinations(s)
