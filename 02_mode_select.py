from lib2to3.pgen2.token import PLUS
import random

#lists for diffrent inputs for the modes
all_list = ["plus","minus","devide","times"]
plus = ["+","plus","p"]
minus = ["-","minus","m"]
devide =["/","devide","d"]
times = ["x","*","times","t"]
keep_going = ""
#loop for testing
while keep_going =="":
    print()
    keep_going= input("press enter to keep loping")
    mode_select = 1
    # loops if +-/x is not entered
    while mode_select > 0:
        print()
        #get input for mode
        what_mode = input("what mode do you want to play for this round + - x / or enter for random mode: ")
        print()
        #outputs what mode is chosen
        if what_mode in plus:
            print("plus")
            mode = "plus"

        elif what_mode in minus:
            print("minus")
            mode = "minus"
   
        elif what_mode in devide:
            print("devide")
            mode = "devide"
      
        elif what_mode in times:
            print("times")
            mode = "times"
         
        elif what_mode == "":
            print("random")
            mode = "random"
            random_mode = random.choice(all_list)
            print(random_mode)
            
        
        #prints error message if anything tother than +-/x is entered
        else:
            print("please enter + - x or /")
            mode= "no"
        
        if mode !="no":
            mode_select = 0
