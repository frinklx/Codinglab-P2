todolist=["testing"]
shoppinglist = ["apple","orange","pear","other things", "je", "sd", "skd", "sdds"]
print(*todolist)
print(*shoppinglist)

print(shoppinglist[0])
print(shoppinglist[1])
print(shoppinglist[2])
print(shoppinglist[3])

shoppinglist[2] = "Chocolate"
print(*shoppinglist)

shoppinglist.append("20000000000")
print(*shoppinglist)

shoppinglist.insert(2,"helo")
print(*shoppinglist)

dictthis = {
    "model":"Honda Civic",
    "year":"2000",
    "color":"white"
    }

print("for : printing out shopping list below")
prev = ' '
for item in shoppinglist:
    print(prev + ', ' + item)
    prev = item
    
print("while: printing out shopping list")
i = 0
while i < len(shoppinglist):
    if (i < len(shoppinglist)/2) :        
        print(shoppinglist[i])
    i += 1

print("ykdm: printing thingy")
i = 0
while i < len(shoppinglist):    
    print(shoppinglist[i])
    i += 2
    

testing1 = input("[SYSTEM] What do you want to know? [Model, Year, Color].. ____: ")
print(dictthis[testing1])

