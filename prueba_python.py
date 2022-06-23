'''Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].'''

A = [1, 3, 6, 4, 1, 2]
def solution(A):
    # write your code in Python 3.6
    b = sorted(set(A))
    c = []
    for i in range(1, 100001):
        c.append(i)
    print("hello")
    d = []
    for i in b:
        for j in c:
            if i != j:
                d.append(i)
    print(f'esta es la lista{d}')
    e = []
    for i in d:
        if i > 0:
            e.append(i)

    f = sorted(e)
    print(f[0])
    return f[0]

solution(A)