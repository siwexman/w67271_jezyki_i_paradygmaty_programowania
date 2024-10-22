wagi_paczek = [10, 15, 8, 7, 20, 5, 10]
max_waga = 25


def podzielPaczki(wagi, max_waga):
    for waga in wagi:
        if waga > max_waga:
            print("Paczka o wadze ", waga, " przekrazcza max wage")

    wagi_sorted = sorted(wagi, reverse=True)
    kursy = []

    for waga in wagi_sorted:
        dodano = False
        for kurs in kursy:
            if sum(kurs) + waga <= max_waga:
                kurs.append(waga)
                dodano = True
                break
        if not dodano:
            kursy.append([waga])

    return len(kursy), kursy


print(podzielPaczki(wagi_paczek, max_waga))
liczba_kursow, kursy = podzielPaczki(wagi_paczek, max_waga)