def generuj_i_uruchom_kod(szablon, dane_wejsciowe):
    """Generuje i uruchamia kod na podstawie szablonu i danych wejściowych."""
    try:
        kod = szablon.format(**dane_wejsciowe)
    except KeyError as e:
        return f"Błąd: Brakujący fragment kodu dla zmiennej {e}"

    try:
        skompilowany_kod = compile(kod, "<string>", "exec")
        exec(skompilowany_kod, globals())
    except SyntaxError as e:
        return f"Błąd składniowy: {e}"
    except Exception as e:
        return f"Błąd wykonania kodu: {e}"

    return "Kod został pomyślnie wygenerowany i uruchomiony."

szablon = """
def funkcja(x):
    return x + {wartosc_dodawana}
print(funkcja({argument}))
"""

dane_wejsciowe = {
    "wartosc_dodawana": 3,
    "argument": 5
}

print(generuj_i_uruchom_kod(szablon, dane_wejsciowe))
