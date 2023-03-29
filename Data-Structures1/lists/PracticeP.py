class node:
    def __init__(self, data):
        self.data = data    
        self.next = None

class list:
    def __init__(self):
        self.head = None
    
    def add(self, data):
        if self.head == None:
            NewOne = node(data)
            self.head = NewOne
        else:
            aux = self.head
            while aux.next is not None:
                aux = aux.next
            NewNode = node(data)
            aux.next = NewNode
    
    def show(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

if __name__ == "__main__":
    NewList = list()
    NewList.add(6)
    NewList.add(5)
    NewList.add(9)
    NewList.add(3)
    NewList.add(55)

    NewList.show()
    print("-----")
    print(NewList.head.data)