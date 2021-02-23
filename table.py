# Caio Beraldi Ribeiro 

class Table:
    def __init__(self, maxSize, decision):
        self.maxSize = maxSize - 1
        self.key = [0] * (maxSize)
        self.value = [None] * (maxSize)
        self.size = -1
        self.auxI = 0
        self.decision = decision
       

    def __repr__(self):
        string =  ""
        if (not self.isEmpty()):
            for i in range(0, self.size + 1):
                string = string + str(self.key[i]) + ": " + str(self.value[i]) + "\n"
            return string + "\n"
        else:
            return string + "Lista destruida"

    def isEmpty(self):
        if (self.size == -1):
            return True
        else:
            False

    def isFull(self):
        if(self.size == self.maxSize):
            return True
        else:
            False

   
    def search(self, key, decision):
        if(decision == "bin"):
            return self.binarySearch(key)            
        elif(decision == "lin"):
            return self.linearSearch(key)
            

    def linearSearch(self, key):
        if(not self.isEmpty()):
            for i in range(0, self.size):
                if(self.key[i] == key):
                    self.auxI = i
                    return self.auxI
        return False        

   

    def binarySearch(self, key, begin = 0, end = None):
        
        if(not self.isEmpty() and (key >= 0 and key <= self.key[self.size])):     
            if(key == self.key[self.size]):
                self.auxI = self.size     
                print("key encontrada na posição:", self.size)
                return self.auxI               
            elif(key == self.key[0]):
                self.auxI = 0
                print("key encontrada na posição:", 0)
                return self.auxI
            else:
                if(end is None):
                    end = self.size                
                if(begin <= end):
                    half = (begin + end) //2
                    if (self.key[half] == key):
                        self.auxI = self.key[half]
                        print("achou:", self.auxI)
                        return self.auxI
                    if (key < self.key[half]):
                        return self.binarySearch(key, begin, half - 1)
                    else:
                        return self.binarySearch(key, half + 1, end)
                return None
            print("key invalida")
        else:                        
            return False

    def delete(self, key):
        if(self.search(key, self.decision)):
            for i in range(self.auxI, self.size):
                self.key[i] = self.key[i + 1]       
                self.value[i] = self.value[i + 1]
            self.size -= 1
    
    def destroy(self):
        self.size = -1


    def insert(self, key, value):
        if(self.search(key, self.decision)):
            self.value[self.auxI] = value
        elif(not self.isFull()):
            if(self.isEmpty()):
                self.size += 1
                self.value[self.size] = value
                self.key[self.size] = key
                print("Primeira key inserida, com chave:", self.key[self.size])
            else:
                if(self.size < self.maxSize):
                    self.size += 1
                self.value[self.size] = value
                self.key[self.size] = key               
                print("Outra key inserida, com chave:", self.key[self.size])

    
    def sortedInsert(self, key, value):
        if(self.search(key, self.decision)):
            self.value[self.auxI] = value
        elif(not self.isFull()):
            if(self.isEmpty()):
                self.size += 1
                self.value[self.size] = value
                self.key[self.size] = key
            else:
                if(self.size < self.maxSize):
                    self.size += 1                
                if(key > self.key[self.size - 1]):
                    self.value[self.size] = value
                    self.key[self.size] = key     
                else:                                       
                    auxSize = self.size - 1
                    while(key < self.key[auxSize]):
                        self.key[auxSize + 1] = self.key[auxSize]       
                        self.value[auxSize + 1] = self.value[auxSize]
                        auxSize -= 1    
                    self.value[auxSize + 1] = value
                    self.key[auxSize + 1] = key  

    



