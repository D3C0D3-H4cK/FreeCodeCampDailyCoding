def is_valid_domino_chain(dominoes):
    if dominoes[0][0] == dominoes[::-1][0]:
        return False
    else:
        primernumero = dominoes[1][0]
        for i in dominoes:
            i[1] != [primernumero]
            primernumero = i[i+1]
            

is_valid_domino_chain([[1, 3], [3, 6], [6, 5]])