names=["abc","def","ghi"]
print(names)
names[0]="xyz"
print(names)

#the property of changing values inside a string is called mutabiity.

print(len(names))
print(names[2])
print(names[-2:2])

#to add new values to a list
names=names+["hello",45]
print(names)

#append function is also used to add values to a list
names.append("chandhu")
print(names)

#to add values to a list from input
print("enter value to the list")
names.append(input())
print(names)