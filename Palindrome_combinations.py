# all possible palindrome combinations from a string

from itertools import permutations


def pali_combinations(str):

    list = [*str]
    mir = []
    palindromes = []  # final set of palindromes
    center = False

    if len(str) == 1:  # only 1 element
        return str

    while list:

        i = list[0]

        if list.count(i) % 2 == 0:
            mir.append(i)
            list.remove(i)
            list.remove(i)

        elif list.count(i) == 1 and len(str) % 2 != 0 and not center:
            c_elem = i  # preserve middle element
            center = True
            list.remove(i)

        else:
            return False  # no polidrome options

    all_lists = set(permutations(mir))  # delete all duplicates

    for p in all_lists:

        print(p)
        p_l = [*p]

        inverted = [p_l[len(p_l)-1-i] for i in range(len(p_l))]

        if center:  # middle element
            p_l.append(c_elem)

        s = "".join(p_l+inverted)
        palindromes.append(s)

    return palindromes


s = input("Input the string: ")
print(pali_combinations(s))
