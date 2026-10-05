class DynamicArray:
    # da_list
    # capacity
    
    def __init__(self, capacity: int):
        self.da_list = []
        self.capacity=capacity

    def get(self, i: int) -> int:
        return self.da_list[i]

    def set(self, i: int, n: int) -> None:
        self.da_list[i]=n
        return

    def pushback(self, n: int) -> None:
        if len(self.da_list)==self.capacity:
            self.resize()
        self.da_list.append(n)
        return


    def popback(self) -> int:
        pop = self.da_list[-1]
        self.da_list=self.da_list[:-1]
        return pop
 

    def resize(self) -> None:
        self.capacity=self.capacity*2


    def getSize(self) -> int:
        return len(self.da_list)
        
    
    def getCapacity(self) -> int:
        return self.capacity
