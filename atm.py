# exercitiu ATM

sold = 10.0

while True:
    print("1. Sold curent")
    print("2. Depunere")
    print("3. Extragere")
    print("4. Iesire")
    print("")

    alegere = input("Alege o optiune: ")

    if alegere == "1":
        print("Soldul tau este:", sold)
        print("")

    if alegere == "2":
        suma = float(input("Introduceti suma: "))
        sold = sold + suma
        print("Depunere reusita!")
        print("")

    if alegere == "3":
        suma = float(input("Introduceti suma: "))
        sold = sold - suma
        print("Extragere reusita!")
        print("")

    if alegere == "4":
        print("IESIRE....")
        break