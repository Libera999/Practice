""" r = int(input("r: "))
i = int(input("i: "))
c = int(input("c: "))


if i == 0:
    if r != 0:
        print(3)
    else:
        print(c)

elif i == 1:
    print(c)

elif i == 4:
    if r != 0:
        print(3)
    else:
        print(4)

elif i == 6:
    print(0)

elif i == 7:
    print(1)

else:
    print(i) """

# date - european and american
""" x, y, z = map(int, input().split())

if (x - 12)*(y - 12) < 0:
    print(1)
elif y == 12 and x >= 12:
    print(1)
elif x == 12 and y >= 12:
    print(1)
else:
    print(0) """

# triangle and point
""" d = int(input())
x, y = map(int, input().split())

if x >= 0 and y >= 0 and x+y <= d:
    print(0)

else:
    rem = [(x**2+y**2, 1), ((x-d)**2+y**2, 2), (x**2+(y-d)**2, 3)]
    print(min(rem)[1])
 """

#Andrey and acid
""" n = input()
a = list(map(int, input().split()))
test = a[:]
test.sort()

if a == test:
    print(max(a)-min(a))
else:
    print(-1) """
