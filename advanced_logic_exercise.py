# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)

# 2. Print the difference between the largest and smallest value:
sorted_numbers = sorted(numbers)
print(sorted_numbers[0])
print(sorted_numbers[-1])
# 3. Print True if the list contains a 2 next to a 2 somewhere.

# LC: @John: I am working on avoiding the temptation to just print out True
for number in numbers:
    if number == 2:
        occurance_index = numbers.index(number)
        if numbers[occurance_index + 1] == 2:
            print("True")
            break


# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

#  so expected result inserts 1, pauses until after it has hit 7 and then adds again
#  I need to split the list on the first 6 into a and b, then split b into c and d on the first  7
#  then I need to join a and d and add all the numbers in that list up
#  expected result is 1 + 1 + 6 + 13 + 99 + 7 = 127

print(numbers)
first_split = numbers.index(6)
print("first split at index " + str(first_split))
second_split = numbers.index(7)
print("second split at index " + str(second_split))
numbers_to_keep = numbers[:1]
print(numbers_to_keep)
more_numbers_to_keep = numbers[(second_split + 1)::1]
print(more_numbers_to_keep)
numbers_to_add_up = numbers_to_keep + more_numbers_to_keep
print(numbers_to_add_up)
sum_of_numbers = 0
for number in numbers_to_add_up:
    sum_of_numbers += number
print(sum_of_numbers)
print("__________________")


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

print(numbers)
sum_of_numbers = 0
counter = 0
stop_check = len(numbers) - 1
print(stop_check)
while counter <= stop_check:
    if numbers[counter] == 13:
        # print("oh a 13")
        counter += 2
    else:
        sum_of_numbers += numbers[counter]
        counter += 1

print(sum_of_numbers)





