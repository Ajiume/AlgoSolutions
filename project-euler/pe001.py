'''
If we list all the natural numbers below 10 that are multiples of 
3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

__author__ = 'SUN'

def calculate():
    cnt = 0
    for i in range(0, 1000):
        if i % 3 == 0 or i % 5 == 0:
            cnt += i
    print(cnt)

def calculate_1():
    cnt = 0
    for i in range(0, 1000, 3):
        cnt += i
    for i in range(0, 1000, 5):
        if i % 3 != 0:
            cnt += i
    print(cnt)

if __name__ == '__main__':
    calculate()
    calculate_1()
