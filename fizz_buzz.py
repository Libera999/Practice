def fizzbuzz(n):
    if n % 3 == 0:
        output = 'Fizz'
        if n % 5 == 0:
            output += 'Buzz'
    elif n % 5 == 0:
        output = 'Buzz'
    else:
        output = str(n)

    return output


print('If you want to quit, type q')
x = input('Input a number: ')

while(x != 'q'):
    print(fizzbuzz(int(x)))
    x = input('Input a number: ')
