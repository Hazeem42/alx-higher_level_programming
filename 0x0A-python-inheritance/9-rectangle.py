#!/usr/bin/python3
"""defines a class Rectangle that inherits through BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


classs rectangle(BaseGeometry):
    """represent a rectangle usingBaseGeometry."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height(int): The height of the new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("heigh", height)
        self.__height = height

        def area(self):
            """Return the area of the rectangle."""
            return self.__width * self.__height

        def __str__(self):
            """Return the print() and str() representation of a Rectangle."""
            string = "[" + str(self.__class__.__name__) + "] "
            string += str(self.__width) + "/" + str(self.__height)
            return string
