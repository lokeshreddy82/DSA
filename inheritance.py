class lokesh():
    def ganesh(self):
        print("i am brother")
class shyam():
    def bro(self):
        print("akhil")
class akhil(lokesh,shyam):
    def brother(self):
        print("i am")
s=akhil()
print(s.bro())
