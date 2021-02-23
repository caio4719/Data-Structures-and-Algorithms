# Caio Beraldi Ribeiro 

from stacks import LinkedNode

class LinkedStack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if (self.head == None):
            return True
        else:
            False


    def push_clone(self, datum):
        if(self.head == None):
            self.head = LinkedNode(datum)
            print("Dado inserido:", datum)
        else:
            newNode = LinkedNode(datum)
            newNode.next = self.head
            self.head = newNode
            print("Dado inserido:", datum)


    def pop_clone(self):
        if (self.isEmpty()):
            return print("Tem nada não cpx")
        else:
            poppedNode = self.head
            self.head = self.head.next
            poppedNode.next = None
            return print("Dado retirado do topo:", poppedNode.datum)
       
        
    def destroy_stack(self):
        self.head = - 1

    def print_head(self):
        if (self.isEmpty()):
            return print("Tem nada não cpx")
        else:
            return print("Dado no topo:", self.head.datum)

    def update_head(self, datum):
        if (self.isEmpty()):
            return print("Tem nada não cpx")
        else:
            self.head.datum = datum
            print("Atulizado com sucesso!")

    def print_all_stack(self):
        auxNode = self.head
        if (self.isEmpty()):
            return print("Tem nada não cpx")
        else:
            print("Pilha abaixo ↧")
            while (auxNode != None):
                print(auxNode.datum)
                print("↧")
                auxNode = auxNode.next
    
   


LinkedStack = LinkedStack()
LinkedStack.push_clone(10)
LinkedStack.push_clone(9)
LinkedStack.push_clone(8)
LinkedStack.push_clone(7)
LinkedStack.push_clone(6)
LinkedStack.push_clone(5)
LinkedStack.update_head(666)
LinkedStack.pop_clone()
LinkedStack.print_head()
LinkedStack.print_all_stack()
LinkedStack.pop_clone()
LinkedStack.pop_clone()
LinkedStack.print_all_stack()