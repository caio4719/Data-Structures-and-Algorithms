# Caio Beraldi Ribeiro 

#  Cria
#  Insere (valor, posição)
#  Remove (posição)
#  Posição (valor)
#  Valor (posição)
#  Destroi

# todas funcções estão nesse arquivo

class Node: 
    def __init__(self, datum):
        self.datum = datum # dado
        self.next = None # aponta para o proximo Nodo amazenado no Head

class LinkedList:
    def __init__(self): 
        self.head = None # posição fixa, o pointer que percorre a lista
        self.size = 0

    
    def appendClone(self, element):
        if (self.head == None): # primeira inserção           
            self.head = Node(element) 
            print("Inserção na posição: ",self.size,", valor:", element)
        else: # outras inserções
            pointer = self.head
            while (pointer.next):
                pointer = pointer.next
            pointer.next = Node(element)
            self.size = self.size + 1 
            print("Inserção na posição: ",self.size,", valor:", element)


    
    def insert(self, element, location): # inseri na posição escolhida
        if ((location > self.size) or (location < 0)):
            print("Posição inválida meu cupinxa!")
        else:
            pointer = self.head
            for i in range(location):            
                pointer = pointer.next
            print("\nElemento achado: ", pointer.datum, "Na posição:", location, " aqui será inserido outro nodo")            
            pointer.datum = element
            
    
    def clonePop(self):
        pointer = self.head
        for i in range(self.size):
            pointer = pointer.next
        pointer.datum = None
        self.size = self.size - 1
                

    
    def printList(self): # print a lista 
        if (self.head == None):
            print("Lista destruida ou inexistente")
        else:
            pointer = self.head
            for i in range(self.size):
                print( pointer.datum, end = ",",)
                pointer = pointer.next
            print("\n")
           
    
    def printElement(self, element): # procura elemento escolhido
        pointer = self.head
        for i in range(self.size):
            if (pointer.datum == element):
                print("\n Elemento achado: ", pointer.datum, "Na posição:", i)
            pointer = pointer.next
    
    
    def printLocation(self, location): # procura posição
        if (location > self.size - 1):
            print("Posição inválida meu cupinxa!")
        else:
            pointer = self.head
            for i in range(location):            
                pointer = pointer.next
            print("\nElemento achado: ", pointer.datum, "Na posição:", location)
        

    
    def destroyList(self):
        self.head = None
        self.size = None


    #    um método que retorne o número de elementos;
    #    um método que receba uma segunda listas encadeada como argumento e retorne um valor lógico indicando se as listas são iguais;
    #    um método que imprima os valores de uma lista encadeada de trás para frente.

    
    def listLenght(self):
        print("\nA lista tem:", self.size + 1, "elementos")
      
    
    def compareLists(self):
        toBeCompared = [3,4,666,777] # lista para ser comparada
        diferences = 0
        if (self.head == None):
            print("Lista destruida ou inexistente")
        else:
            pointer = self.head            
            for i in range(self.size):
                if (pointer.datum != toBeCompared[i]):
                    diferences = diferences + 1                   
                pointer = pointer.next
            if(diferences == 0):
                print("Listas iguais com", self.size, "elementos")
            else: 
                print("Listas diferentes")
    
        
                
    
    def printListBack(self):          
        auxSize = self.size   
        for i in range(auxSize):
            pointer = self.head   
            auxSize = auxSize - 1
            for i in range(auxSize):
                pointer = pointer.next
            print( pointer.datum, end = ",",)
        


listaTeste = LinkedList()
listaTeste.appendClone(1)
listaTeste.appendClone(2)
listaTeste.appendClone(3)
listaTeste.appendClone(4)
listaTeste.appendClone(5)
listaTeste.appendClone(6)
listaTeste.appendClone(7)
listaTeste.appendClone(8)
listaTeste.appendClone(9)
listaTeste.appendClone(10)
listaTeste.appendClone(11)
listaTeste.appendClone(12)
listaTeste.printList()
listaTeste.insert(5, 2)
listaTeste.printListBack()
listaTeste.listLenght()

# listaTeste.compareLists()
# listaTeste.printListBack()
# listaTeste.destroyList()

listaTeste.printElement(11)
listaTeste.printElement(1)
listaTeste.printElement(5)

listaTeste.printLocation(0)
listaTeste.printLocation(1)
listaTeste.printLocation(2)
listaTeste.printLocation(3)
listaTeste.printLocation(10)
listaTeste.printLocation(666)

# listaTeste.clonePop()
# listaTeste.clonePop()
# listaTeste.clonePop()
# listaTeste.printList()
