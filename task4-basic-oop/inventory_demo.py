"""
inventory_demo.py

Demonstrates the usage of the Product class.
"""

from product import Product

def main():
    try:
        # Create product
        phone = Product("Smartphone", 699.99, 20)
        print(phone)

        # Update stock
        phone.update_stock(-3)
        print("After selling 3:", phone)

        # Modify price
        phone.price = 649.99
        print("After price drop:", phone)

        # Restock
        phone.update_stock(10)
        print("After restocking:", phone)

        # Uncomment below lines to test error handling:
        # phone.price = -50  # Should raise ValueError
        # phone.quantity = "twenty"  # Should raise TypeError
        # phone.update_stock(-100)  # Should raise ValueError

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
