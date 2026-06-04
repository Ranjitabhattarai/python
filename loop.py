#while loop
i=0
while i < 10:
    print(i)
    i += 1




#for loop
fruits = ["apple", "banana", "manago"]
for f in fruits:
    print(f)

#continue statement 
for i in range(10):
    if i == 5:
        continue
    print(i)

#choice statement 
x = -2
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")
