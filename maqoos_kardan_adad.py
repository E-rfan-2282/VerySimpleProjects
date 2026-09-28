print("Welcome\n")
while True:
    number = int(input("Enter the number:"))
    if number < 0:
        print(f"\n{abs(number)}")
    elif number > 0:
        print(f"\n{number - (number*2)}")
    else:
        print(f"\n{number}")
    r_again = (
        input("Do you want to run the program again?(yes or no) ").strip()).upper()
    if r_again == "YES":
        print("Welcome\n")
    else:
        break
print("Thanks for used.")
