class node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class tree:

    def __init__(self):
        self.root = None
       
    def add(self, nodo, data):
        if nodo == None:
            NewNode = node(data)
            self.root = NewNode
           
        else:
            if data < nodo.data:
                if nodo.left is not None:
                    self.add(nodo.left, data)
                else:
                    nodo.left = node(data)
               
            else:
                if nodo.right is not None:
                    self.add(nodo.right, data)
                else:
                    nodo.right = node(data)

    def put(self, data):
        self.add(self.root, data)

    def show(self, root):
        if root == None:
            return
        else:
            self.show(root.left)
            print(root.data)
            self.show(root.right)

    def showTree(self):
        self.show(self.root)

 


if __name__ == "__main__":
    Mytree = tree()
    Mytree.put(7)
    Mytree.put(4)
    Mytree.put(9)
    Mytree.put(5)
    Mytree.put(1)
    Mytree.put(8)
    
    Mytree.showTree()
