# 7. Reverse Integer
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value 
# to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


def reverse(self, x: int) -> int:
    temp = x
    if temp < 0:
        temp *= -1
    reverse = 0
    while temp > 0:
        reminder = temp % 10
        reverse = reverse * 10 + reminder
        temp = temp // 10
    
    if reverse > 2**31 -1:
        return 0
    elif x < 0:
        return -1 * reverse
    else:
        return reverse

        