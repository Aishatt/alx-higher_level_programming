#!/usr/bin/python3
"""Rectangle class
Defines a Rectangle class.
"""

class Rectangle:
    """Rectangle class defined by width and height."""

    def __init(self, width=0, height=0):
        self.width = width
        self.height=height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value,int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >=0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self,value):
        if not isinstance(value,int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >=0")
        self.height = value