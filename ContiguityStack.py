# Caio Beraldi Ribeiro 

from stacks import ContiguityNode

class ContiguityStack:
    def __init__(self, size):
        self.stack = [0] * size
        self.head = 0 # topo da Pilha
        self.size = size # tamanho do vetor alocado para pilha
        
    
    def push_clone(self, datum):
        if (self.head < self.size):
            self.head = self.head + 1
            self.stack[self.head] = datum
        print("Dado adicionado:" , self.stack[self.head], "head:", self.head)

    def pop_clone(self):
        if (self.head <= self.size):
            print("Dado removido:" , self.stack[self.head])
            self.head = self.head - 1

    def destroy_stack(self):
        self.head = - 1

    def print_head(self):
        if(self.head == -1):
            print("Pilha excluida :(")
        else:
            print("-------- * * --------","\nDado topo da pilha:" ,self.stack[self.head], "\n Valor head:", self.head, "\n-------- * * --------",)

    def print_all_stack(self):       
        if(self.head == -1):
            print("Pilha excluida :(")
        else:
            auxHead = self.head  
            while (auxHead != 0):
                print(self.stack[auxHead])
                print("↧")
                auxHead = auxHead - 1

    def update_head(self, datum):
        if(self.head == -1):
            print("Pilha excluida :(")
        else:
            self.stack[self.head] = datum
               
                
                


# ContiguityStack = ContiguityStack(10)
# ContiguityStack.push_clone(10)
# ContiguityStack.push_clone(9)
# ContiguityStack.push_clone(8)
# ContiguityStack.push_clone(7)
# ContiguityStack.push_clone(6)
# ContiguityStack.push_clone(5)
# ContiguityStack.update_head(666)
# ContiguityStack.print_all_stack()
# ContiguityStack.pop_clone()
# ContiguityStack.print_head()
# ContiguityStack.destroy_stack()
# ContiguityStack.print_head()