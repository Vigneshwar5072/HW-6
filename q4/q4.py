my_dict = {"firstName":"Mohamed", "lastName":"Farag", "birthYear":"1990", "Nationality":"Egyptian"}
print(my_dict)
n = int(input("Please enter the number of keys to be removed: \n"))
myRemovalList = []
for i in range(0, n):
    ele = str(input("Enter the key element:"))
    myRemovalList.append(ele)
def removingKeys(my_dict, myRemovalList):
    [my_dict.pop(key) for key in myRemovalList]
    return(my_dict)
print("The keys to be removed are :", myRemovalList)
my_dict = removingKeys(my_dict,myRemovalList)
print("The final my_dict is :", my_dict)
