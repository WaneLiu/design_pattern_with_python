from __future__ import annotations
from abc import ABC, abstractmethod


class Implementation(object):
    @abstractmethod
    def operation_implementation(self):
        pass

class ConcreteImplementationA(Implementation):
    def operation_implementation(self):
        return "ConcreteImplementationA: Here's the result on the paltform A"

class ConcreteImplementationB(Implementation):
    def operation_implementation(self):
        return "ConcreteImplementationB: here's the result on the platform B"


class Abstraction:
    """
    Abstraction
    """

    def __init__(self, implementation: Implementation):
        self.implementation = implementation


    def operation(self):
        return (f"Absctraction: Base operation with: \n"
                f"{self.implementation.operation_implementation()}")


class ExtendedAbstraction(Abstraction):
    """
    Extend Abstraction
    """

    def operation(self):
        return (f"ExtendedAbstraction: Extended operation with: \n"
                f"{self.implementation.operation_implementation()}")


def client_code(abstraction: Abstraction):
    print(abstraction.operation())


if __name__ == "__main__":
    """
    """
    implementation = ConcreteImplementationA()
    client_code(Abstraction(implementation))

    client_code(ExtendedAbstraction(ConcreteImplementationB()))
