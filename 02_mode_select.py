

#lists for diffrent inputs for the modes
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
        what_mode = input("what mode do you want to play for this round + - x / or enter for random mode: ")
        print()
        #outputs what mode is chosen
        if what_mode in plus:
            print("plus")
            mode_select = 0
        elif what_mode in minus:
            print("minus")
            mode_select = 0
        elif what_mode in devide:
            print("devide")
            mode_select = 0
        elif what_mode in times:
            print("times")
            mode_select = 0
        elif what_mode == "":
            print("random")
            mode_select = 0
        #prints error message if anything tother than +-/x is entered
        else:
            print("please enter + - x or /")
