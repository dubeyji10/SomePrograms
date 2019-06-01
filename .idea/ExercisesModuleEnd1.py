# - ExercisesModuleEnd1.py *- coding: utf-8 -*-
""" Find and correct all the errors in the following Python functions.
    To run one, click in the cell (between two lines) and type Ctrl-Enter for
    Windows or Command-Return for a Mac.  Then enter the name of the function
    into the IPython console.  For example, to run the first one enter
    print_phrase() and press return.
"""
""" 
Exercise 1 
"""
#%% #error ':' was not put after function declaration ......... (corrected )
def print_phrase():
    phrase = "Now is the time" #quote was missing ...... corrected
    print(phrase)
#%%
""" 
Exercise 2
"""
#%%
def favorite_sport(favorite):
    sport = favorite #originally --- "favorite"
    print("Your favorite sport is",sport) # original -- .print("Your favorite sport is",sport)
    #corrected - removed the period in the beginning
#%%
""" 
Exercise 3 
"""
#%%
def username(yourname):
    print("Your name is",yourname) #here --- youname ---------- corrected now
#%%
"""
Exercise 4
"""
#%%
def compare_numbers(x,y):
    if x == y: #assignment was done = instead of comparision ==
        print("they are equal")
    else : #colon absent -----
        print(x, "and", y, 'are not equal')
        #%%
        """
Exercise 5
"""
#%%
def count_by_5():
    """ Count from 5 to 100 in steps of 5 """
    """ 5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100 """
    print ('Counting from 5 through 100 in steps of 5') #parentheses of print function were absent  --
    ct = 5
    while ct < 100:
        print(ct, end = " ")
        ct = ct + 5
#%%
print("\n running after removing errors - ----- - - - \n")
print_phrase()
favorite_sport("football")
username("asd")
compare_numbers(4,6)
count_by_5()