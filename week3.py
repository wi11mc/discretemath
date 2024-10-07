#these functions work for converting decimal to binary and binary to decimal
def ConvertToBinary(decimal_num):
    return bin(decimal_num).replace("0b", "")

def ConvertToDecimal(binary_num):
    return int(binary_num, 2)
#variable to store choice
choice = 0

#while loop to display menu
while choice != 3:
    print("pick a number corresponding to what action you're trying to do:")
    print("1 convert decimal to binary")
    print("2 convert Binary to Decimal")
    print("3 quit")

    #processes the choice
    choice = int(input())

    if choice == 1:
        #converts decimal to binary
        decimal_num = int(input("choose decimal number: "))
        binary_result = ConvertToBinary(decimal_num)
        print(f"your number in binary: {binary_result}")
    elif choice == 2:
        #binary to decimal
        binary_num = input("choose binary number: ")
        decimal_result = ConvertToDecimal(binary_num)
        print(f"your number in decimal is: {decimal_result}")
    elif choice == 3:
        #quits on choice 3
        print("quitting the program")
        quit()
    else:
        #bad choice
        print("you cant choose that")
