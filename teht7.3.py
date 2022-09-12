Airports = {"EFNU": "Nummelan lentokenttä", "EFHK": "Helsinki/Vantaan lentokenttä",
            "EFHN": "Hankoon lentokenttä", "EFKO": "Kalajoen lentokenttä"}

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
            print(f"Lentokenttää ei löytynyt")
    elif Input == "uusi":
        Airport = input("Syötä lentokentän ICAO koodi\n").upper()
        AirportName = input("Syötä lentokentän nimi\n").title()
        if Airport in Airports or AirportName in Airports:
            print("ICAO-koodi tai lentokenttä löytyy jo hakemistosta\n")
        else:
            Airports[Airport] = AirportName
    elif Input == "lopeta":
        Program_Running = False