#assignment one

number_list = [1,2,3,4,5,6,7,8,9]

#list of even numbers only

def even_numbers(my_list):
    even_list = []
    for number in my_list:
        if(number % 2) == 0:
            even_list.append(number)
    return even_list

print even_numbers(number_list)


# list of odd numbers only

def odd_numbers(my_list):
    odd_list = []
    for numbers in my_list:
        if(numbers % 2)!= 0:
            odd_list.append(numbers)
    return odd_list

print odd_numbers(number_list)


#Total of only odd numbers

def sum_odd_numbers(my_list):
    return sum(odd_numbers(my_list))

print sum_odd_numbers(number_list)

#highest/biggest in my even list

def max_of_even_numbers(my_list):
    return max(even_numbers(my_list))

print max_of_even_numbers(number_list)

#highest/biggest of odd numbers

def max_of_odd_numbers(my_list):
    return max(odd_numbers(my_list))

print max_of_odd_numbers(number_list)

