Airports = {"EFNU": "Nummelan lentokenttä", "EFHK": "Helsinki/Vantaan lentokenttä",
            "EFHN": "Hankoon lentokenttä", "EFKO": "Kalajoen lentokenttä"}

Input = input("Kirjoita \"uusi\" jos haluat syöttää uuden kentän; "
              "kirjoita \"olemassaoleva\" jos haluat etsiä olemassaolevista.\n")
if Input == "olemassaoleva":
    Airport = input("Syötä lentokentän ICAO koodi\n")
    if Airport in Airports:
        print(f"Lentokentän {Airport} ICAO koodia vastaava lentokenttä on: {Airports[Airport]}")
    else:
        print(f"Lentokenttää ei löytynyt")
elif Input == "uusi":
    Airport = input("Syötä lentokentän ICAO koodi\n")
    AirportName = input("Syötä lentokentän nimi\n")