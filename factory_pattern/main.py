from __future__ import annotations
from abc import ABC, abstractclassmethod

class Creator(ABC):
    """
    The Creator class declares
    """

    @abstractclassmethod
    def factory_method(self):
        pass


    def some_operation(self) -> str:
        """
        Also note
        :param self:
        :return str:
        """
        product = self.factory_method()
        result = f"Creator: The same creator's code has just worked with {product.operation()}"
        return result

class ConcreteCreator1(Creator):
    def factory_method(self):
        return 