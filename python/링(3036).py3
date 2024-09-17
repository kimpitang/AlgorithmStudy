from fractions import Fraction

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.head=None

    def push(self, data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def pop(self):
        if self.is_empty():
            return -1
        data=self.head.data
        self.head=self.head.next
        return data

    def is_empty(self):
        if self.head:
            return False
        return True

    def peek(self):
        if self.is_empty():
            return -1
        return self.head.data



if __name__=="__main__":

    ringnum = int(input())
    ringrr = str.split(input())

    ringr=Stack()

    for i in range(ringnum-1,-1,-1):
        ringr.push(ringrr[i])

    for j in range(0, ringnum):
        if j==0:
            fr=int(ringr.pop())
        elif j==ringnum-1:
            f=Fraction(fr,int(ringr.pop()))
            print(str(f.numerator)+"/"+str(f.denominator))
        else:
            f = Fraction(fr, int(ringr.pop()))
            print(str(f.numerator) + "/" + str(f.denominator))

