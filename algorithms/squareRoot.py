# using binary search


def sqrt(n):
    low = 0.0
    high = n+1
    while ((high-low) > 0.00001):
        mid = (low+high) / 2
        if (mid*mid < n):
            low = mid
        else:
            high = mid
    return low

# using newtons raphson method


def newton(a):
    x = a
    con = 0.00001
    guess = 1.0

    while abs(pow(guess, 2) - x) >= con:
        r = x / guess + guess
        guess = r / 2

    return guess

# 24 49
print(sqrt(int(input("Enter Number : "))))
