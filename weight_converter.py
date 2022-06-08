weight=int(input('What is your weight?  '))
flag=input('L(lb) or K(kg)? ')
if flag.upper()=='L':
    w=weight/2.2
    print(round(w))
elif flag.upper()=='K':
    w=weight*2.2
    print(round(w))

1