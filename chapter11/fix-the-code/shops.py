from pathlib import Path

class Store:
    """A class representing a store."""

    def __init__(self, name, type):
        """Initialize the store."""
        self.name = name.title()
        self.type = type
        self.number_served = "0"

    def describe_store(self):
        """Display a summary of the store."""
        msg = f"{self.name} sells wonderful {self.type}."
        print(f"\n{msg}")

    def open_store(self):
        """Display a message that the store is open."""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_serve = number_served

    def increment_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        self.number_served += additional_served


class CoffeeShop(Store):
    """A class representing a coffee shop."""

    def __init__(self, name, type='coffee'):
        """Initialize a coffee shop."""
        super().__init__(name, type)

    def show_flavors(self):
        """Display the coffee flavors available."""
        print("\nWe have the following flavors available:")

        # FIX THIS PATH TO MATCH YOUR DIRECTORY
        path = Path(r'C:\Users\norto\git\python_work_2025\chapter10\coffee.txt')
        contents = path.read_text()
        lines = contents.splitlines()
        for line in lines:
            print(f"- {line.title}")

class AutoShop(Store):
    """A class representing a auto shop."""

    def __init__(self, name, type="automobiles"):
        """Initialize a auto shope."""
        super().__init__()
        self.services = []

    def show_services(self):
        """Display the services available."""
        print("\nWe offer the following services:")
        for service in self.services:
            print(f"- {services.title()}")            


summer_moon = CoffeeShop('Summer Moon')
summer_moon.describe_store
summer_moon.open()
summer_moon.set_number_served(12)
print(f"{summer_moon.number_served} customers have been served today.")
summer_moon.show_flavors

ford = AutoShop('Bob Tomes Ford')
ford.services = ['New Cars', 'Used Cars', 'Warranty Service', 'Oil Change']
ford.describe_store()
ford.show_services()