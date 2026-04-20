import math
def get_pi_decimal(n):
    pi = str(math.pi)
    print(pi[:n+2])

get_pi_decimal(10)