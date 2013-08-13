# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 21:20:36 2013

@author: andrew
"""

"""
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""

#Define getnext(n)

def getnext(n):
    #gets next number in the sequence
    n =  str(n)
    sums = 0
    for i in n:
        sums += int(i)**2
    return sums

def checkfor89(n):
    if n == 1:
        return False
    elif n != 89:
        n = getnext(n)
        return checkfor89(n)
    else:
        return True


def main():
    count = 0    
    for i in range(2,(10**7)):
        if checkfor89(i) == True:
            count += 1
    return count

print main()    
