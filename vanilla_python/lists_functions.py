#using list values
lucky_numbers = [45,4,8,15,16,22]
friends = ["John","Paul","Mick","Dylan","Jim","Sara"]
print(friends)
#append  item to the end of a list
friends.append('Rock')
print(friends)
#insert a value into the middle of a list basedd on the index
friends.insert(1,"Pope") 
print(friends)
#remove a value based on an element
friends.remove('Pope')
print(friends)
#find the index of a value
print(friends.index("Mick"))
print(friends.index("Sara"))

#remove all elements for the list
# friends.clear()
# print(friends)

# friends = ["John","Paul","Mick","Dylan","Jim","Sara","Sara"]
# #getst the count of same elements
# print(friends.count("Sara"))

#sorts lists
lucky_numbers.sort()
friends.sort()

print(friends)

#add list to another list 
# friends.extend(lucky_numbers)
# print(friends)
