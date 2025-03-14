from abc import ABC, abstractmethod

class IComponent(ABC):
    @abstractmethod
    def Operation(self):
        pass

class Component(IComponent):
    def Operation(self):
        return "I am walking "

class DecoratorA(IComponent):
    def __init__(self, _component : IComponent):
        self.component = _component
    def Operation(self):
        return self.component.Operation() + "and listening to Clissic FM "


class DecoratorB(IComponent):

    def __init__(self, _component : IComponent):
        self.component = _component
        self.state = "past the Coffee Shop "

    def Operation(self):
        return self.component.Operation() + "to school "
    
    def AddedBehavior(self):
        return "and I bought a cappuccino"


if __name__ == "__main__":

    def Display(s, IComponent):
        print(s + IComponent.Operation())

    component= Component()
    Display("1. Basic Component : ", component)
    Display("2. A Decorated : ", DecoratorA(component))
    Display("3. B Decorated : ", DecoratorB(component))
    Display("4. B-A Decorated : ", DecoratorB(DecoratorA(component)))
    b = DecoratorB(component)
    Display("4. A-B Decorated : ", DecoratorA(b))
    # Adding State and Behaviour
    print(f"\t\t {b.state} + {b.AddedBehavior()}")

