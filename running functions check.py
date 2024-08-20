import sortablelist as sl
my_list = sl.SortableList([3,5,7,9,10,14,27,48,4,5,4])

print("the max is", my_list.__max__())
#print("the number you're looking for is at index", my_list.binary_search(5))
my_list.bogo_sort()
print(my_list)
