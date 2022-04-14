# 412. Fizz Buzz

# Given an integer n, return a string array answer (1-indexed) where:
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.


def fizzBuzz(number):
    array = []

    for i in range(1, number + 1):
        if i % 15 == 0:
            array.append("FizzBuzz")
        elif i % 3 == 0:
            array.append("Fizz")
        elif i % 5 == 0:
            array.append("Buzz")
        else:
            array.append(str(number))

    return array
    