def count_letters_and_numbers(s):
    countLetter = 0
    countNumber = 0 
    for i in s:
        if i.isalpha():
            countLetter += 1
        elif i.isdigit():
            countNumber += 1
    
 
    print(f"The string has {countLetter} {'letter' if countLetter == 1 else "letters"} and {countNumber} {"number" if countNumber == 1 else "numbers" }.")


count_letters_and_numbers("helloworld123")