from itertools import permutations


def pali_combinations(str):

    list = [*str]
    mir = []
    palindromes = []  # final set of palindromes
    center = False

    if len(str) == 1:  # only 1 element
        return str

    for i in list:
        # print(i)

        if list.count(i) % 2 == 0:
            mir.append(i)
            list.remove(i)
            list.remove(i)

        elif list.count(i) == 1 and len(str) % 2 != 0 and not center:
            c_elem = i  # preserve central element
            center = True

        else:
            return False  # no polidrome options

    # print(mir)

    all_lists = permutations(mir)

    for p in all_lists:

        p_l = [*p]
        if center:
            p_l.append(c_elem)

        inverted = [p_l[len(p_l)-1-i] for i in range(len(p_l))]

        s = "".join(p_l+inverted)
        palindromes.append(s)

    return palindromes


s = input("Input the string: ")
print(pali_combinations(s))
