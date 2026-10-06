class Node:
    def __init__(self, val=None, next=None):
        self.next = None
        self.val=val
        self.next=next
    

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.length = 0
    
    def get(self, index: int) -> int:
        if index<0 or index>= self.length:
            return -1
        curr = self.head
        for i in range(index):
            if curr.next:
                curr = curr.next
        return curr.val
        

    def insertHead(self, val: int) -> None:
        self.head = Node(val,next=self.head)
        self.length+=1
        

    def insertTail(self, val: int) -> None:
        if self.head is None:
            self.insertHead(val)
            self.length+=1
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next = Node(val)
        self.length+=1

        

    def remove(self, index: int) -> bool:
        # remove and stitch.
        # so remove at 1...
        if index>=self.length or index<0:
            return False
        elif index==0:
            self.head=self.head.next
            self.length-=1
            return True
        else:
            curr = self.head
            for i in range(index-1):
                curr=curr.next
            curr.next=curr.next.next
            self.length-=1
            return True
        

    def getValues(self) -> List[int]:
        res = []
        curr = self.head
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
