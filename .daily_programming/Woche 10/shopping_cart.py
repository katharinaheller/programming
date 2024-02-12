class ShoppingCart:
    def __init__(self, tax_rate=0.1, discount_rate=0.05):
        # Initialize the shopping cart with default tax rate and discount rate.
        self.tax_rate = tax_rate
        self.discount_rate = discount_rate

    def calculate_subtotal(self, quantity, price):
        # Calculate the subtotal by multiplying quantity and price.
        return quantity * price

    def calculate_tax(self, subtotal):
        # Calculate tax based on the given subtotal and the tax rate.
        return subtotal * self.tax_rate

    def calculate_discount(self, subtotal):
        # Calculate discount based on the given subtotal and the discount rate.
        return subtotal * self.discount_rate

    def calculate_total_price(self, quantity, price):
        # Calculate the total price by combining subtotal, tax, and discount.
        subtotal = self.calculate_subtotal(quantity, price)
        tax = self.calculate_tax(subtotal)
        discount = self.calculate_discount(subtotal)

        total_price = subtotal + tax - discount
        return total_price

# Main code
quantity = 10
price = 20

# Create an instance of the ShoppingCart class.
shopping_cart = ShoppingCart()

# Calculate the total price using the ShoppingCart instance.
total_price = shopping_cart.calculate_total_price(quantity, price)

# Display the total price to the user.
print("Total price:", total_price)
