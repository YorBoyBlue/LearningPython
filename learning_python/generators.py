# NOT Generator
def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i * i)
    return result


def square_numbers_gen(nums):
    for i in nums:
        yield (i * i)


# result will be [1, 4, 9, 16, 25]
my_nums = square_numbers([1, 2, 3, 4, 5])
print(my_nums)

print()

# result will be <generator object square_numbers_gen at 0x000002510A042780>
my_nums = square_numbers_gen([1, 2, 3, 4, 5])
print(my_nums)
# You can convert the generator to a list but you will lose the advantages you
# gain regarding performance (Generators don't store values in memory)
print(list(my_nums))

print()

# You can call next() on the generator to select the next value
# If you call it too many times you will get an error
my_nums = square_numbers_gen([1, 2, 3, 4, 5])
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))

# This is the best and safest way to access all values from a generator
my_nums = square_numbers_gen([1, 2, 3, 4, 5])
for num in my_nums:
    print(num)

print()

# The above example done with a list comprehension
my_nums = [x * x for x in [1, 2, 3, 4, 5]]
print(my_nums)


def find_even_index(arr):
    index = 0
    for i in arr:
        left_sum = 0
        right_sum = 0
        left = []
        right = []

        # I want an array with all values to the left and right of the current index
        if index != 0:
            left = arr[:i + 1]
            right = arr[i:]

        # Sum up the values to the left and right of the current index
        for value in left:
            left_sum += value

        for value in right:
            right_sum += value

        if left_sum == right_sum:
            return i

        index += 1

    return -1


my_arr = [20, 10, 30, 10, 10, 15, 35]

print(find_even_index(my_arr))
