# Displays instructions, returns ""
def instructions():
    print()
    statement_decorator("How To Play",".")

    print('''

       *****************************************************************************************************************************
       * ------------------------------------------------------------------------------------------------------------------------- ******************
       * |In this game you will choose the amount of rounds to play for a number or infinite and what mode to play for each round|----------------- *
       * |( divide, plus, times,minus and random - random will chose a different mode for every question eg minus for one and plus for the other.)| * 
       * |You can enter xxx to quit at any time and round history will be displayed at the end|```````````````````````````````````````````````````` *
       * ````````````````````````````````````````````````````````````````````````````````````` ******************************************************
       *****************************************************************************************

    ''',)

    return""

#statement decorator
def statement_decorator(statement, decoration):
    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement,sides)
    top_bottom = decoration * len(statement)
    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

#Yes or no checker
def yes_no(question):
    yes_ok = ["no","n","nope"]
    no_ok = ["yes","y","yep"]

    valid= False 
    while not valid:
            response = input(question).lower()
            #if they say yes, output 'program continues'
            if response in no_ok:
                response= "yes"
                return response
            #if they say no, output 'displays instructions'
            elif response in yes_ok:
                response= "no"
                return response

            #else, output'Please enter yes or no'
            else:
                print()
                print("Please enter yes or no")
                print()

#main rotine
played_before = yes_no("have you played before? ")
if played_before =="no":
    instructions()