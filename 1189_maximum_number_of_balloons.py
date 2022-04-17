# 1189. Maximum Number of Balloons

# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
# You can use each character in text at most once. Return the maximum number of instances that can be formed.

def maxNumberOfBalloons(text):

    dictionary = {'b':0, 'a':0, 'l':0, 'o':0, 'n':0}
    for i in text:
        if i in dictionary:
            dictionary[i] += 1
    
    dictionary['l'] = dictionary['l'] // 2
    dictionary['o'] = dictionary['o'] // 2
    return min(dictionary['b'], dictionary['a'], dictionary['l'], dictionary['o'], dictionary['n'])


def maxNumberOfBalloons_2(text):
    expected = {'b':1, 'a':1, 'l':2, 'o':2, 'n':1}

    counts = {}
    for c in text:
        if c not in counts:
            counts[c] = 0
        counts[c] += 1

    for c in expected:
        if c not in counts:
            return 0

    result = 0
    while True:
        for c in expected:
            counts[c] -= expected[c]
            if counts[c] < 0:
                return result
        result += 1


print(maxNumberOfBalloons("alloonsalloonsalloonsalloonsbbnaloooo"))
print(maxNumberOfBalloons_2("alloonsalloonsalloonsalloonsbbnaloooo"))
