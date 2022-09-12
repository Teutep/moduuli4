Airports = {"EFNU": "Nummelan Lentokenttä", "EFHK": "Helsinki/Vantaan Lentokenttä",
            "EFHN": "Hankoon Lentokenttä", "EFKO": "Kalajoen Lentokenttä"}

Program_Running = True
while Program_Running:
    Input = input("""Kirjoita \"uusi\" jos haluat syöttää uuden kentän
Kirjoita \"olemassaoleva\" jos haluat etsiä olemassaolevista.
Kirjoita \"lopeta\" jos haluat lopettaa ohjelman käytön.
> """).lower()
    if Input == "olemassaoleva":
        Airport = input("Syötä lentokentän ICAO koodi\n").upper()
        if Airport in Airports:
            print(f"Lentokentän {Airport} ICAO koodia vastaava lentokenttä on: {Airports[Airport]}\n")
        else:
            print(f"Lentokenttää ei löytynyt\n")
    elif Input == "uusi":
        vaihe = 0
        while vaihe == 0:
            Airport = input("Syötä lentokentän ICAO koodi\n").upper()
            if Airport in Airports:
                print("Lentokentän ICAO on jo rekisteröity\n")
            else:
                vaihe += 1
        while vaihe == 1:
            AirportName = input("Syötä lentokentän nimi\n").title()
            if AirportName in Airports: #Mitenköhän tähän kannattaa määritellä arvo
                print("Lentokenttä on jo rekisteröity\n")
            else:
                vaihe += 1
        else:
            Airports[Airport] = AirportName
    elif Input == "lopeta":
        Program_Running = False