"""
shapes_demo.py

This script demonstrates how to use the Shape, Circle, and Rectangle classes.
Let's see how we can create shapes and calculate their area and perimeter!
"""

from shapes import Circle, Rectangle

def main():
    """Main function to demonstrate creating and using shapes."""

    try:
        # Let's create a circle with a radius of 5
        circle = Circle(5)
        print(circle)  # Shows details of the circle

        # Now, let's create a rectangle with length 10 and width 4
        rectangle = Rectangle(10, 4)
        print(rectangle)  # Shows details of the rectangle

        # Uncomment the following lines to see how errors are handled:
        # invalid_circle = Circle(-3)  # Will raise a ValueError
        # invalid_rectangle = Rectangle(0, 4)  # Will raise a ValueError

    except Exception as e:
        # In case something goes wrong, we print the error message
        print(f"Oops! Something went wrong: {e}")

if __name__ == "__main__":
    main()  # Run the demonstration
