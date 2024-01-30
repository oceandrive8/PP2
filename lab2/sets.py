#Exercise 1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")
#checking if apple in set
  
  
#Exercise 2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
#adding new element

#Exercise 3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
#adding all elements from more_fruits into fruits

#Exercise 4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
#removing banana :/

#Exercise 5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
#discarding(removing again) banana...