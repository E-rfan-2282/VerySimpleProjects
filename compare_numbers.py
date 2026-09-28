def compare_numbers():

    num1 = int(input("Please enter the first number: "))

    num2 = int(input("Please enter the second number: "))

    if num1 > num2:

        print(num1, "is greater")

    elif num2 > num1:

        print(num2, "is greater")

    else:

        print("Both numbers are equal")


compare_numbers()