print("Welcome\n")
while True:
    number = int(input("Enter the number:"))
    if number < 0:
        print(f"\n{abs(number)}")
    elif number > 0:
        print(f"\n{number - (number*2)}")
    else:
        print(f"\n{number}")
    run_again = (
        input("Do you want to run the program again?(yes or no) ").strip()).upper()
    if run_again == "YES":
        print("Welcome\n")
    else:
        break
print("Thanks for using.")
