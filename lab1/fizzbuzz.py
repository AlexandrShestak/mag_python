for x in range(2, 50, 2):
    if not x % 15:
        print 'FizzBuzz'
    elif not x % 3:
        print 'Fizz'
    elif not x % 5:
        print 'Buzz'
    else:
        print x
