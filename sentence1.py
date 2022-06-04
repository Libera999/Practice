sentence = "Define the most common letter in the text"
list_l = list(sentence)

set = set(list_l)

dic_max = {}
max = 0
for letter in set:

    if list_l.count(letter) >= max:
        max = list_l.count(letter)
        dic_max[letter] = list_l.count(letter)

x = [l for l, v in dic_max.items() if v == max]  # returns list
print(*x)  # unpack list into values


# for letter, value in dic_max.items():
#   if value == max:
#      print(letter)
