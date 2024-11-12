open System

// zadanie 1
type Uzytkownik = { Waga: float; Wzrost: float }

let obliczBMI (uzytkownik: Uzytkownik) =
    let wzrostMetry = uzytkownik.Wzrost / 100.0
    let bmi = uzytkownik.Waga / (wzrostMetry * wzrostMetry)
    bmi

let kategoriaBMI (bmi: float) =
    if bmi < 18.5 then "Niedowaga"
    elif bmi >= 18.5 && bmi < 24.9 then "Waga prawidłowa"
    elif bmi >= 25.0 && bmi < 29.9 then "Nadwaga"
    else "Otyłość"

[<EntryPoint>]
let main argv =
    printf "Podaj swoją wagę w kilogramach: "
    let wagaStr = Console.ReadLine()
    
    printf "Podaj swój wzrost w centymetrach: "
    let wzrostStr = Console.ReadLine()

    let waga = float wagaStr
    let wzrost = float wzrostStr

    let uzytkownik = { Waga = waga; Wzrost = wzrost }

    let bmi = obliczBMI uzytkownik

    let kategoria = kategoriaBMI bmi

    printfn "Twoje BMI wynosi: %.2f" bmi
    printfn "Kategoria BMI: %s" kategoria

    0

// zadanie 2
let kursyWymiany =
    Map [
        ("USD", "EUR"), 0.85
        ("EUR", "USD"), 1.18
        ("USD", "GBP"), 0.75
        ("GBP", "USD"), 1.33
        ("EUR", "GBP"), 0.88
        ("GBP", "EUR"), 1.14
    ]

let przeliczKwote (kwota: float) (walutaZrodlowa: string) (walutaDocelowa: string) =
    match kursyWymiany.TryFind (walutaZrodlowa, walutaDocelowa) with
    | Some kurs -> kwota * kurs
    | None -> 
        printfn "Przelicznik dla tej kombinacji walut nie jest dostępny."
        0.0

[<EntryPoint>]
let main argv =
    printfn "Podaj kwotę do przeliczenia:"
    let kwotaStr = Console.ReadLine()
    let kwota = float kwotaStr

    printfn "Podaj walutę źródłową (np. USD, EUR, GBP):"
    let walutaZrodlowa = Console.ReadLine().ToUpper()

    printfn "Podaj walutę docelową (np. USD, EUR, GBP):"
    let walutaDocelowa = Console.ReadLine().ToUpper()

    let przeliczonaKwota = przeliczKwote kwota walutaZrodlowa walutaDocelowa

    if przeliczonaKwota > 0.0 then
        printfn "Przeliczona kwota: %.2f %s" przeliczonaKwota walutaDocelowa

    0
