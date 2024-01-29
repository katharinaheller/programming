def greedy_coin_change(coins, amount):
    coins.sort(reverse=True)  # Sortiere die Münzen in absteigender Reihenfolge

    num_coins = 0  # Zähler für die Anzahl der Münzen
    coin_list = []  # Liste zur Aufzeichnung der verwendeten Münzen

    for coin in coins:
        while amount >= coin:
            amount -= coin
            num_coins += 1
            coin_list.append(coin)

    return num_coins, coin_list

# Beispiel mit Münzsatz 50, 10, 5, 2, 1 und Betrag 78
coins = [25, 10, 8, 1]
amount = 41
num_coins, coin_list = greedy_coin_change(coins, amount)

print(f"Der Betrag {amount} kann mit {num_coins} Münzen dargestellt werden:")
print(coin_list)