#for loop
for x in range(1,10):
  print(x)

items = ["item1", 'item2', 'item3']

for item in items:
    print(item)

for x in range(len(items)):
    print("x is" + str(x))
    print("item is " + items[x])

#loop 10times

def countNumber():
    print ("count")

for x in range(1,10):
    countNumber()

#
# 

def countNumber(theNumber):
    print ("count:" + str(theNumber))

for value in range(1,10):
    countNumber(value)
#the other writing
#numberOfTimes = 10
# for value in range(1,numberOfTimes):
    countNumber(value)    

items = ["item1", 'item2', 'item3']
print("item in items")

# 3 similiar for typying ways
for x in items:
    print(x)

for x in range(0,3):
    print(items[x])

for x in range(len(items)):
    print(items[x])    

#while loop 1
x=0
while x<10:
    x +=1
    print(x)

#while loop 2
global x
x = 0

def increaseCount():
    global x
    x += 1

while x<10:
    increaseCount()
    print(x)