# **competitive-programs**

This Repository contains

> - [**Algorithms**](https://github.com/ThayalanGR/competitive-programs#algorithms)
> - [**Challenges**](https://github.com/ThayalanGR/competitive-programs#challenges)

---

# Algorithms

**Index :-**

1. Kadanes Algorithm

---

> ## Kadanes Algorithm

Kadane's Algorithm to find Maximum Sum Subarray.
This problem, also known as Maximum Subarray Problem, is a very common question in a coding interview, and this gives the optimal answer.

```language
# kadanes algorithm to find max sum sub array

# input :-
    a array

# output :-
    max sub array

# Time complexity :-
    O(n) - linear time
    (normal bruteforce method takes O(n^2))

```

> [KadanesAlgorithm.py](https://github.com/ThayalanGR/competitive-programs/blob/master/algorithms/kadanesAlgorithm.py)

---

# Challenges

**Index :-**

1. [Magic Square](https://link)
2. [Harshad Matrix](https://link)

---

> ## Magic square

A magic square of order n is an arrangement of n^2 numbers, usually distinct integers, in a square, such that the n numbers in all rows, all columns, and both diagonals sum to the same constant. A magic square contains the integers from 1 to n^2.

The constant sum in every row, column and diagonal is called the magic constant or magic sum, M. The magic constant of a normal magic square depends only on n and has the following value:
M = n(n^2+1)/2

```language
In any magic square, the first number i.e. 1 is stored at position (n/2, n-1). Let this position be (i,j). The next number is stored at position (i-1, j+1) where we can consider each row & column as circular array i.e. they wrap around.

Three conditions hold:

1. The position of next number is calculated by decrementing row number of previous number by 1, and incrementing the column number of previous number by 1. At any time, if the calculated row position becomes -1, it will wrap around to n-1. Similarly, if the calculated column position becomes n, it will wrap around to 0.

2. If the magic square already contains a number at the calculated position, calculated column position will be decremented by 2, and calculated row position will be incremented by 1.

3. If the calculated row position is -1 & calculated column position is n, the new position would be: (0, n-2).

Example:-

Magic Square of size 3
----------------------
 2  7  6
 9  5  1
 4  3  8

```

> [magicSquare.py](https://github.com/ThayalanGR/competitive-programs/blob/master/challenges/magicSquare.py)

---

> ## Harshad Matrix

An integer number in base 10 which is divisible by sum of it digits is said to be a Harshad Number.

In our case 2 _ 2 sub matrixes should be aggregated from given n _ n matrix and each 2 _ 2 is examined to find if it is harshad matrix, for that we have to find whether all the elements in the 2 _ 2 matrix is harshad or not, if it so we will say that the matrix is harshad matrix

```language
# Harshad Matrix

# input :-
    n * n matrix

# output :-
    all 2*2 harshad matrix

# Time complexity :-
    O(n^2)
```

> [harshadMatrix.py](https://github.com/ThayalanGR/competitive-programs/blob/master/challenges/harshadMatrix.py)
