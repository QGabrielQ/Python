
sprzet_list = [
    {
        "nazwa": "Laptop XYZ 2024",
        "producent": "XYZ Corp",
        "procesor": {
            "nazwa": "Intel Core i7",
            "generacja": "13. generacja",
            "rdzenie": 8,
            "wątki": 16,
            "taktowanie": "3.6 GHz",
            "taktowanie_max": "5.0 GHz"
        },
        "pamięć_ram": {
            "pojemność": "16 GB",
            "typ": "DDR4",
            "częstotliwość": "3200 MHz"
        },
        "dysk": {
            "typ": "SSD",
            "pojemność": "512 GB",
            "interfejs": "NVMe"
        },
        "karta_graficzna": {
            "nazwa": "NVIDIA GeForce RTX 3060",
            "ram": "6 GB",
            "typ": "GDDR6",
            "szyna": "192-bit",
            "wersja_directx": "DirectX 12"
        },
        "ekran": {
            "przekątna": "15.6 inch",
            "rozdzielczość": "1920x1080",
            "typ": "IPS",
            "odświeżanie": "144 Hz"
        },
        "bateria": {
            "pojemność": "50 Wh",
            "czas_pracy": "8 godzin",
            "typ": "Li-Ion"
        },
        "system_operacyjny": "Windows 11 Pro",
        "cena": "5999 PLN"
    },
    {
        "nazwa": "Laptop ABC Pro 2023",
        "producent": "ABC Electronics",
        "procesor": {
            "nazwa": "AMD Ryzen 9 7900X",
            "generacja": "7000-series",
            "rdzenie": 12,
            "wątki": 24,
            "taktowanie": "3.8 GHz",
            "taktowanie_max": "5.4 GHz"
        },
        "pamięć_ram": {
            "pojemność": "32 GB",
            "typ": "DDR5",
            "częstotliwość": "4800 MHz"
        },
        "dysk": {
            "typ": "SSD",
            "pojemność": "1 TB",
            "interfejs": "PCIe 4.0"
        },
        "karta_graficzna": {
            "nazwa": "AMD Radeon RX 6800M",
            "ram": "12 GB",
            "typ": "GDDR6",
            "szyna": "256-bit",
            "wersja_directx": "DirectX 12"
        },
        "ekran": {
            "przekątna": "16.0 inch",
            "rozdzielczość": "2560x1600",
            "typ": "OLED",
            "odświeżanie": "120 Hz"
        },
        "bateria": {
            "pojemność": "60 Wh",
            "czas_pracy": "10 godzin",
            "typ": "Li-Polymer"
        },
        "system_operacyjny": "Windows 10 Pro",
        "cena": "8999 PLN"
    },
    {
        "nazwa": "Laptop DEF 2022",
        "producent": "DEF Inc.",
        "procesor": {
            "nazwa": "Intel Core i5",
            "generacja": "11. generacja",
            "rdzenie": 6,
            "wątki": 12,
            "taktowanie": "2.4 GHz",
            "taktowanie_max": "4.2 GHz"
        },
        "pamięć_ram": {
            "pojemność": "8 GB",
            "typ": "DDR4",
            "częstotliwość": "2666 MHz"
        },
        "dysk": {
            "typ": "HDD",
            "pojemność": "1 TB",
            "interfejs": "SATA"
        },
        "karta_graficzna": {
            "nazwa": "Intel UHD Graphics",
            "ram": "Shared",
            "typ": "Integrated",
            "szyna": "Integrated",
            "wersja_directx": "DirectX 12"
        },
        "ekran": {
            "przekątna": "14.0 inch",
            "rozdzielczość": "1366x768",
            "typ": "LED",
            "odświeżanie": "60 Hz"
        },
        "bateria": {
            "pojemność": "40 Wh",
            "czas_pracy": "6 godzin",
            "typ": "Li-Ion"
        },
        "system_operacyjny": "Windows 10 Home",
        "cena": "2499 PLN"
    }
]
for sprzet in sprzet_list:
    print(f"Nazwa: {sprzet['nazwa']}")
    print(f"Producent: {sprzet['producent']}")
    print(f"Procesor: {sprzet['procesor']['nazwa']} ({sprzet['procesor']['generacja']})")
    print(f"Pamięć RAM: {sprzet['pamięć_ram']['pojemność']} {sprzet['pamięć_ram']['typ']}")
    print(f"Dysk: {sprzet['dysk']['pojemność']} {sprzet['dysk']['typ']}")
    print(f"Karta graficzna: {sprzet['karta_graficzna']['nazwa']}")
    print(f"Ekran: {sprzet['ekran']['przekątna']} - {sprzet['ekran']['rozdzielczość']}")
    print(f"Czas pracy na baterii: {sprzet['bateria']['czas_pracy']}")
    print(f"Cena: {sprzet['cena']}")
    print("-" * 30)
