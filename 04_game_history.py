import random
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

#main rotine


keep_going= ""

#loop for testing
while keep_going == "":
    
    #resets all values
    list_amount = 0
    wins = 0
    loses = 0
    questions = 0
    rounds_played = 0
    
    #makes history for testing
    user_input_history_list =[4,7,1,8,1,6,1,6,1,4,89,1,35,1,4,245,325,43,12,11]
    result_history_list = ["win","loss","win","loss","win","loss","win","loss","win","loss","win","loss","xxx","loss","win","loss","win","win","loss","win"]
    rounds_played = intcheck("how many rounds? ", low = 0)
    questions = rounds_played *10

    # prints first round
    if rounds_played >0:
        print("-----------round 1-----------")

    next_round =1
    items = 0
    # prints user history
    while items < rounds_played:
        #breaks if no questions are answered
        if questions == 0:
            break
        round = 1
        mini_loop = 0
        
        choice = 1
        # loops for each round
        while mini_loop <10 :
            #gets the right item for each guess
            user_history = user_input_history_list[list_amount]
            result_history = result_history_list[list_amount]
            #prints what was chosen
            print("{} choice ".format(choice))
            print(" you chose ({}) number was was ({})".format(user_history,result_history))
            #breaks if ueser exits mid round
            if result_history == "xxx":
                mini_loop = 13
            choice +=1
            mini_loop +=1
            list_amount +=1
        items +=1

        #breaks if only one round played
        if items == rounds_played:
            break
        
        #prints the round
        elif rounds_played >1:
            next_round +=1
            print()
            print("-----------round {}------------".format(next_round))
        
        else:
            break
    keep_going = input("press enter to keep loping ")