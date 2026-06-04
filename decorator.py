#for single decorator
def fruits(function):
    def myinner():
        return function().upper()
    return myinner

@fruits
def myfunction():
    return "mango"

print(myfunction())

#for multiple decorator 
def infromation(function):
    def myinner():
        return function().upper()
    return myinner

@infromation
def myfunction():
    return "Ranjita"

@infromation
def otherfunction():
    return "Have a great day"

print(myfunction())
print(otherfunction())

#add data 
def fruits(function):
    def myinner(name):
       return function(name).upper()
    return myinner 

@fruits
def myfunction(name):
    return name
print(myfunction("Banana"))