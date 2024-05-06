from abc import ABC, abstractmethod
class computer(ABC):
    @abstractmethod
    def keyboard(self):
        pass
class laptoop(computer):
    def keyboard(self):
        print("i have many items in my bag")
class desktop(computer):
    def keyboard(self):
        print("i have no keys")
class lab(computer):
    def keyboard(self):
        print("i have lot of work")
lo=laptoop()
lo.keyboard()
so=desktop()
so.keyboard()
