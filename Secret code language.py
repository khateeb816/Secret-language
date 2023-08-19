# write a program to generate the random string in upper and lower case letters.  
import random  
import string  
def Upper_Lower_string(length): 
    result = ''.join((random.choice(string.ascii_lowercase) for x in range(length))) # run loop until the define length  
    return result

user = int(input("\n Enter your option: \n 1. Encode\n 2. Decode \n >>>> "))
if user == 1:
    #Encoder
    user_input = input("\n Enter your message: ")
    user_input2 = user_input.split()
    output=[]

    for word in user_input2:
        if len(word) <= 3:
            temp = word[::-1]
            output.append(temp)
        else:
            temp1 = word[1:len(word)]
            temp =  temp1 + word[0]
            output.append(temp)

    user_output = ' '.join(output)
    user_output2 =[]
    for xyx in output:
        temp = xyx + Upper_Lower_string(3)
        temp = Upper_Lower_string(3) + temp
        user_output2.append(temp)
        user_output = ' '.join(user_output2)
        input("\n Press enter to exit")
    print(user_output)
elif user == 2:
    #decoder
    user_input = input("\n Enter your message: ")
    user_input2 = user_input.split()
    output=[]

    for word in user_input2:
        if len(word) <= 3:
            temp = word[::-1]
            output.append(temp)
        else:
            temp1 = word[3:len(word)-4]
            temp = word[len(word) - 4] + temp1
            output.append(temp)

    user_output = ' '.join(output)
    print(user_output)
    input("\n Press enter to exit")
else:
    print("\n Invalid input Try again")
