Airports = {"EFNU": "Nummelan lentokenttä", "EFHK": "Helsinki/Vantaan lentokenttä",
            "EFHN": "Hankoon lentokenttä", "EFKO": "Kalajoen lentokenttä"}

Program_Running = True
while Program_Running:
    Input = input("""Kirjoita \"uusi\" jos haluat syöttää uuden kentän
Kirjoita \"olemassaoleva\" jos haluat etsiä olemassaolevista.
Kirjoita \"lopeta\" jos haluat lopettaa ohjelman käytön.
>""").lower()
    if Input == "olemassaoleva":
        Airport = input("Syötä lentokentän ICAO koodi\n").upper()
        Airport = Airport
        if Airport in Airports:
            print(f"Lentokentän {Airport} ICAO koodia vastaava lentokenttä on: {Airports[Airport]}\n")
        else:
            print(f"Lentokenttää ei löytynyt")
    elif Input == "uusi":
        Airport = input("Syötä lentokentän ICAO koodi\n")
        Airport = Airport.upper()
        AirportName = input("Syötä lentokentän nimi\n")
        Airports[Airport] = AirportName
    elif Input == "lopeta":
        Program_Running = False