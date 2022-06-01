
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
    
    mode_select = 1
    # loops if +-/x is not entered
    while mode_select > 0:
        print()
        #get input for mode
        what_mode = input("what mode do you want to play for this round + - x / or enter for random mode: ").lower()
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
            
            #randomly generates what question to generate
            loop=0
            while loop < 10:
                random_mode = random.choice(all_list)
                print(random_mode)
                loop +=1
            
        
        #prints error message if anything tother than +-/x is entered
        else:
            print("please enter + - x or /")
            mode= "no"
        
        #breaks the error loop in less line of code than using break for every mode :)
        if mode !="no":
            mode_select = 0
    #asks to keep looping for testing
    print()
    keep_going= input("press enter to keep loping")