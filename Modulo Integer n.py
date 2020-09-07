# *** Integer Modulo n ***
"""
Integer Modulo n states that: a ≡ bmodn <-> a % n == b % n
The % (modulo) operator in Python (or other languages that supports this operator) returns the remainder.
"""


def congruence(num1, num2, modn):
    return num1 % modn == num2 % modn


"""
Question: Is 2 congruent to 4 under modulo integer 2?
Hence, we want to prove or disprove 2 ≡ 4mod2
By definition, we want to show if the remainder of 2 / 2 == 4 / 2
If so, statement is True
Otherwise, statement is False
"""
a = 2
b = 4
n = 2
print(congruence(a, b, n))

# Positive Test Case: 18 ≡ 3mod5
print(congruence(18, 3, 5))

# Negative Test Case: 17 ≡ 3mod5
print(congruence(17, 3, 5))
