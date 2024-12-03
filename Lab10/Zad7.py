def sprawdz_uzytkownika(uzytkownik):
    assert 'wiek' in uzytkownik, "Niepoprawny obiekt użytkownika"
    if 'wiek' in uzytkownik:
        print("Brak błędu!")


uzytkownik1 = {"imie": "Anna", "wiek": 25}
uzytkownik2 = {"imie": "Piotr"}
print(sprawdz_uzytkownika(uzytkownik1)) # Brak błędu
print(sprawdz_uzytkownika(uzytkownik2)) # AssertionError: Niepoprawny obiekt użytkownika