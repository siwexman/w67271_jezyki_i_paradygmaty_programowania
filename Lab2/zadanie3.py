def analiza_danych(dane):
    liczby = list(filter(lambda x: isinstance(x, (int, float)), dane))
    napisy = list(filter(lambda x: isinstance(x, str), dane))
    krotki = list(filter(lambda x: isinstance(x, tuple), dane))

    najwieksza_liczba = max(liczby) if liczby else None
    najdluzszy_napis = max(napisy, key=len) if napisy else None
    najdluzsza_krotka = max(krotki, key=len) if krotki else None

    return najwieksza_liczba, najdluzszy_napis, najdluzsza_krotka

dane = [42, "napis", (1, 2, 3), [1, 2], 3.14, "najdluzszy napis", (1,), {1: "a"}, 99]
print(analiza_danych(dane))
