while True:
    try:
        num = int(input("Bitte geben Sie eine Zahl zwischen 1 und 10 ein: "))

        if 1 <= num <= 10:
            
            if num % 2 == 0:
                print(f"{num} ist eine gerade Zahl.")
            else:
                print(f"{num} ist eine ungerade Zahl.")
            
        else:
            print("Die Zahl muss zwischen 1 und 10 liegen. Bitte versuchen Sie es erneut.")
            continue  

    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie eine ganze Zahl ein.")
        continue  

    break
