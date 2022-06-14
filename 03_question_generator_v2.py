
import random
import math
from turtle import right
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

#lists all the modes to chose from for testing
mode_list =["plus","minus","times","divided","random"]
random_mode_list =["plus","minus","times","divided"]
high_number_list=["plus","devided"]
keep_going = ""

result_history_list = []
user_input_history_list = []
#main rotine
wins = 0
rounds_played = 0
loses = 0
questions = 0
while keep_going =="":

    #generates mode for testing
    mode = random.choice(mode_list) 
    
    #if random mode is chosen random mode is activated if not is is deacvtivated
    if mode == "random":
        random_mode = True
    else:
        random_mode=False
    print(mode)
    loop = 1
    
    #loop for testing
    while loop<7:
           
            #resets the loop for devide mode
            loop_devide = False
            
            #generates answer based on mode
            
            #gereates a random mode for every quetion
            if random_mode == True:
                mode = random.choice(random_mode_list)  
            
            #generates numbers for answers
            
            #generates a high number for deive and plus
            if mode in high_number_list:
                number_1 = random.randint(1,30)
                number_2 = random.randint(1,30)
            
            #generates a smaller number for minus and times mode
            else:
                number_1 = random.randint(1,15)
                number_2 = random.randint(1,15)
            #devide mode
            
            if mode == "divided":
                number_3 = number_1 * number_2
                answer = number_3 / number_2
                number_1 = number_3
                simple_mode = "/"
            
            #forms answer buy - two diffrent numbers
            elif mode == "minus":
                    number_3 = number_1 * number_2
                    answer = number_3 - number_2
                    number_1 = number_3
                    simple_mode = "-"
            #forms answer buy * two diffrent numbers 
            elif mode == "times":

                    answer = number_1 * number_2
                    simple_mode = "*"
            #forms answer buy + two diffrent numbers
            else:
                    answer = number_1 + number_2
                    simple_mode = "+"
            #gets the input from the user
            user_input = intcheck("What is {} {} {} ".format(number_1,simple_mode,number_2),low = 0, exit_code="xxx")
            
            #breaks if exit code is entered
            if user_input =="xxx":
                break
            
            #prints answer and input for testing
            print(user_input)
            print(answer)   
            
            #checks if answer is wrong or right.
            if user_input == answer:
                print("correct")
                wins +=1
                result = "right"
            else:
                print("wrong")
                result = "wrong"
                loses +=1
            user_input_history_list.append(user_input)
            result_history_list.append(result) 
            questions +=1
            loop +=1
    #breaks if exit code is entered
    if user_input =="xxx":
                break 
    rounds_played +=1

    keep_going= input("press enter to keep looping")  

print(rounds_played)
print(questions)
print(wins)
print(loses)    
