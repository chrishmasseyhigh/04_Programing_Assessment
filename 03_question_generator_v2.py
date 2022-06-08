
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

#lists all the modes to chose from for testing
mode_list =["plus","minus","times","devided","random"]
random_mode_list =["plus","minus","times","devided"]
all_list = ["plus","minus","devided","times"]
keep_going = ""

while keep_going =="":
    #generates mode for testing
    mode = "random" #random.choice(mode_list) 
    
    #if random mode is chosen random mode is activated if not is is deacvtivated
    if mode == "random":
        random_mode = True
    else:
        random_mode=False
    print(mode)
    loop = 1
    
    #loop for testing
    while loop<7:
            #generates numbers for answers
            number_1 = random.randint(1,10)
            number_2 = random.randint(1,10)
            
            #resets the loop for devide mode
            loop_devide = False
            
            #generates answer based on mode
            
            #gereates a random mode for every quetion
            if random_mode == True:
                mode = random.choice(random_mode_list)  
            
            
            #devide mode
            
            if mode == "devided":
                #loops until the answer is an intiger
                while loop_devide == False:
                    number_1 = random.randint(1,50)
                    number_2 = random.randint(1,50)
                    answer = number_1 / number_2
                    #checks if answer is an itiger and breaks the loop if not
                    loop_devide = (answer.is_integer())

            #forms answer buy - two diffrent numbers
            elif mode == "minus":
                    answer = number_1 - number_2

            #forms answer buy * two diffrent numbers 
            elif mode == "times":
                    answer = number_1 * number_2

            #forms answer buy + two diffrent numbers
            else:
                    answer = number_1 + number_2

            #gets the input from the user
            user_input = intcheck("What is {} {} {} ".format(number_1,mode,number_2),exit_code="xxx")

            print(user_input)
            print(answer)   
            #checks if answer is wrong or right.
            if user_input == answer:
                print("correct")
            else:
                print("wrong")
            loop +=1



    keep_going= input("press enter to keep looping")  

    
