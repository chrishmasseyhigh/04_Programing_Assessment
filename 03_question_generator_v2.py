
from lib2to3.pgen2.token import PLUS
import random
import math
#Functions go here






# Number checking function goes here
def intcheck(question, low=None, high=None, exit_code = None):

    while True:

        # sets up error messages
        if low is not None and high is not None:
            error = "Please enter an integer between {} and {} (inclusive)".format(low, high)
        elif low is not None and high is None:
            error = "Please enter an integer that is more than or equal to {}".format(low)
        elif low is None and high is not None:
            error = "Please enter an integer that is less than or equal to {}".format(high)
        else:
            error = "Please enter an integer"

        try:
            response = input(question)
            
            # check to see if response is the exit code and return it
            if response == exit_code:
                return response
            
            # change the response into an integer
            else:
                response = int(response)

            # Checks response is not too low, not use of 'is not' keywords
            if low is not None and response < low:
                print(error)
                continue

            # Checks response is not too high
            if high is not None and response > high:
                print(error)
                continue

            return response

        # checks input is a integer
        except ValueError:
            print(error)
            continue


mode_list =["plus","minus","times","devided"]
all_list = ["plus","minus","devided","times"]
keep_going = ""
while keep_going =="":
    mode = "devided"
    #random.choice(mode_list) 
    print(mode)
    loop = 1
    
    #loop for testing
    while loop<3:
            number_1 = random.randint(1,10)
            number_2 = random.randint(1,10)
            loop_devide = False
            
            #modes
            
            #devide mode
            if mode == "devided":
                #while loop_devide == True:
                while loop_devide == False:
                    number_1 = random.randint(1,50)
                    number_2 = random.randint(1,50)
                    answer = number_1 / number_2
                    loop_devide = (answer.is_integer())

            #minus mode
            elif mode == "minus":
                    answer = number_1 - number_2

            #times mode    
            elif mode == "times":
                    answer = number_1 * number_2

            #random mode
            elif mode == "random":
                    random_mode = random.choice(all_list)

            #plus mode       
            else:
                    answer = number_1 + number_2

            user_input = intcheck("What is {} {} {} ".format(number_1,mode,number_2),exit_code="xxx")

            print(user_input)
            print(answer)   
            if user_input == answer:
                print("correct")
            else:
                print("wrong")
            loop +=1



    keep_going= input("press enter to keep looping")  

    
