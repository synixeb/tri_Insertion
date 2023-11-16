import random

def generate_tab(n : int)->[int]:
    tab = []
    for i in range(n):
        tab.append(random.randint(0, max))
    return tab

def ordre_croissant(T: [int])->[int]:
    for i in range(len(T)):
        for j in range(i, len(T)):
            if T[i] > T[j]:
                T[i], T[j] = T[j], T[i]
    return T