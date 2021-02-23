# Caio Beraldi Ribeiro 

from LinkedStack import LinkedStack
from ContiguityStack import ContiguityStack

class Comparison:
    def __init__(self):
        self.diferences = 0

    def compare_stacks(self):
        self.diferences = 0
        auxNode = LinkedStack.head  
        auxHead = ContiguityStack.head      
        while (auxNode != None):
            if (ContiguityStack.stack[auxHead] != auxNode.datum):
                self.diferences = self.diferences + 1
            auxNode = auxNode.next
            auxHead = auxHead - 1
        if (self.diferences != 0):
            print("Pilhas diferentes, há:", self.diferences,"diferença(s)")            
        else:
            print("Pilhas iguais")
    



LinkedStack = LinkedStack()
LinkedStack.push_clone(10)
LinkedStack.push_clone(9)
LinkedStack.push_clone(8)
LinkedStack.push_clone(7)
LinkedStack.push_clone(6)
LinkedStack.push_clone(5)
# LinkedStack.update_head(666)
# LinkedStack.pop_clone()
# LinkedStack.print_head()
# LinkedStack.print_all_stack()
# LinkedStack.pop_clone()
# LinkedStack.pop_clone()



ContiguityStack = ContiguityStack(10)
ContiguityStack.push_clone(10)
ContiguityStack.push_clone(9)
ContiguityStack.push_clone(8)
ContiguityStack.push_clone(7)
ContiguityStack.push_clone(6)
ContiguityStack.push_clone(5)
# ContiguityStack.print_head()
# ContiguityStack.update_head(666)
# ContiguityStack.print_head()
# ContiguityStack.pop_clone()
# ContiguityStack.print_head()
# ContiguityStack.destroy_stack()

Comparison = Comparison()
Comparison.compare_stacks()
LinkedStack.print_all_stack() 
ContiguityStack.print_all_stack()