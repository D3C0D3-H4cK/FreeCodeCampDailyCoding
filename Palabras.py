def is_pangram(sentence, letters):
    minuscula = sentence.lower()
    return all(letra in minuscula for letra in letters.lower())
is_pangram("hello", "helo")
print(is_pangram("hello", "hel"))