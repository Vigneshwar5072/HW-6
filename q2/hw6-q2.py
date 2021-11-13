class Queue:
    inner_list = []
    counter = 0
    
    def enqueue(self, value):
        #element=input("Enter the element:")
        inner_list.append(value)
        print(value,"is added to the Queue!")

    def dequeue(self):
        if not inner_list:# or if len(stack)==0
            print("Queue is Empty!!!")
        else:
            e=inner_list.pop(0)
            print("element removed!!:",e)
        
    def delete(self):
        value = int(input("enter the element to be removed from the Queue:"))
        if not inner_list:# or if len(stack)==0
            print("Queue is Empty!!!")
        else:
            #print("I am here")
            for i in range(len(inner_list)):
                if(inner_list[i] == value):
                    e= inner_list.pop(i)
                    print("element removed!!:", e)
                    print(inner_list)
                    break
                    
            #e=inner_list.pop(0)
            #print("element removed!!:",e)
        
inner_list = []        
obj = Queue()
obj.enqueue(5)
obj.enqueue(7)
obj.enqueue(13)
obj.enqueue(4)
obj.enqueue(7)
print(inner_list)
obj.delete()
print(obj.dequeue()) # Should return 5
