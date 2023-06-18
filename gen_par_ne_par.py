def generiraj_parni_neparni(parametar):
    return [(broj, 'paran') if broj % 2 == 0 else (broj, 'neparan') for broj in range(parametar)]

rezultat = generiraj_parni_neparni(10)
for broj, parnost in rezultat:
    print(f"Broj {broj} je {parnost}.")
