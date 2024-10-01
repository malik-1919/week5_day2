#collection= single "variable" used to store multiple variables 
# lists= {} ordered and changable, Duplicates Ok
#set {} unorderd and imutable, but Add/Remove Ok,No duplicates
# Tuple=() ordered and unchangeable, duplicates Ok, FASTER

# fruits=["apple","orange","bannana","cocunit","kiwi","strawberry"]
# fruits={"apple","orange","banana","coconut"}
# print(help(fruits))
# print(dir(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

# fruits.add("pineapple") #adds element to list
# fruits.remove("apple") #removes element from list 
# fruits.pop() #pops off the element at the end
# fruits.clear() #clears 
# print(fruits)

# print(dir(fruits)) # prints out all the methods that come with the function 
# print(help(fruits)) # tells us what each method does 
# print(len(fruits)) # tells us how much is in each list
# print("apple" in fruits) 
# print("pineapple" in fruits) 
# fruits[0]="pineapple" # ressigns values
# fruits.append("pineapple") #add elements to the list 
# fruits.remove("apple") #removes elements 
# fruits.insert(0,"pinneapple") # inserts an item into a speicfic spot in the list 
# fruits.sort() # sorts the list
# fruits.reverse() # reverse the list
# fruits.clear() # clears the elements in the list 


#for fruit in fruits
#print(fruit)

# cars=["bmw","maserati","audi",",mercedes","ferrari"]
# print(f"these are a list of {cars[0]}")
# print(f"the first car is{cars[0]}")

# # changing the vaulue of the list

# cars[0]="toyota"
# print(f"the first car is {cars[0]}")

# print(f"the last car is{cars[-1]}")
# cars[-1]="lamborghini"
# print(f"the last car is{cars[-1]}")

# #adding a new value to the list
# cars.append("bugatti")
# print(cars)
# cars.remove("maserati")
# print(cars)

#looping through the list 
#otherwise called iteratiing through the list
#for car in cars:
#print(len(car))
#print(car)
    #carRequest=input("add a new car please:")
   # cars.append(carRequest)
    #print(cars)
   # print(len(cars))
    # print(cars,upper())
    #print(cars)
   # if len(cars)>10:
     #   break 


#print(help(fruits))
#print(dir(fruits))
#print(len(fruits))
#print("pineapple" in fruits)


#TUPLES 
#print(fruits.index("apple"))
#print(fruits.count("coconut"))
#print(fruits)
#for fruit in fruits:
#print(fruit)
#fruits={"apple","orange","banana","coconut"}





#DICTIONARY
#dictionary=a collection of {key:value} pairs
#               ordered and changable. No duplicates 
capitals={"USA":"Washington D.C.",
          "India": "New Delhi",
          "China":"Beijing",
          "Russia":"Moscow"}

#print(dir(capitals))
#print(help(capitals))
capitals.get("USA")
print(capitals.get("Japan"))
if capitals.get("Japan"):
    print("That capital exists")

else:
    print("That capital doesn't exist")  
capitals.update({"Germany": "Berlin"})
capitals.update({"USA":"Detroit"})
capitals.pop("China")
capitals.popitem()
capitals.clear

keys=capitals.keys()
for key in capitals.keys():
    print(key)

print(capitals)    


values=capitals.values()
for value in capitals.values():
  print(value)

  items=capitals.items()
  print(items)
  for key, value in capitals.items():
      print(f"{key}:{value}")






    #challange
    # create a list of friends
    # make sure the initial list is none
   # friends=[]
    #add a new friend  to the list,add at least 5 friends 
    # remove a friend 
    # insert a friend at a specific index maybe 2 
    #print the list of friends
    #loop through the list and print the friends name 
    # see if a particiular friend is in the list(boolean value)
    # if the list is greater than 10 break the loop

#friends=[]
#addFriend=input("add a friend please")
#friends.append(addFriend)
#print(friends)
#for friend in friends:
        #addFriend=input("add a friend please")
        #friends.append(addFriend)
        #print(friends)
        #if len(friends) >5:
                #break
        
#friends.remove("alex")
#print(friends)
