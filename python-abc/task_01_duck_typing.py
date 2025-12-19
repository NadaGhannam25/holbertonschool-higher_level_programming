#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Abstract base class for shapes"""
    
    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape"""
        pass


class Circle(Shape):
    """Circle class inheriting from Shape"""
    
    def __init__(self, radius):
        """Initialize a circle with given radius"""
        self.radius = radius
    
    def area(self):
        """Calculate area of circle: πr²"""
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """Calculate perimeter (circumference) of circle: 2πr"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class inheriting from Shape"""
    
    def __init__(self, width, height):
        """Initialize a rectangle with given width and height"""
        self.width = width
        self.height = height
    
    def area(self):
        """Calculate area of rectangle: width * height"""
        return self.width * self.height
    
    def perimeter(self):
        """Calculate perimeter of rectangle: 2(width + height)"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print area and perimeter of a shape using duck typing
    
    Args:
        shape: An object that implements area() and perimeter() methods
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
    
