from abc import ABC, abstractmethod
import random

class IStrategy:
    @abstractmethod
    def Move(self, _context):
        pass

class Strategy1(IStrategy):
    def Move(self, _context):
        return _context.Counter + 1

class Strategy2(IStrategy):
    def Move(self, _context):
        return _context.Counter - 1

class Context:
    def __init__(self):
        self.start = 5
        self.Counter = 5
        self.strategy = Strategy1()


    def Algorithm(self):
        return self.strategy.Move(self)

    def SwitchStrategy(self):
        if isinstance(self.strategy, Strategy1):
            self.strategy = Strategy2()
        else:
            self.strategy = Strategy1()


if __name__ == "__main__":
    print("Running App")
    context = Context()
    context.SwitchStrategy()
    r = random.randint(0,37)
    for i in range(context.start, context.start+15):
        if r == 2:
            print("|| ")
            context.SwitchStrategy()
        print(context.Algorithm())
    
