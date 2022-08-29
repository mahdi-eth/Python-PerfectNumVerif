def perfect_checker(input_number):
    check_list = 0
    for i in range(1, input_number - 1):
        if input_number % i == 0:
            check_list += i
    if check_list == input_number:
        print(True," It is a perfect number :) \n")
    else:
        print(False," It is not a perfect number :( \n\n","...FYI the answrer was ",check_list , "\n")


input_number = int(input("Enter a number to see if it's perfect : "))
perfect_checker(input_number)
