class Node:
   def __init__(self, data):
      self.left = None
      self.mid = None
      self.right = None
      self.data = data

   def insert(self, data):
# Compare the new value with the parent node
      if self.data:
        if data < self.data:
            if self.left is None:
               self.left = Node(data)
               print("inserted the left small element: small element")
            else:
               self.left.insert(data)
        elif (data-self.data > 10):
            if self.right is None:
                self.right = Node(data)
                print("inserted the right element: too big element")
            else:
                self.right.insert(data)
        elif(data-self.data<10):
            if self.mid is None:
                self.mid = Node(data)
                print("inserted the mid element: big element")
            else:
                self.mid.insert(data)
      else:
        self.data = data

# Print the tree
   def traversal_print(self):

      if self.left:
         self.left.traversal_print()
      print(self.data)
      if self.mid:
          self.mid.traversal_print()
      if self.right:
         self.right.traversal_print()

   def deleteDeepest(root,d_node):
       q = []
       q.append(root)
       while(len(q)):
           temp = q.pop(0)
           if temp is d_node:
               temp = None
               return
           if temp.right:
               if temp.right is d_node:
                   temp.right = None
                   return
               else:
                   q.append(temp.right)
           if temp.left:
               if temp.left is d_node:
                   temp.left = None
                   return
               else:
                   q.append(temp.left)
           if temp.mid:
               if temp.mid is d_node:
                   temp.mid = None
                   return
               else:
                   q.append(temp.mid)

  
# function to delete element in binary tree
   def deletion(root, key):
       if root == None :
           return None 
       if root.left == None and root.right == None and root.mid == None:
           if root.key == key :
               return None
           else :
               return root
        
       key_node = None
       q = []
       q.append(root)
       temp = None
       while(len(q)):
           temp = q.pop(0)
           if temp.data == key:
               key_node = temp
           if temp.left:
               q.append(temp.left)
           if temp.right:
               q.append(temp.right)
           if temp.mid:
               q.append(temp.mid)
       if key_node :
           x = temp.data
           deleteDeepest(root,temp)
           key_node.data = x
       return root


root = Node(20)
root.insert(40)
root.insert(45)
root.insert(32)

root.traversal_print()
root.deletion(45)
root.traversal_print()
