def user_info():
    first_name = input ('Pleas inter your first name:\n')
    last_name = input ('pleas inter your last name:\n')
    your_info = {
    'First_name' : first_name.title(),
    'Last_name' : last_name.title()
    }
    print (your_info)
    c = input ('\nIs it your info?(yes or no)\n')
    if c == 'no' :
        user_info()
    if c == 'yes' :
        print ("Hello!",' ',first_name.title(),' ',last_name.title())
      
user_info()