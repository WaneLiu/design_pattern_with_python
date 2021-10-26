from __future__ import annotations
from abc import abstractclassmethod
from typing import Any

class Builder():
    """
    
    """
    @property
    @abstractclassmethod
    def product(self):
        pass
    
    @abstractclassmethod
    def produce_part_a(self):
        pass
    
    
    @abstractclassmethod
    def produce_part_b(self):
        pass
    
    @abstractclassmethod
    def produce_part_c(self):
        pass


class Product1(object):
    def __init__(self):
        self.parts = []


    def add(self, part: Any):
        self.parts.append(part)


    def list_parts(self):
        print(f"Proudct parts:{', '.join(self.parts)}")


class ConcreteBuilder1(Builder):
    """
    
    """
    def __init__(self):
        self.reset()
    
    
    def reset(self):
        self._product = Product1()

    
    @property
    def product(self):
        product = self._product
        self.reset()
        return product

    def produce_part_a(self):
        self._product.add('PartA1')


    def produce_part_b(self):
        self._product.add('PartB1')


    def produce_part_c(self):
        self._product.add('PartC1')

class Director:
    """

    """
    def __init__(self):
        self._builder = None


    @property
    def builder(self):
        return self._builder


    @builder.setter
    def builder(self, builder: Builder):
        self._builder = builder


    def build_minimal_viable_product(self):
        self.builder.produce_part_a()


    def build_full_featured_product(self):
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


if __name__ == "__main__":
    """
    
    """
    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder
    print("Stardard basic product:")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print('\n')
    print("Stardard full featured product: ")
    director.build_full_featured_product()
    builder.product.list_parts()

    print('\n')
    print("Customer product: ")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()