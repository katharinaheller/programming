# day 10
import time

def intro():
    print("Willkommen zur interaktiven Geschichte!")
    time.sleep(1)
    print("Du stehst vor einer entscheidenden Wahl...")
    time.sleep(1)

def make_decision(options):
    print("Wähle eine Option:")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    choice = int(input("Deine Wahl: "))
    return options[choice - 1]

def story():
    intro()
    
    decision1 = make_decision(["Gehe durch die mysteriöse Tür", "Folge dem leuchtenden Pfad"])
    
    if decision1 == "Gehe durch die mysteriöse Tür":
        print("Du betrittst einen dunklen Raum...")
        time.sleep(1)
        decision2 = make_decision(["Schalte die Taschenlampe ein", "Rufe nach Hilfe"])
        
        if decision2 == "Schalte die Taschenlampe ein":
            print("Das Licht erhellt den Raum, und du entdeckst eine alte Schatzkiste.")
            time.sleep(1)
            print("Herzlichen Glückwunsch, du hast den Schatz gefunden!")
        else:
            print("Niemand antwortet auf deinen Hilferuf. Du gehst weiter und findest einen Ausgang.")
            time.sleep(1)
            print("Du hast den Raum sicher verlassen.")
    else:
        print("Der leuchtende Pfad führt dich zu einem verzauberten Wald...")
        time.sleep(1)
        decision3 = make_decision(["Folge dem singenden Vogel", "Betritt die geheimnisvolle Höhle"])
        
        if decision3 == "Folge dem singenden Vogel":
            print("Der Vogel führt dich zu einem magischen Garten. Du erlebst eine friedliche Zeit.")
            time.sleep(1)
            print("Glückwunsch, du hast einen zauberhaften Ort entdeckt!")
        else:
            print("In der Höhle findest du eine magische Lampe. Du reibst sie und es erscheint ein Flaschengeist.")
            time.sleep(1)
            print("Der Flaschengeist gewährt dir einen Wunsch. Was wünschst du dir?")
            wish = input("Dein Wunsch: ")
            print(f"Dein Wunsch '{wish}' wird erfüllt. Viel Spaß damit!")

if __name__ == "__main__":
    story()
