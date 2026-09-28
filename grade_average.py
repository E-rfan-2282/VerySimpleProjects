def average_of_grades():
    number_of_lessons = int(input("Enter the number of lessons:\n"))
    grades = []

    def get_grades():
        grade = int(input("What is your grade?\n"))
        grades.append(grade)
    for repeat_of_questions_for_grades in range(number_of_lessons):
        get_grades()
    print("\n", grades)
    make_sure = input("Are these your grades?(yes or no)\n")
    if make_sure.upper().strip() == "YES":
        sum_of_the_grades = sum(grades)
        average = "\n{} It is the average of your grades\n"
        print(average.format(sum_of_the_grades/number_of_lessons))
    if make_sure.upper().strip() == "NO":
        print("Ok,please run the code again")
    run_again = input("\n\nDo you want to run the code again?(yes or no)\n")
    if run_again.upper().strip() == "YES":
        average_of_grades()
    elif run_again.upper().strip() == "NO":
        print("\nThanks for using.")


average_of_grades()
