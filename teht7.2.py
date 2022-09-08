nl = set()
user = input("Anna käyttäjänimi: ")
while user != "":
    if user in nl:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nl.add(user)
    user = input("Anna käyttäjänimi: ")
for i in nl:
    print(i)