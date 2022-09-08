kuukaudet = ("tammikuu", "helmikuu", "maaliskuu",
             "huhtikuu", "toukokuu", "kesäkuu",
             "heinäkuu", "elokuu", "syyskuu",
             "lokakuu", "marraskuu", "joulukuu")

vuodenajat = ("talveen", "kevääseen", "kesään", "syksyyn")
manyth = int(input("Mones kuukausi on kyseessä? "))
kuukausi = kuukaudet[manyth-1]
if manyth <= 2 or manyth == 12:
    vuodenaika = vuodenajat[0]
elif manyth > 2 and manyth <= 5:
    vuodenaika = vuodenajat[1]
elif manyth > 5 and manyth <= 8:
    vuodenaika = vuodenajat[2]
else:
    vuodenaika = vuodenajat[3]

print(f"{manyth}. kuukausi on {kuukausi} ja tämä on {vuodenaika} kuuluva kuukausi")