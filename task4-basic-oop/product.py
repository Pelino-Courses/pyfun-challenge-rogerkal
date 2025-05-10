"""
product.py

Defines a Product class for inventory management, implementing encapsulation,
input validation, and error handling.
"""

class Product:
    """
    Represents a product in an inventory.

    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
        quantity (int): The available stock quantity.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initializes a Product instance with validated data.

        Args:
            name (str): Product name.
            price (float): Product price, must be non-negative.
            quantity (int): Quantity in stock, must be non-negative.

        Raises:
            ValueError: If price or quantity is negative.
            TypeError: If provided values are of incorrect types.
        """
        self.name = name
        self._price = None
        self._quantity = None

        self.price = price
        self.quantity = quantity

    @property
    def price(self):
        """float: Gets or sets the product's price."""
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Price must be a number.")
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = float(value)

    @property
    def quantity(self):
        """int: Gets or sets the product's quantity."""
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if not isinstance(value, int):
            raise TypeError("Quantity must be an integer.")
        if value < 0:
            raise ValueError("Quantity cannot be negative.")
        self._quantity = value

    def update_stock(self, change: int):
        """
        Updates the product's stock quantity.

        Args:
            change (int): Number to add or subtract from quantity.

        Raises:
            ValueError: If the resulting quantity would be negative.
            TypeError: If change is not an integer.
        """
        if not isinstance(change, int):
            raise TypeError("Stock change must be an integer.")
        new_quantity = self._quantity + change
        if new_quantity < 0:
            raise ValueError("Insufficient stock.")
        self._quantity = new_quantity

    def __str__(self):
        """Returns a string representation of the product."""
        return f"{self.name} - ${self.price:.2f} (Stock: {self.quantity})"
