my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#           0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#         -10,-9,-8,-7,-6,-5,-4,-3,-2,-1


# Lists =======================================================================
print()
print('SLICING LISTS', '-' * 100)
print()
print('Accessing indices')
print(my_list)
# Access specific element starting from beginning
print(my_list[0])
# Access specific element starting from end
print(my_list[-1])
# Slice a section of the list
# list[start:end:step]
# END ARG (INDEX) ARE NOT INCLUSIVE!!!!!!!!!!!!!!!!!!!
print()
print('Slice a section of the list')
print(my_list[0:5])  # |        (0) - (5)
print(my_list[3:7])  # |        (3) - (7)
print(my_list[3:-3])  # |       (3) - (3 from end of list)
print(my_list[-7:-3])  # |      (7 from end of list) - (3 from end of list)
print(my_list[:-3])  # |        (0) - (3 from end of list)
print(my_list[3:])  # |         (3) - (end of list)
# Using the step arg
print()
print('Using the step arg')
print(my_list[2:9:2])  # |      (2) - (9) but only every second index
print(my_list[3:10:3])  # |     (3) - (10) but only every third index
# Slice and return in reverse order
print()
print('Slice and return in reverse order')
print(my_list[10:2:-1])  # |    (10) - (2)
print(my_list[10:2:-3])  # |    (10) - (2) but only every third index
print(my_list[::-1])  # |       reverse entire list

# Slicing Strings =============================================================
print()
print('SLICING STRINGS', '-' * 100)
print()
sample_url = 'http://derp.com'
print(sample_url)
print(sample_url[::-1])  # |    Reverse the url
print(sample_url[-4:])  # |     Select '.com'
print(sample_url[7:])  # |      Select url without 'http://'
print(sample_url[7:-4])  # |    Select url without 'http://' or '.com'
