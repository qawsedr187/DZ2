def fizz_buzz(x):
    for n in range(1, x +1):
        if n % 3 == 0:
            print('Fizz')
        elif n % 5 == 0:
            print('Buzz')
        elif n % 3 == 0 and n % 5 == 0:
            print('FizzBuzz')
        else:
            print(n)
fizz_buzz(17)
        
