#collection= single "variable" used to store multiple variables 
# lists= {} ordered and changable, Duplicates Ok
#set {} unorderd and imutable, but Add/Remove Ok,No duplicates
# Tuple=() ordered and unchangeable, duplicates Ok, FASTER

# fruits=["apple","orange","bannana","cocunit","kiwi","strawberry"]
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

friends=[]
addFriend=input("add a friend please")
friends.append(addFriend)
print(friends)
for friend in friends:
        addFriend=input("add a friend please")
        friends.append(addFriend)
        print(friends)
        if len(friends) >5:
                break
        
friends.remove("alex")
print(friends)