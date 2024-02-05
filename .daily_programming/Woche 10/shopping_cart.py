class ShoppingCart:
    def __init__(self, tax_rate=0.1, discount_rate=0.05):
        self.tax_rate = tax_rate
        self.discount_rate = discount_rate

    def calculate_subtotal(self, quantity, price):
        return quantity * price

    def calculate_tax(self, subtotal):
        return subtotal * self.tax_rate

    def calculate_discount(self, subtotal):
        return subtotal * self.discount_rate

    def calculate_total_price(self, quantity, price):
        subtotal = self.calculate_subtotal(quantity, price)
        tax = self.calculate_tax(subtotal)
        discount = self.calculate_discount(subtotal)

        total_price = subtotal + tax - discount
        return total_price

# Main code
quantity = 10
price = 20

shopping_cart = ShoppingCart()
total_price = shopping_cart.calculate_total_price(quantity, price)

print("Total price:", total_price)
