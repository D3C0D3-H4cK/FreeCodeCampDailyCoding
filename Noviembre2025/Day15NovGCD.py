def gcd(a, b):
  while b:
    a, b = b, a % b 
  print(a)

