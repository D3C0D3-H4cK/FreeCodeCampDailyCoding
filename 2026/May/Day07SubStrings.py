def get_longest_substring(s):
    mejor = ""
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            sub = s[i:j]
            if s.find(sub, i + 1) != -1:
                if len(sub) > len(mejor):
                    mejor = sub
    print(mejor)
get_longest_substring("ha ha ha ha ha ha ha")