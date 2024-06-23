"""
#
#Part : Python While loop
#
"""

i = 1
while i < 5:
    print (" i =", i)
    i += 1

i = 1 
while i < 5:
    print("i = ",i)
    if i == 3:
        break
    i+=1

i = 1
while i < 5:
        print("i = ",i)
        if i == 3:
            continue
        i+=1

#i = 1
# while i < 5:
#   print("i = ", i)
#   if i ==3:
#       continue
#   i=+1

i = 1
while i < 5:
     print ("i = ", i)
     i+=1
else:
    print("Game over")


"""
#
#Part : Python For loop
#
"""
fruits = ["Apple","Banana","Coconut"]
for x in fruits:
     print("fruit:",x)
     
for fruit in fruits:
     print("Fruit:", fruit)
     if fruit == "banana":
          break
     print("fruit:",fruit)

     if fruit == "banana":
          continue
     print("fruit:",fruit)

for x in range(len(fruits+1)):
     print("Number = ",x)
else:
     print("Game Over")

adjs = ["Red","Yellow","Coconut"]
fruit = ["Apple","Banana","Coconut"]
for adj in adjs:
     for fruit in fruits:
          print(adj, fruit)
          



     