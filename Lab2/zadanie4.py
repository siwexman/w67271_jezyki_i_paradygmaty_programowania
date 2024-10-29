import numpy as np
from functools import reduce

def polacz_macierze(lista_macierzy, operacja):
    """Łączy listę macierzy według operacji zdefiniowanej przez użytkownika."""
    def wykonaj_operacje(a, b):
        return eval(operacja)
    
    return reduce(wykonaj_operacje, lista_macierzy)

macierze = [
    np.array([[1, 2], [3, 4]]),
    np.array([[5, 6], [7, 8]]),
    np.array([[9, 10], [11, 12]])
]

print("Suma macierzy:")
print(polacz_macierze(macierze, "a + b"))

print("\nIloczyn macierzy:")
print(polacz_macierze(macierze, "a @ b"))
