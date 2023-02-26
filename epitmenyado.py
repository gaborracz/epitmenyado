telkek = list()
prices = list()

with open("utca.txt" , "r") as file:
    
    firstLine = file.readline()
    firstLine = firstLine.split()
    
    for element in firstLine:
        prices.append(int(element))
            
    for line in file:
        line = line.split()
        tempList = (int(line[0]), line[1], line[2], line[3], int(line[4]))
        telkek.append(tempList)
        

def elsoFeladat(telkek):
    print(f"2. feladat. A mintában {len(telkek)} telek szerepel.")

def masodikFeladat(telkek):
    adoszam = int(input("3. feladat. Egy tulajdonos adószáma: "))
    matchingEntries = list()
    for item in telkek:
        if item[0] == adoszam:
            matchingEntries.append(item)
    if len(matchingEntries) != 0 :
        for i in matchingEntries:
            print(f"{i[1]} utca {i[2]}")
    else:
        print("Nem szerepel az állományban.")

def ado(adosav, alapterulet):
    if adosav == "A":
        fizetendoAdo = 800 * alapterulet
    elif adosav == "B":
        fizetendoAdo = 600 * alapterulet
    elif adosav == "C": 
        fizetendoAdo = 100 * alapterulet
    
    if fizetendoAdo < 10000:
        return 0
    else:
        return fizetendoAdo

def otodikFeladat(telkek):
    savA = 0
    savB = 0
    savC = 0
    adoA = 0
    adoB = 0
    adoC = 0
    
    for element in telkek: 
        if element[3] == "A":
            savA = savA + 1
            adoA = adoA + ado(element[3], element[4])
        elif element[3] == "B":
            savB = savB + 1
            adoB = adoB + ado(element[3], element[4])
        elif element[3] == "C":
            savC = savC + 1
            adoC = adoC + ado(element[3], element[4])
    print("5. feladat:")
    print(f"A sávba {savA} telek esik, az adó {adoA} Ft.")
    print(f"B sávba {savB} telek esik, az adó {adoB} Ft.")
    print(f"C sávba {savC} telek esik, az adó {adoC} Ft.")

def hatodikFeladat(telkek):
    felulvizsgalandoUtcak = list()
    utcakA = list()
    utcakB = list()
    utcakC = list()
    
    for telek in telkek:
        if telek[3] == "A" and telek[1] not in utcakA: utcakA.append(telek[1])
        elif telek[3] == "B" and telek[1] not in utcakB: utcakB.append(telek[1])
        elif telek[3] == "C" and telek[1] not in utcakC: utcakC.append(telek[1])
    
    for i in utcakA:
        if i in utcakB:
            felulvizsgalandoUtcak.append(i)
        elif i in utcakC:
            felulvizsgalandoUtcak.append(i)
    
    for i in utcakB:
        if i in utcakC:
            felulvizsgalandoUtcak.append(i)
    
    print("6. feladat. A több sávba sorolt utcák:")
    for i in felulvizsgalandoUtcak:
        print(i)

def hetedikFeladat(telkek):
    fizetesek = {}
    
    for i in telkek:
        if i[0] not in fizetesek:
            adoszam = i[0]
            fizetendo = ado(i[3], i[4])
            fizetesek[adoszam] = fizetendo
        elif i[0] in fizetesek:
            adoszam = i[0]
            fizetendo = ado(i[3], i[4])
            jelenlegiErtek = fizetesek[adoszam]
            osszesenFizetendo = jelenlegiErtek + fizetendo
            fizetesek[adoszam] = osszesenFizetendo
            
    with open("fizetendo.txt", "w") as file:
        for key, value  in fizetesek.items():
            file.write(f"{key} {value}\n")
    
elsoFeladat(telkek)

masodikFeladat(telkek)

otodikFeladat(telkek)

hatodikFeladat(telkek)

hetedikFeladat(telkek)

