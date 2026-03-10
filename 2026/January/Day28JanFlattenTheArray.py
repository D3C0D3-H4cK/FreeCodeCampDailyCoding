numeros = []
def flatten(arr):
    for i in arr:
        if isinstance(i, list):
            flatten(i)
            
        else:
            numeros.append(i)
    


flatten(["A", [[[["B"]]]], "C"]) 