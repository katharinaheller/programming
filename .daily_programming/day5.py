# day 5
# two methods of reversing a list in python

# method one - using reverse()
my_list = [1,2,3,4,5,66]
my_list.reverse()
print(my_list)
# this is what the output looks like: [66, 5, 4, 3, 2, 1]

# method two - using slicing
list = [5,6,7,8,9,10]
list = list[::-1] # creates a reversed copy of the list using slicing
print(list)
# this is what the output looks like: [10, 9, 8, 7, 6, 5]
