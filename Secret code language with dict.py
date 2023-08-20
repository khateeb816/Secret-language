import os
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

dictnary = { 9 : "a",
            7 : "b",
            6: "c",
            8: "d",
            5:"e",
            3:"f",
            4:"g",
            1:"h",
            0:"i",
            2:"j",
            12:"k",
            10:"l",
            11:"m",
            20:"n",
            18:"o",
            19:"p",
            13:"q",
            15:"r",
            14:"s",
            17:"t",
            16:"u",
            26:"v",
            21:"w",
            23:"x",
            22:"y",
            25:"z",
            30:" "
            }
def get_key(val):

    for key, value in dictnary.items():
        if val == value:
          return key
 
    return "key doesn't exist"
userinput = int(input("\n Enter your selection: \n 1. Encode\n 2. Decode\n >>>> "))
if userinput == 1:
    clear_terminal()
    print("\n ---Welcome to Encoder---\n")
    txt_encode = input("\n Enter Your message to Encode: ")
    for word in txt_encode:
        for i in word:
            print(get_key(i), end=" ")

    input("\n Press Enter to exit......")
elif userinput == 2:
    clear_terminal()
    print("\n ---Welcome to Decoder---\n")
    txt_decode = input("\n Enter Your message to Decode: ")
    user_list = txt_decode.split()
    for i in user_list:
        print(dictnary[int(i)], end="")

    input("\n Press Enter to exit......")
else:
    clear_terminal()
    print("\n Invalid input try again")
    input("\n Press Enter to exit......")