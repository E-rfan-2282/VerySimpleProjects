def average_of_grades():
	number_of_lessons = int(input("Enter the number of lessons:\n"))
	grades = []
	def questions_for_grades():
		grades_questions = int(input("What is your grade?\n"))
		grades.append(grades_questions)
	for repeat_of_questions_for_grades in range(number_of_lessons):
		questions_for_grades()
	print ("\n",grades)
	make_sure = input("Are these your grades?(yes or no)\n")
	corrected_to_make_sure = make_sure.upper()
	if corrected_to_make_sure.strip() == "YES":
		sum_of_the_grades = sum(grades)
		average = "\n{} It is the average of your grades\n"
		print (average.format(sum_of_the_grades/number_of_lessons))
	if corrected_to_make_sure.strip() == "NO":
		print ("Ok,please run the code again")
	run_again = input("\n\nDo you want to run the code again?(yes or no)\n")
	corrected_of_run_again = run_again.upper()
	if corrected_of_run_again.strip() == "YES":
		average_of_grades()
	elif corrected_of_run_again.strip() == "NO":
		print ("\nThanks for use.")
average_of_grades()
