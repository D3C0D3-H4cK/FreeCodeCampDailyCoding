"""

A prime number is a positive integer greater than 1 that is divisible only by 1 and itself. The first five prime numbers are 2, 3, 5, 7, and 11.

Given a positive integer n, return the nth prime number. For example, given 5 return the 5th prime number: 11.
"""

def nth_prime(n):
    contador = 0
    numero = 2 
    
    while contador < n:
        primo = True
        for i in range(2,numero ):
            if numero % i == 0:
                primo = False
        if primo:
            print(numero)
            contador +=1
                
        numero +=1 
    print(numero -1)
nth_prime(5)