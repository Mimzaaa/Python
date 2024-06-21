def fizz_buzz(n):
    for b in range(1, n + 1):
        if b % 3 == 0:
            print("Fizz")
        elif b % 5 == 0:
            print("Buzz")
        elif b % 3 == 0 and b % 5 == 0:
            print("FizzBuzz")
        else:
            print(b)

fizz_buzz(17)
