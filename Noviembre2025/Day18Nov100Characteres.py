"""
100 Characters

Welcome to the 100th Daily Coding Challenge!

Given a string, repeat its characters until the result is exactly 100 characters long. If your repetitions go over 100 characters, trim the extra so it's exactly 100.

"""



def one_hundred(chars):
    string = ""
    while len(string) < 100:
        for i in chars:
            if len(string) < 100:
                string += i
    print(len(string))
    print(string)
        
    

one_hundred("One hundred ")