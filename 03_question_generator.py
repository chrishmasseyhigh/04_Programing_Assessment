import random


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

    


