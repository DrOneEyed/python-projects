from math import ceil, floor
from tarfile import TarInfo


class MyCircularQueue():

    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    def enqueue(self, data):

        if ((self.tail + 1) % self.k == self.head):
            print("The circular queue is full\n")

        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data

    def dequeue(self):
        if (self.head == -1):
            print("The circular queue is empty\n")

        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp

    def printCQueue(self):
        if(self.head == -1):
            print("No element in the circular queue")

        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()

    def checkRich(self):
        if(self.head == -1):
            print("No elements in the circular queue")
        elif(self.tail >= self.head):
            for i in range(self.head, self.tail+1):
                if(i%2 == 0):
                    if(i == 0):
                        if(self.queue[self.tail] > self.queue[0] and self.queue[1] > self.queue[0]):
                            mon1 = floor(self.queue[self.tail]*10/100)
                            mon2 = floor(self.queue[1]*10/100)
                            self.queue[self.tail] -= mon1
                            self.queue[1] -= mon2
                            self.queue[0] = (self.queue[0] + mon1 + mon2)
                        elif(self.queue[0] < self.queue[self.tail]):
                            mon =  floor(self.queue[self.tail]*15/100)
                            self.queue[self.tail] = (self.queue[self.tail] - mon)
                            self.queue[0] = self.queue[0] + mon
                        elif(self.queue[0] < self.queue[1]):
                            mon = floor(self.queue[1]*15/100)
                            self.queue[1] -= mon
                            self.queue[0] = (self.queue[0] + mon)
                    elif(i == self.tail):
                        if(self.queue[self.tail] < self.queue[0] and self.queue[self.tail] < self.queue[i-1]):
                            mon1 = floor(self.queue[0]*10/100)
                            mon2 = floor(self.queue[i-1]*10/100)
                            self.queue[0] -= mon1
                            self.queue[i-1] -= mon2
                            self.queue[self.tail] = (self.queue[self.tail] + mon1 + mon2)
                        elif(self.queue[self.tail] < self.queue[i-1]):
                            mon =  floor(self.queue[i-1]*15/100)
                            self.queue[i-1] = floor(self.queue[i-1] - mon)
                            self.queue[self.tail] = (self.queue[self.tail] + mon)
                        elif(self.queue[self.tail] < self.queue[0]):
                            mon = floor(self.queue[0]*15/100)
                            self.queue[0] -= mon
                            self.queue[self.tail] = (self.queue[self.tail] + mon)
                    else:
                        if(self.queue[i-1] > self.queue[i] and self.queue[i+1] > self.queue[i]):
                            mon1 = floor(self.queue[i-1]*10/100)
                            mon2 = floor(self.queue[i+1]*10/100)
                            self.queue[i-1] -= mon1
                            self.queue[i+1] -= mon2
                            self.queue[i] = (self.queue[i] + mon1 + mon2)
                        elif(self.queue[i] < self.queue[i-1]):
                            mon =  floor(self.queue[i-1]*15/100)
                            self.queue[i-1] = floor(self.queue[i-1] - mon)
                            self.queue[i] = floor(self.queue[i] + mon)
                        elif(self.queue[i] < self.queue[i+1]):
                            mon = floor(self.queue[i+1]*15/100)
                            self.queue[i+1] -= mon
                            self.queue[i] = (self.queue[i] + mon)
                else:
                    if(i == 0):
                        if(self.queue[self.tail] > self.queue[0] and self.queue[1] > self.queue[0]):
                            mon1 = ceil(self.queue[self.tail]*10/100)
                            mon2 = ceil(self.queue[1]*10/100)
                            self.queue[self.tail] -= mon1
                            self.queue[1] -= mon2
                            self.queue[0] = (self.queue[0] + mon1 + mon2)
                        elif(self.queue[0] < self.queue[self.tail]):
                            mon =  ceil(self.queue[self.tail]*15/100)
                            self.queue[self.tail] = (self.queue[self.tail] - mon)
                            self.queue[0] = self.queue[0] + mon
                        elif(self.queue[0] < self.queue[1]):
                            mon = ceil(self.queue[1]*15/100)
                            self.queue[1] -= mon
                            self.queue[0] = (self.queue[0] + mon)
                    elif(i == self.tail):
                        if(self.queue[self.tail] < self.queue[0] and self.queue[self.tail] < self.queue[i-1]):
                            mon1 = ceil(self.queue[0]*10/100)
                            mon2 = ceil(self.queue[i-1]*10/100)
                            self.queue[0] -= mon1
                            self.queue[i-1] -= mon2
                            self.queue[self.tail] = (self.queue[self.tail] + mon1 + mon2)
                        elif(self.queue[self.tail] < self.queue[i-1]):
                            mon =  ceil(self.queue[i-1]*15/100)
                            self.queue[i-1] = (self.queue[i-1] - mon)
                            self.queue[self.tail] = (self.queue[self.tail] + mon)
                        elif(self.queue[self.tail] < self.queue[0]):
                            mon = ceil(self.queue[0]*15/100)
                            self.queue[0] -= mon
                            self.queue[self.tail] = (self.queue[self.tail] + mon)
                    else:
                        if(self.queue[i-1] > self.queue[i] and self.queue[i+1] > self.queue[i]):
                            mon1 = ceil(self.queue[i-1]*10/100)
                            mon2 = ceil(self.queue[i+1]*10/100)
                            self.queue[i-1] -= mon1
                            self.queue[i+1] -= mon2
                            self.queue[i] = (self.queue[i] + mon1 + mon2)
                        elif(self.queue[i] < self.queue[i-1]):
                            mon =  ceil(self.queue[i-1]*15/100)
                            self.queue[i-1] = (self.queue[i-1] - mon)
                            self.queue[i] = (self.queue[i] + mon)
                        elif(self.queue[i] < self.queue[i+1]):
                            mon = ceil(self.queue[i+1]*15/100)
                            self.queue[i+1] -= mon
                            self.queue[i] = (self.queue[i] + mon)


obj = MyCircularQueue(10)
for i in range(10):
    obj.enqueue(int(input()))

print("Initial Queue")
obj.printCQueue()

n = int(input())
for i in range(n):
    obj.checkRich()
    print("After")
    obj.printCQueue()
