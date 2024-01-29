def optimal_coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[amount] == float('inf'):
        return "Es gibt keine Lösung für den gegebenen Betrag."
    
    used_coins = []
    i = amount
    while i > 0:
        for coin in coins:
            if i - coin >= 0 and dp[i] == dp[i - coin] + 1:
                used_coins.append(coin)
                i -= coin
                break

    return len(used_coins), used_coins

# Beispiel mit Münzsatz 50, 10, 5, 2, 1 und Betrag 78
coins = [25, 10, 8, 1]
amount = 41
num_coins, coin_list = optimal_coin_change(coins, amount)

print(f"Der Betrag {amount} kann mit {num_coins} Münzen optimal dargestellt werden:")
print(coin_list)
