import random
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

mode_list =["plus","random","times","devide"]

keep_going = ""
while keep_going =="":
    mode = random.choice(mode_list) 
    print(mode)
    loop = 1
    if mode == "plus":
        while loop<3:
            number_1 = random.randint(1,20)
            number_2 = random.randint(1,20)
            user_input = input("What is {} plus {}: ".format(number_1,number_2))
            answer = number_1 + number_2
            print(answer)
            if user_input == answer:
                print("correct")
            else:
                print("wrong")
            loop +=1
    elif mode =="times":
        while loop<3:    
            number_1 = random.randint(1,20)
            number_2 = random.randint(1,20)
            answer = number_1* number_2
            print(answer)
            user_input = input("What is {} times {}: ".format(number_1,number_2))
            if user_input == answer:
                print("correct")
            else:
                print("wrong")
            loop +=1
    elif mode == "random":
        while loop<10:
            print("do soon")
            loop +=1
    else:
        while loop<3:    
            number_1 = random.randint(1,20)
            number_2 = random.randint(1,20)
            user_input = input("What is {} minus {}: ".format(number_1,number_2))
            answer = number_1 - number_2
            print(answer)
            if user_input == answer:
                print("correct")
            else:
                print("wrong")
            loop +=1

    keep_going= input("press enter to keep looping")  

    


