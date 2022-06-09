import random


user_input_history_list =[4,7,1,8,1,6,1,6,1,4,89,1,35,1,4,245,325,43,12,11]
result_history_list = ["win","loss","win","loss","win","loss","win","loss","win","loss","win","loss","win","loss","win","loss","win","win","loss","win"]
list_amount = 0
wins = 0
rounds_played = 0
loses = 0
questions = 0
rounds_played = random.randint(0,2)
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
        choice +=1
        mini_loop +=1
        list_amount +=1
    items +=1

    #breaks if only one round
    if items == rounds_played:
        break
    
    #prints the round
    elif rounds_played >1:
        next_round +=1
        print()
        print("-----------round {}------------".format(next_round))
    
    else:
        break
    