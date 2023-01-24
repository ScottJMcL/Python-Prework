################################################################################
# Five questions to show understanding of Python pre-work Ch 1 - 8
################################################################################

# Question 1:
# Write a function to print "hello_USERNAME!" USERNAME is the input of the 
# function. The first line of the code has been defined as below.

def hello_name(user_name):
    """ Takes USERNAME and prints a personalized greeting. """

    print("\nHello_" + user_name.upper() + "!\n")

print("\nQuestion 1 output:")
hello_name("Jim_Bob")
print("")

################################################################################

# Question 2:
# Write a python function, first_odds that prints the odd numbers from 1-100 
# and returns nothing

def first_odds():
    """
    Prints all odd numbers from 1 - 100.  No return values.
    """

    i = 1
    while i <= 100:
        if i % 2 == 0:
            i+=1
        elif i % 2 != 0:
            print(i)
            i+=1
        else:
            print("Error")
            break

print("\nQuestion 2 output:")

first_odds()

print("")

################################################################################

# Question 3:
# Please write a Python function, max_num_in_list to return the max number of 
# a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    """
    Returns the max of a given list.
    """    
    current_list = a_list[:]

    """
    Returns the max from a given list.
    """
    current_list.sort()
    return current_list[-1]

print("\nQuestion 3 output:")

print(max_num_in_list([189,2,3,4]))

print("")

################################################################################

# Question 4:
# Write a function to return if the given year is a leap year. A leap year is 
# divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).

# Wikipedia: https://en.wikipedia.org/wiki/Leap_year
# Every year that is exactly divisible by four is a leap year, except for years 
# that are exactly divisible by 100, but these centurial years are leap years 
# if they are exactly divisible by 400. For example, the years 1700, 1800, and 
# 1900 are not leap years, but the years 1600 and 2000 are.

def is_leap_year(a_year):
    """
    Determines if a given year is a leap year.  Returns True or False.
    """

    if a_year % 4 == 0:
        if a_year % 100 != 0:
            return True
        elif a_year % 100 == 0:
            if a_year % 400 == 0:
                return True
            elif a_year % 400 != 0:
                return False
            else:
                print("Error_1")
        else:
            print("Error_2")
    elif a_year % 4 != 0:
        return False
    else:
        print("Error_3")

print("")
print("\nQuestion 4 output:")

years = [1974, 1975, 1976, 1977, 1978, 1979, 1980, 2000, 1600, 1960, 1964, 
        1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 
        2016, 2020
        ]

for year in years:

    print(str(year), end=" ")

    if is_leap_year(year):
        print("was a leap year.")
    elif is_leap_year(year) == False:
        print("was NOT a leap year.")
    else:
        print("This should never print")

print("")


################################################################################



# Question 5
# Write a function to check to see if all numbers in list are consecutive 
# numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] 
# are not consecutive numbers. The return should be boolean Type.

 

def is_consecutive(a_list):
    """
    Determines if numbers in a given list are consecutive. Returns True or False
    """

    # Assumes question requires list to be in order as well as consecutive.

    # If a list with out-of-order, but consecutive numbers is accepatable:
        # working_list = sorted(a_list[:])
        # use working_list in place of a_list below
    
    i = 1
    while i < len(a_list):
        if a_list[i] == a_list[i-1] + 1: 
            i += 1
            continue # current number consecutive with previous, keep going
        elif a_list[i] != a_list[i-1] + 1:
            return False # current number consecutive with previous, stop
            break
    return True     # Finished list, all numbers are consecutive


print("\nQuestion 5 output:")

my_list = [1,2,3,4,5,6,7,8,9,10]
your_list = [6,7,8,9,10,12,11,14]
print(is_consecutive(my_list))
print(is_consecutive(your_list))
