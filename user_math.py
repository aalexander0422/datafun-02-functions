"""
Always start with a docstring that describes what the module does.
Include your name and the date.

Use built-in functions and 
functions from the math module.

To illustrate the ability to call functions and 
display useful results to the user. 

Use your textbook and the examples in this repo to get ideas.

"""

import math

# define some functions

def get_area_of_lot(length, width):
    """
    Return area of a lot given the length and width of the lot.

    Could this fail?

    """

    # Use a try / except / finally block when something 
    # could go wrong
    try: 
        area = length * width 
        return area
    except Exception as ex:
        print(f"Error: {ex}")
        return None


# define more functions here (see instuctions)


def total_pounds_lifted(reps, weight): 
    # returns total pounds lifted per set
    tpounds = reps * weight
    return tpounds

def sum_of_pounds(setone, settwo, setthree):
    # returns the sum of pounds
    sumpounds = math.fsum([setone,settwo,setthree]) 
    return sumpounds
def range_of_sets(Highestset, Lowestset):
    # Returns the range of the set 
    range = Highestset - Lowestset 
    return range


# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    print("Explore some functions in the math module")
    print()
    print(f"math.comb(5,1) = {math.comb(5,1)}")
    print(f"math.perm(5,1) = {math.perm(5,1)}")
    print(f"get area of lot(6,2) = {get_area_of_lot(6,2)}")
    print(f"total pounds(14,12) = {total_pounds_lifted(14,12)}")
    print(f"Sum of pounds(14,12,14) = {sum_of_pounds(14,12,14)}")
    print(f"Range of sets(22, 14) = {range_of_sets(22,14)}")
