import logging

# Konfigurieren des Logging-Systems
logging.basicConfig(filename='example.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def add_numbers(a, b):
    # Protokolliere, dass die Addition durchgeführt wird
    logging.info(f"Adding {a} and {b}")
    
    # Durchführung der Addition
    result = a + b
    
    # Protokolliere das Ergebnis der Addition
    logging.debug(f"Result: {result}")
    
    # Rückgabe des Ergebnisses
    return result

def main():
    # Protokolliere den Start des Programms
    logging.info("Program started")
    
    # Aufruf der add_numbers-Funktion mit den Werten 5 und 10
    result = add_numbers(5, 10)
    
    # Protokolliere das Ende des Programms
    logging.info("Program finished")
    
    # Protokolliere das endgültige Ergebnis
    logging.info(f"Final result: {result}")

# Überprüfen, ob das Skript direkt ausgeführt wird
if __name__ == "__main__":
    # Starte die main-Funktion, wenn das Skript direkt ausgeführt wird
    main()