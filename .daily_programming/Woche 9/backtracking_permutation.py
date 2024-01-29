def backtrack(perm, choices):
    # Wenn es keine weiteren Entscheidungen gibt, haben wir eine vollständige Permutation
    if not choices:
        print(perm)
    else:
        # Durchlaufe alle verbleibenden Entscheidungen
        for i in range(len(choices)):
            # Wähle eine Option aus den verbleibenden Entscheidungen
            new_perm = perm + [choices[i]]

            # Entferne die ausgewählte Option aus den verbleibenden Entscheidungen
            new_choices = choices[:i] + choices[i+1:]

            # Rufe die Backtrack-Funktion rekursiv mit der neuen Permutation und den verbleibenden Entscheidungen auf
            backtrack(new_perm, new_choices)

if __name__ == "__main__":
    # Hier die gewünschten Elemente einfügen
    elements = [ 2, 4, 6]  
    # Starte das Backtracking mit einer leeren Permutation und allen Elementen als verbleibende Entscheidungen
    backtrack([], elements)
