def user_info():
    first_name = input('Please enter your first name:\n')
    last_name = input('Please enter your last name:\n')
    your_info = {
        'First_name': first_name.title(),
        'Last_name': last_name.title()
    }
    print(your_info)
    check = input('\nIs it your info?(yes or no)\n')
    if check == 'no':
        user_info()
    if check == 'yes':
        print("Hello!", ' ', first_name.title(), ' ', last_name.title())


user_info()
