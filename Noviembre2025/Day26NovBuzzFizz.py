def is_fizz_buzz(sequence):
    n = len(sequence)
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
    if lista == sequence:
        print(True)
    else:
        return False
is_fizz_buzz([1, 2, 3, 4])