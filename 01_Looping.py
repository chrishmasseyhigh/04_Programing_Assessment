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


#asks user for how many rounds they want to play or they can press ener for ininite mode
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
    exit = intcheck("what is the answer? ", exit_code="xxx")
    if exit == "xxx":
        break
print()
print("end")

