mylist =list(("10" , "20" , "30" , "40" , "50"))
print(mylist[0])
print(mylist[-2])

print(mylist[1:4])
print(mylist[::-3])

tuple1 = ("A" , "B" , "C" , "D" , "E")
tuple2 = (1, 2, 3, 4, 5)
tuple3 = ("true", "true", "false")



print(tuple1)
print(tuple2)
print(tuple3)



pokhara = {
    "district" : "kaski",
    "country" : "Nepal",
    "university" : "pokhara university"
}


pokhara["university"] = "kathmandu university"
print(pokhara["university"])


#to print list into tuples
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print(my_tuple)