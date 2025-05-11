"""
shapes.py

This module defines a base class called Shape, and two derived classes: Circle and Rectangle.
Each shape has methods for calculating area and perimeter, and each class has basic validation.
Let's make geometry fun!
"""

import math

class Shape:
    """
    A basic class representing any geometric shape.

    This class can be used as a blueprint for specific shapes like Circle and Rectangle.
    Every shape has an area and perimeter that we can calculate, but each shape will
    calculate them in its own way (hence, we "inherit" and "override" methods in subclasses).
    """

    def __init__(self, shape_name: str):
        """
        Initializes a Shape with a name.

        Args:
            shape_name (str): Name of the shape (e.g., 'Circle', 'Rectangle').
        
        Raises:
            ValueError: If the shape name is an empty string.
            TypeError: If the shape name is not a string.
        """
        if not isinstance(shape_name, str):
            raise TypeError("Shape name must be a string.")
        if not shape_name:
            raise ValueError("Shape name cannot be empty.")
        self.shape_name = shape_name

    def area(self):
        """Each shape calculates its own area. This method will be overridden."""
        raise NotImplementedError("You need to define how to calculate the area in each subclass!")

    def perimeter(self):
        """Each shape calculates its own perimeter. This method will be overridden."""
        raise NotImplementedError("You need to define how to calculate the perimeter in each subclass!")

    def __str__(self):
        """String representation of the shape."""
        return f"{self.shape_name} is a wonderful shape!"

class Circle(Shape):
    """
    Represents a circle, a specific shape that has a radius.

    The area and perimeter (circumference) are calculated based on the radius.
    """

    def __init__(self, radius: float):
        """
        Creates a Circle object.

        Args:
            radius (float): The radius of the circle. Must be positive.

        Raises:
            ValueError: If the radius is less than or equal to zero.
            TypeError: If the radius is not a number.
        """
        super().__init__("Circle")
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a number.")
        if radius <= 0:
            raise ValueError("Radius must be greater than zero.")
        self.radius = radius

    def area(self):
        """Calculates the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculates the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius

    def __str__(self):
        """A string representation of the circle, showing its details."""
        return f"Circle: radius={self.radius}, area={self.area():.2f}, perimeter={self.perimeter():.2f}"

class Rectangle(Shape):
    """
    Represents a rectangle, a shape with length and width.

    The area and perimeter are calculated using the rectangle's dimensions.
    """

    def __init__(self, length: float, width: float):
        """
        Creates a Rectangle object.

        Args:
            length (float): The length of the rectangle. Must be positive.
            width (float): The width of the rectangle. Must be positive.

        Raises:
            ValueError: If either length or width is less than or equal to zero.
            TypeError: If length or width is not a number.
        """
        super().__init__("Rectangle")
        if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
            raise TypeError("Length and width must be numbers.")
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must both be greater than zero.")
        self.length = length
        self.width = width

    def area(self):
        """Calculates the area of the rectangle."""
        return self.length * self.width

    def perimeter(self):
        """Calculates the perimeter of the rectangle."""
        return 2 * (self.length + self.width)

    def __str__(self):
        """A string representation of the rectangle, showing its details."""
        return f"Rectangle: length={self.length}, width={self.width}, area={self.area():.2f}, perimeter={self.perimeter():.2f}"
