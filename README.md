# oops-python

# OOP in Python

This repository contains examples and explanations of Object-Oriented Programming (OOP) concepts implemented in Python. It covers basic to advanced topics, demonstrating how to structure and organize Python code using classes and objects.

## Table of Contents
- [Introduction](#introduction)
- [OOP Concepts](#oop-concepts)
  - [Classes and Objects](#classes-and-objects)
  - [Encapsulation](#encapsulation)
  - [Inheritance](#inheritance)
  - [Polymorphism](#polymorphism)
  - [Abstraction](#abstraction)
- [Examples](#examples)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Object-Oriented Programming (OOP) is a programming paradigm that relies on the concept of classes and objects. OOP allows for better code reusability, scalability, and organization, making it easier to maintain and extend your code. 

This repository aims to teach the core concepts of OOP in Python with simple examples and explanations.

## OOP Concepts

### Classes and Objects
- **Class**: A blueprint for creating objects (instances).
- **Object**: An instance of a class. It has attributes (data) and methods (functions) that define its behavior.

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print(f"{self.name} makes a sound.")



Encapsulation
Encapsulation refers to the bundling of data (attributes) and methods that operate on the data into a single unit, or class, and restricting access to some of the object’s components.



class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance










Inheritance
Inheritance allows one class (child class) to inherit the properties and methods of another class (parent class).







class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Dog")

    def make_sound(self):
        print(f"{self.name} barks.")

Polymorphism
Polymorphism allows for using a unified interface to work with different types of objects. It refers to the ability to present the same interface for different data types.












def animal_sound(animal):
    animal.make_sound()

dog = Dog("Buddy")
cat = Animal("Whiskers", "Cat")

animal_sound(dog)  # Buddy barks.
animal_sound(cat)  # Whiskers makes a sound.



Abstraction
Abstraction hides the internal implementation details and shows only the essential features of an object.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)


Examples
The repository contains code examples to demonstrate the core OOP principles:

Basic class definitions and object creation
Constructor and __init__ method usage
Method overriding and inheritance
Using abstract base classes and polymorphism
Getting Started
To explore the examples, clone the repository:

git clone https://github.com/PunitTak2005/oops-python
cd oop-in-python

nstallation
Ensure you have Python 3 installed on your machine. You can download the latest version of Python here.

Usage
Run the Python scripts to see OOP concepts in action:


python classes_and_objects.py
python inheritance_example.py
python polymorphism_example.py

Contributing
Contributions are welcome! Please feel free to submit a Pull Request with improvements, additional examples, or bug fixes.

License
This project is licensed under the MIT License. See the LICENSE file for details.









