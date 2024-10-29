import numpy as np

def wykonaj_operacje(operacja):
    """Przyjmuje string z operacją na macierzach i zwraca wynik."""
    czesci = operacja.split(";")
    typ_operacji = czesci[0].strip()
    
    macierze = [np.array(eval(m.strip())) for m in czesci[1:]]
    
    if typ_operacji == "dodaj":
        if macierze[0].shape != macierze[1].shape:
            return "Błąd: Macierze muszą mieć te same wymiary do dodawania."
        wynik = macierze[0] + macierze[1]
        
    elif typ_operacji == "mnoz":
        if macierze[0].shape[1] != macierze[1].shape[0]:
            return "Błąd: Liczba kolumn pierwszej macierzy musi się zgadzać z liczbą wierszy drugiej."
        wynik = macierze[0] @ macierze[1]
        
    elif typ_operacji == "transponuj":
        wynik = macierze[0].T
    
    else:
        return "Błąd: Nieznana operacja."
    
    return wynik

print("Dodawanie macierzy:")
print(wykonaj_operacje("dodaj; [[1, 2], [3, 4]]; [[5, 6], [7, 8]]"))

print("\nMnożenie macierzy:")
print(wykonaj_operacje("mnoz; [[1, 2, 3], [4, 5, 6]]; [[7, 8], [9, 10], [11, 12]]"))

print("\nTransponowanie macierzy:")
print(wykonaj_operacje("transponuj; [[1, 2], [3, 4]]"))
