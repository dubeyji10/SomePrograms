#
# """
# Exercise:
# Write a function 'def areatriangle(b,h)' to compute the area
# of a triangle: formula is area = .5*b*h.
# Output should look like:
# The area of a triangle of base 3 and height 5 is 7.5
#
# You can test your function by executing the following code:
# """
# #%%
# # The following will test areatriangle()
# #%%
# """
# Solution:
# """
# #%%
# def areatriangle(b,h):
#     area = .5*b*h
#     print("The area of a triangle of base {} and height {} is {}".format(b,h,area))
#
# areatriangle(3,5)
# areatriangle(2,20)
#
# #--------------------------------------------------------------------------
#
#
# #
# # Exercise:
# # Write a function 'def celsius_to_fahrenheit(temp)' to convert Celsius
# # to Fahrentheit temperature. The formula is (9/5) times temp plus 32.
# # Print the output in the form:
# # The Celsius temperature 50.0 is equivalent to 122.0 degrees Fahrenheit.
# # """
# #%%
# # The following will test the above function
#
# #%%
# """
# Solution:
# """
# #%%
# def celsius_to_fahrenheit(temp):
#     f=(temp*9/5)+32
#     print("The Celsius temperature ",temp ," is equivalent to ",f," degrees Fahrenheit.")
#
#
# celsius_to_fahrenheit(100)
# celsius_to_fahrenheit(0)
# celsius_to_fahrenheit(50.)
#
#
# #------------------------------------------------------------------------
#
#
#
# # def name():
# #     """ Input first and last name, combine to one string and print """
# #     fname = input("Enter your first name: ")
# #     lname = input("Enter your last name: ")
# #     fullname = fname + " " + lname
# #
# #     print("Your name is:", fullname)
# #
#
# """
# Exercise:
# Extend the name function written in class to include the city and state.
# That is, ask two more questions to get the city and the state you live in.
# Print where you are from on a new line. Put the customary comma between
# city and state. to save time, here is the starting function.
# Your run should look like the following (even if this is not the customary
# way in your country):
# Enter your first name: Bill
#
# Enter your last name: Boyd
#
# Enter the city you live in: Middletown
#
# Enter the state you live in: CT
# Your name is: Bill Boyd
# You live in:  Middletown, CT
#
#
# """
# #solution :
#
#
#
# # def name():
# #     """ Input first and last name, combine to one string and print """
# #     fname = input("Enter your first name: ")
# #     lname = input("Enter your last name: ")
# #     fullname = fname + " " + lname
# #     city = input("Enter the city you live in: ")
# #     state = input("Enter the state you live in: ")
# #     place = city+", "+state
# #     print("Your name is:", fullname)
# #     print("You live in: ",place)
# #
# # name()
#
# #----------------------------------------------------------------------------
# '''
# Exercise:
# Write a function absolutevalue(num) that computes the absolute value of
# a number. You will need to use an 'if' statement. Remember if a number is
# less than zero then you must multiply by -1 to make it greater than zero.
# Give output in the form:
#
# The absolute value of -5  is  5
# '''
# #solution :
# def absolutevalue(num):
#     if num<0:
#         absolute = num*(-1)
#         print("The absolute value of ",num," is ",absolute)
#     else:
#         absolute = num
#         print("The absolute value of ",num," is ",absolute)
#
# print("\n\n\n\n")
# absolutevalue(5)
# absolutevalue(-5)
# absolutevalue(4-4) #it is zero
# absolutevalue(3+-9) #it is -6
#
# print("\n---------------------------------\n")
# #-----------------------------------------------------------------------
#
# def fahrenheit_to_celsius2():
#     """ IMPROVED. Does some checking of input before using it.
#     Input from keyboard, which is always a string and must often be
#     converted to an int or float.
#     Converts Fahrenheit temp to Celsius.
#     Uses 'if' to make sure an entry was made.
#     """
#
#     temp_str = input("Enter a Fahrenheit temperature: ")
#     if temp_str:
#         temp = int(temp_str)
#         newTemp = 5*(temp-32)/9
#         print("The Fahrenheit temperature",temp,"is equivalent to ",end='')
#         print(newTemp,"degrees Celsius")
#
# fahrenheit_to_celsius2()
#
#
# print("-"*40)
#
#
# #%%
# """
# Test the program above by entering the temperature 212 and also by simply
# pressing 'Enter' or 'Return' key. Note the improvement. Now try entering 'a'.
# """
# #%%
# def fahrenheit_to_celsius3():
#     """ MORE IMPROVED. Does even more checking of input before using it.
#     Input from keyboard, which is always a string and must often be
#     converted to an int or float.
#     Converts Fahrenheit temp to Celsius.
#     Uses if to check whether input is a number and then uses .isdigit() method
#     of strings to check whether input is made of of digits.
#     """
#
#     temp_str = input("Enter a Fahrentheit temperature: ")
#     if temp_str:
#         if temp_str.isdigit():
#             temp = int(temp_str)
#             newTemp = 5*(temp-32)/9
#             print("The Fahrenheit temperature",temp,"is equivalent to ",end='')
#             print(newTemp,"degrees Celsius")
#         else:
#             print("You must enter a number. Bye")
# #%%
#
# fahrenheit_to_celsius3()
#
#
#------------------

def inches_to_feet1(inches):
    """ converts inches to feet and inches """
    feet = inches//12  # division by integer with fraction thrown away
    extra_inches = inches - 12*feet
    print(inches,"inches is",feet,"feet and",extra_inches,"inches")


inches_to_feet1(77)
#%%



print("-"*50)

#
# """
# Exercise: Rewrite inches_to_feet1(inches) calling it inches_to_feet2(inches)
# using % to compute the inches. Recall that 19 % 5 will give 4 (the remainder).
# Copy and paste the original into the solution area and modify to same typing
# time.
# """
# """
# Solution:
# """
#%%

def inches_to_feet2(inches):
    """ converts inches to feet and inches """
    feet = inches//12  # division by integer with fraction thrown away
    extra_inches = inches%12 #here is the difference ====  see in
    #========================= --------------------------------  inches_to_feet1() and compare
    print(inches,"inches is",feet,"feet and",extra_inches,"inches")

inches_to_feet2(77)


print("-"*50)
"""
# Exercise:
# Write a function count_down() that starts at 10 and counts down to rocket 
# launch. It's output should be 10 9 8 7 6 5 4 3 2 1 BLASTOFF! You can make
# all the numbers on the same line or different lines. Use a while loop.
# """
# """
# Solution:
# """
#
# def count_down():
#     count = 10
#     while count>0:
#         print(count,end=' ')
#         count -= 1
#     print("BLASTOFF! ")
#
# count_down()
#
# print("-"*50)
# """
# Exercise:
# Write a function countdown1() that starts at 10 and counts down to rocket
# launch. It's output should be 10 9 8 7 6 5 4 3 2 1 BLASTOFF! You can make
# all the numbers on the same line or different lines. Use a 'for' loop and
# range(). range has a start and a stop and a step that ---------- MAY BE NEGATIVE --------.
# """
# """
# Solution:
# """
# def countdown1():
#     for i in range(10,1,-1):
#         print(i,end=' ')
#     print("BLASTOFF!")
#
# countdown1()