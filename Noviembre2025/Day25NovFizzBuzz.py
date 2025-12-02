def fizz_buzz(n):
    lista = []
    for i in range(1, n + 1):
        if i % 5 == 0 and i % 3 == 0:
            lista.append("FizzBuzz")
        elif i % 3 == 0:
            lista.append("Fizz")
        elif i % 5 == 0:
            lista.append("Buzz")
      
        else:
            lista.append(i)
    print(lista)
fizz_buzz(50)