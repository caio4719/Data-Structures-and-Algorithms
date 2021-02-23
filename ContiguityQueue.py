# Caio Beraldi Ribeiro

from ContiguityStack import ContiguityStack

class Nodo:
    def __init__(self, datum):
        self.datum = datum
        self.next = next

    def __repr__(self):
        return str(self.datum) + "-->" + str(self.next)


class ContiguityQueue:
    def __init__(self, size):
        self.queueArray = [None] * size
        self.bottomLimit = 0
        self.upperLimit = size - 1
        self.beginQueue = self.bottomLimit - 1 
        self.endQueue = self.upperLimit + 1
        self.size = size

    def isEmpty(self):
        return self.beginQueue < self.bottomLimit or self.endQueue > self.upperLimit

    def isFull(self):
        return (self.beginQueue == self.bottomLimit and self.endQueue == self.upperLimit) or (self.beginQueue == self.endQueue + 1) 
        

    def insert(self, datum):
        if (self.isEmpty()):
            self.beginQueue = self.bottomLimit
            self.endQueue = self.bottomLimit
            self.queueArray[self.endQueue] = datum
        elif (not self.isFull()):
            if (self.endQueue == self.upperLimit):
                self.endQueue = self.bottomLimit
            else:
                self.endQueue += 1
            self.queueArray[self.endQueue] = datum
        else: 
            print("A fila está cheia")

    def delete(self):
        if (not self.isEmpty()):
            if (self.beginQueue > self.endQueue and self.beginQueue == self.upperLimit):
                self.beginQueue = self.bottomLimit
            elif (self.beginQueue == self.endQueue):
                self.destroyQueue()
            else:
                self.beginQueue += 1
        

    def destroyQueue(self):
        self.beginQueue = self.bottomLimit - 1 
        self.endQueue = self.upperLimit + 1

    def consult(self):
        if (not self.isEmpty()):
            return self.queueArray[self.beginQueue]
            
    def __repr__(self):
        string = "["
        if (not self.isEmpty()):
            if (self.beginQueue <= self.endQueue):
                for i in range (self.beginQueue, self.endQueue +1):
                    string = string + " --> " + str(self.queueArray[i])
            else:
                for i in range (self.bottomLimit, self.endQueue +1):
                    string = string + " --> " + str(self.queueArray[i])
        return string + "]"

    


    def orderContiguityQueue(self):
        stackSize = self.size + 1 
        auxStack01 = ContiguityStack(stackSize)
        auxStack02 = ContiguityStack(stackSize)
        forRange = self.size - 1
        counter = 0
               

        def queueToStack01():      
            auxStack01.push_clone(self.queueArray[self.beginQueue])
            ContiguityQueue.delete()      
                      
        
        def stack01ToStack02():
            auxStack02.push_clone(auxStack01.stack[auxStack01.head])
            auxStack01.pop_clone()
           

        def stack02ToStack01():
            auxStack01.push_clone(auxStack02.stack[auxStack02.head])
            auxStack02.pop_clone()

        def stack01ToQueue():            
            ContiguityQueue.insert(auxStack01.stack[auxStack01.head])
            auxStack01.pop_clone()

        
        queueToStack01()
        for i in range (0, forRange): 
            if (self.queueArray[self.beginQueue] < auxStack01.stack[auxStack01.head]):
                queueToStack01()
            elif(self.queueArray[self.beginQueue] > auxStack01.stack[auxStack01.head]):
                counter = 0
                while((self.queueArray[self.beginQueue] > auxStack01.stack[auxStack01.head]) and  (auxStack01.stack[auxStack01.head] != 0)):
                    stack01ToStack02()
                    counter = counter + 1
                queueToStack01()
                for i in range (0, counter):
                    stack02ToStack01()

        forRange = forRange + 1
        for i in range (0, forRange): 
            stack01ToQueue()


                

        print("--------- // ---------")

        print("Pilha 01")
        auxStack01.print_all_stack()
        print("Pilha 02")
        auxStack02.print_all_stack()

        print("--------- // ---------")
       
  
        

ContiguityQueue = ContiguityQueue(40)
ContiguityQueue.insert(15)
ContiguityQueue.insert(9)
ContiguityQueue.insert(18)
ContiguityQueue.insert(45)
ContiguityQueue.insert(6)
ContiguityQueue.insert(5)
ContiguityQueue.insert(48)
ContiguityQueue.insert(3)
ContiguityQueue.insert(156)
ContiguityQueue.insert(74)
ContiguityQueue.insert(415)
ContiguityQueue.insert(189)
ContiguityQueue.insert(84)
ContiguityQueue.insert(654)
ContiguityQueue.insert(612)
ContiguityQueue.insert(65)
ContiguityQueue.insert(26)
ContiguityQueue.insert(67)
ContiguityQueue.insert(217)
ContiguityQueue.insert(1)
ContiguityQueue.insert(15)
ContiguityQueue.insert(9)
ContiguityQueue.insert(18)
ContiguityQueue.insert(45)
ContiguityQueue.insert(6)
ContiguityQueue.insert(5)
ContiguityQueue.insert(48)
ContiguityQueue.insert(3)
ContiguityQueue.insert(156)
ContiguityQueue.insert(74)
ContiguityQueue.insert(415)
ContiguityQueue.insert(189)
ContiguityQueue.insert(84)
ContiguityQueue.insert(654)
ContiguityQueue.insert(612)
ContiguityQueue.insert(65)
ContiguityQueue.insert(26)
ContiguityQueue.insert(67)
ContiguityQueue.insert(217)
ContiguityQueue.insert(1)

print("--------- // ---------")
print("lista",ContiguityQueue)
print("--------- // ---------")
print("Ordenando abaixo")

ContiguityQueue.orderContiguityQueue()
print("lista",ContiguityQueue)
