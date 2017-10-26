# Swift Navigation Application Coding Test
# Author: Daniel Hunter
# Date: Oct 26 2017

from math import sqrt
import timeit # used for runtime testing


def fibonacci(n):
    '''Returns a list of the first n Fibonacci numbers.'''
    fibs = [0]*n
    fibs[1] = 1 # set up the initial sequence of 0, 1
    for i in range(2, n):
        fibs[i] = fibs[i - 1] + fibs[i - 2]
    return fibs # this algorithm adopts the modern usage of adding 0 to the 
    # beginning of the sequence: 0, 1, 1, 2, 3, 5, etc.

def createPrimeLookupTable(n):
    '''Returns a list of booleans of length n + 1, each value representing the 
    primality of the index.
    Ex: primes[4] -> false 
        primes[5] -> true

    Uses the Sieve of Eratosthenes algorithm.'''
    n = n + 1 # n includes 0, so add one to actually get the first 'n' primes
    primes = [True]*(n)
    primes[0] = primes[1] = False
    for i in range(2, int(sqrt(n))):
        if primes[i] == True:
            for j in range(i*i, n, i):
                primes[j] = False
    return primes

def printFibonacci(n):
    '''Prints the first Fibonacci numbers according to the following rules:
    Print:
    "BuzzFizz" when F(n) is prime.
    "FizzBuzz" when F(n) is divisible by 15.
    "Buzz" when F(n) is divisible by 3.
    "Fizz" when F(n) is divisible by 5.
    the value F(n) otherwise.
    '''
    fibs = fibonacci(n)
    primes = createPrimeLookupTable(fibs[n-1]) # the nth Fibonacci number is 
    # at fibs[n-1], so the prime lookup table needs to be based on that
    for i in fibs:
        if primes[i]:
            print('BuzzFizz')
        else:
            print('Fizz' * (i % 5 == 0) + 'Buzz' * (i % 3 == 0) or str(i))

if __name__ == '__main__':
    start = timeit.default_timer()
    printFibonacci(35)
    stop = timeit.default_timer()
    print('This program took', stop - start, 'seconds')