import random

#functions go here

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

# Displays instructions, returns ""
def instructions():
    print()
    statement_decorator("How To Play",".")

    print('''

       *****************************************************************************************************************************
       * ------------------------------------------------------------------------------------------------------------------------- ******************
       * |In this game you will choose the amount of rounds to play for a number or infinite and what mode to play for each round|----------------- *
       * |( divide, plus, times,minus and random - random will chose a different mode for every question eg minus for one and plus for the other.)| * 
       * |You can enter xxx to quit at any time and round history will be displayed at the end. Each round has 7 questions``````````````````````````*
       * ``````````````````````````````````````````````````````````````````````````````````````````````````````````````````**************************
       *****************************************************************************************

    ''',)

    return""


#**************************main rotine***************************       
 
#lists all the modes to chose from for testing
mode_list =["plus","minus","times","divided","random"]
random_mode_list =["plus","minus","times","divided"]
high_number_list=["plus","devided"]
keep_going = ""

#sets up all the history
result_history_list = []
user_input_history_list = []
wins = 0
rounds_played = 0
loses = 0
questions = 0 
#lists for diffrent inputs for the modes
all_list = ["plus","minus","devide","times"]
plus = ["+","plus","p"]
minus = ["-","minus","m"]
devide =["/","devide","d"]
times = ["x","*","times","t"]
keep_going = ""
 
 
statement_decorator("welcome to the basic math game","+")
print()
#asks if user has played before and dispays instrictions if they enter no
played_before = yes_no("have you played before? ")
print()
if played_before =="no":
    instructions()

#asks user for how many rounds they want to play or they can press ener for ininite mode
rounds_wanted = intcheck("How many rounds?  Press <enter> for infinite mode: ", 1, exit_code = "")
mode=""

#infinite mode
if rounds_wanted == "":
    mode = "infinite"
    rounds_wanted = 10 


# play it
rounds_played = 0

#loops for desiered amount
while rounds_played < rounds_wanted:
    if mode == "infinite":
        rounds_wanted +=1
    
    mode_select = 1
    # loops if +-/x is not entered
    while mode_select > 0:
        print()
        #get input for mode
        what_mode = input("what mode do you want to play for this round + - x / or enter for random mode: ").lower()
        print()
        #outputs what mode is chosen
        if what_mode in plus:
            mode = "plus"

        elif what_mode in minus:
            mode = "minus"
   
        elif what_mode in devide:
            mode = "devide"
      
        elif what_mode in times:
            mode = "times"
         
        elif what_mode == "":
            mode = "random"

        #exits if xxx is entered
        elif what_mode == "xxx":
            mode = "xxx"
        #prints error message if anything tother than +-/x is entered
        else:
            print("please enter + - x or /")
            mode= "no"
        
        #breaks the error loop in less line of code than using break for every mode :)
        if mode !="no":
            mode_select = 0
    
    rounds_played +=1
    
    #breaks cod if xx is enetered
    if mode == "xxx":
        break
    #displays round 
    print()
    print("---------Round {}---------".format(rounds_played))
    print()
    question_loop = 0
    

    #if random mode is chosen random mode is activated if not is is deacvtivated
    if mode == "random":
        random_mode = True
    else:
        random_mode=False
    print("{} mode".format(mode))
    loop = 1
        
    #resets the loop for devide mode
    loop_devide = False
                
    #loops for 10 quesses
    while question_loop <7: 
        #generates answer based on mode
                
        #generates numbers for answers
                
        #generates a high number for devide and plus
        if mode in high_number_list:
            number_1 = random.randint(1,30)
            number_2 = random.randint(1,30)
                
        #generates a smaller number for minus and times mode
        else:
            number_1 = random.randint(1,12)
            number_2 = random.randint(1,12)
        
        #gereates a random mode for every quetion
        if random_mode == True:
            mode = random.choice(random_mode_list)  
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
        print()
        user_input = intcheck("What is {} {} {} ".format(number_1,simple_mode,number_2),low = 0, exit_code="xxx")
        print()

        #breaks if exit code is entered
        if user_input =="xxx":
            user_input_history_list.append(user_input)
            result_history_list.append(result) 
            result = "xxx"
            break
                

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
            
        question_loop +=1
print("****************************************game history****************************************")




print()
print("round history")
print()
# prints first round
if rounds_played >0:
    print("-----------round 1-----------")


list_amount= 0
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
    while mini_loop <7:
        #gets the right item for each guess
        user_history = user_input_history_list[list_amount]
        result_history = result_history_list[list_amount]
        #prints what was chosen
        print("{} choice ".format(choice))
        print(" you chose ({}) the guess was ({})".format(user_history,result_history))
        #breaks if ueser exits mid round
        if user_history == "xxx":
            break
        
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
