class Target:
    """
    Target class
    """

    def request(self):
        return 'Target: the default target\' behavior.'


class Adaptee:
    """
    Adaptee class
    """

    def specific_request(self):
        return 'Special behavior for Adaptee.'


class Adapter(Target, Adaptee):
    """

    """

    def request(self):
        return f"Adapter: (Translated) {self.specific_request()}"


def client_code(target: Target) -> None:
    """

    :param target:
    :return None:
    """
    print(target.request())


if __name__ == "__main__":
    print("Client: I can work just fine with the Target Object")
    target = Target()
    client_code(target)

    adaptee = Adaptee()
    print("Client: The Adaptee class has weird interface, I do not understand it")
    print(f"Adaptee: {adaptee.specific_request()}")

    print("Client: But I can work with it via adapter")
    adapter = Adapter()
    client_code(adapter)
    print(Adapter.__mro__)
