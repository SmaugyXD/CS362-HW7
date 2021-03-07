def FizzBuzz(n):
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 5 == 0:
        return "Buzz"
    elif n % 3 == 0:
        return "Fizz"
    else:
        return n

if __name__ == '__main__':
    for counter in range(1,101):
        print(FizzBuzz(counter))