"""Classes for melon orders."""
from random import randint

class AbstractMelonOrder:
    '''A base class that other Melon Orders will inherit from'''

    def __init__(self, species, qty, order_type, tax):
        '''Initializes the attributes of Melon Order'''

        self.species = species
        self.qty = int(qty)
        self.order_type = order_type
        self.tax = tax
        self.shipped = False

    def get_total(self):
        '''Calculates the order total to include tax'''
        base_price = self.get_base_price()

        if self.species == 'Christmas melon':   #this takes care of xmas melon
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == 'international' and self.qty < 10:
            total += 3
       #ask about how to make this go to 2 dec places  
        return round(total,2)

    def get_base_price(self):
        """Gets a random base price between 5-9"""

        return randint(5,9)

    def mark_shipped(self):
        '''Records that an order has been shipped'''

        self.shipped = True

class GovernmentMelonOrder(AbstractMelonOrder):
    '''Melon order for US Government and tells whether passed inspection'''
    tax = 0
    def __init__(self, species, qty):
        self.passed_inspection = False
        super().__init__(species, qty, "government", 0)
        
    def mark_inspection(self, passed):
        self.passed_inspection = passed


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        super().__init__(species, qty, "domestic", 0.08)

    # def __init__(self, species, qty):
    #     """Initialize melon order attributes."""

    #     self.species = species
    #     self.qty = qty
    #     self.shipped = False
    #     self.order_type = "domestic"
    #     self.tax = 0.08

    # def get_total(self):
    #     """Calculate price, including tax."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price

    #     return total

    # def mark_shipped(self):
    #     """Record the fact than an order has been shipped."""

    #     self.shipped = True


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        self.country_code = country_code
        super().__init__(species, qty, "international", 0.17)
    
    def get_country_code(self):
        """Return the country code."""

        return self.country_code



    # def __init__(self, species, qty, country_code):
    #     """Initialize melon order attributes."""

    #     self.species = species
    #     self.qty = qty
    #     self.country_code = country_code
    #     self.shipped = False
    #     self.order_type = "international"
    #     self.tax = 0.17

    # def get_total(self):
    #     """Calculate price, including tax."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price

    #     return total

    # def mark_shipped(self):
    #     """Record the fact than an order has been shipped."""

    #     self.shipped = True

    # def get_country_code(self):
    #     """Return the country code."""

    #     return self.country_code


