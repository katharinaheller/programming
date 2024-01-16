# speed Aufgabe zu Dictonaries
# Sample transactions
transactions = [
    {"type": "Purchase", "amount": 1000, "date": "2024-01-14"},
    {"type": "Sale", "amount": 900, "date": "2024-01-14"},
    {"type": "Purchase", "amount": 500, "date": "2024-01-13"},
]

# 1. How many transactions were done yesterday?
yesterday_transactions = [t for t in transactions if ["date"] == "2024-01-14"]
num_yesterday_transactions = len(yesterday_transactions)
print(f"Number of transactions done yesterday: {num_yesterday_transactions}")

# 2. What was the total income and expense over all transactions?
total_income = sum(t["amount"] for t in transactions if t["type"] == "Sale")
total_expense = sum(t["amount"] for t in transactions if t["type"] == "Purchase")
print(f"Total income: {total_income}, Total expense: {total_expense}")
