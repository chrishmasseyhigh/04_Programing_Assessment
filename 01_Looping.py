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

rounds_wanted = intcheck("How many rounds?  Press <enter> for infinite mode: ", 1, exit_code = "")
mode=""
if rounds_wanted == "":
    mode = "infinite"
    rounds_wanted = 10 
input_2 =0
# play it
rounds_played = 0
user = 0
#loops for desiered amount
while rounds_played < rounds_wanted:
    if mode == "infinite":
        rounds_wanted +=1
    rounds_played += 1
    #displays round 
    print()
    print("-----Round {}-----".format(rounds_played))
    print()
    #asks to exit
    exit = intcheck("what is the number? ",0,10, exit_code="xxx")
    if exit == "xxx":
        break


