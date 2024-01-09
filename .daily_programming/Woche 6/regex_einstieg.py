import re  # Importiere das Modul für reguläre Ausdrücke

def find_emails(text):
    """
    Diese Funktion sucht nach Email-Adressen in einem Text.

    Args:
    - text (str): Der Text, in dem nach Email-Adressen gesucht werden soll.

    Returns:
    - list: Eine Liste der gefundenen Email-Adressen.
    """
    # Definiere den regulären Ausdruck für Email-Adressen
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # Suche nach allen Übereinstimmungen im Text
    matches = re.findall(email_regex, text)

    return matches

def main():
    # Beispieltext mit Email-Adressen
    sample_text = """
    Beispieltext mit Email-Adressen:
    john.doe@example.com
    alice_smith@email.de
    contact@company.org
    """

    # Finde und zeige alle gefundenen Email-Adressen an
    email_addresses = find_emails(sample_text)
    
    if email_addresses:
        print("Gefundene Email-Adressen:")
        for email in email_addresses:
            print(email)
    else:
        print("Keine Email-Adressen gefunden.")

if __name__ == "__main__":
    main()
