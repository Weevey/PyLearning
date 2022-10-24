import random
value = random.randint(0,5)
def newSub():
    print("Showing some text")
    print("printing",value,"times")
    for i in range(value):
        if i < value:
            print('Hello world')
    print("done")

start = input("Would you like some text? ")

if start == "yes":
    newSub()