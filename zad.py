import random

imena = ['Richard', 'Kevin', 'Edward', 'Debbie', 'Adam', 'Norma', 'Christopher', 'Karen', 'Tami', 'Michael', 'John',
         'Roseanna', 'Gerald', 'George', 'Vesta', 'Julie', 'Raymond', 'Janice', 'Susan', 'Kerry', 'Lorenzo', 'Holly',
         'Dan', 'Sherri', 'William', 'Karey', 'Marion', 'Melissa', 'Vincent', 'Ruby']

prezimena = ['Arnold', 'Simmons', 'Velasco', 'Canada', 'Gibbs', 'Thompson', 'Rendall', 'Harris', 'Hendon', 'Lyles',
             'Perez', 'Cleary', 'Hoyman', 'Hall', 'Baker', 'Fichter', 'Colantuono', 'Moose', 'Howard', 'Davis',
             'Nutt', 'Cornett', 'Smith', 'Lemus', 'Beltran', 'Ho', 'Cook', 'Samuels', 'Rodriguez', 'Cano']

radnici = []

# Generiranje radnika
for _ in range(15):
    ime = random.choice(imena)
    prezime = random.choice(prezimena)
    satnica = round(random.uniform(4, 6), 2)
    tjedni_sati = random.randint(20, 30)
    isplata = round(satnica * tjedni_sati, 2)

    radnik = {
        "ime": ime,
        "prezime": prezime,
        "satnica": satnica,
        "tjedni_sati": tjedni_sati,
        "isplata": isplata
    }

    radnici.append(radnik)

ukupna_isplata = sum(radnik["isplata"] for radnik in radnici)
prosjecna_isplata = round(ukupna_isplata / len(radnici), 2)

# Ispis podataka
for radnik in radnici:
    ime = radnik["ime"]
    prezime = radnik["prezime"]
    isplata = radnik["isplata"]

    print(f"Ime: {ime}\nPrezime: {prezime}\nIsplata: {isplata}\n")

print(f"Ukupna isplata: {ukupna_isplata}")
print(f"Prosjecna isplata: {prosjecna_isplata}")

# Ispis imena radnika s isplatom iznad prosjeka
print("\nRadnici s isplatom iznad prosjeka:")
for radnik in radnici:
    ime = radnik["ime"]
    prezime = radnik["prezime"]
    isplata = radnik["isplata"]

    if isplata > prosjecna_isplata:
        print(f"{ime} {prezime}")
