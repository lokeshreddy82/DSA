"""#linked list
#iam creating a node and implementing the linked list
class node:
    def __init__(self,data):
        self.leftdata=data
        self.rightdata=None
class Slinked_List:
    def __init__(self):
        self.headdata=None
        def listprint(self):
            printval=self.headdata
            while printval is not None:
                print(printval.leftdata)
                printval=printval.rightdata
list=Slinked_List()
list.headdata=node("mon")
e2=node("tue")
e3=node("wed")
list.headdata.rightdata =e2
e2.rightdata=e3
list.listprint()"""
class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   def __init__(self):
      self.headval = None

list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# Link first Node to second node
list1.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3
