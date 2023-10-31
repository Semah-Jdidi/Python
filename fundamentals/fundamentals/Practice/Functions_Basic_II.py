

# Countdown
def countdown(number):
    new_list = []
    for i in range(number,-1,-1):
        new_list.append(i)
    return new_list


count = countdown(5)
print(count)


# Print and Return
list = [1,2]

def print_and_return(list):
    print(list[0])
    return list[1]


print(print_and_return(list))


# First Plus Length
my_list = [1,2,3,4,5]

def first_plus_length(my_list):
    sum = my_list[0] + len(my_list)
    return sum


print(first_plus_length(my_list))


# Values Greater than Second


#This Length, That Value
def this_length_that_value(size,value):
    list1 = []
    for x in range(size):
        list1.append(value)
    return list1

print(this_length_that_value(5,10))