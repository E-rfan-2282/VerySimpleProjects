def مقایسه():
	num1 = int(input("لطفا عدد اول را وارد کنید"))
	num2 = int(input("لطفا عدد دوم را وارد کنید"))
	if num1 > num2:
		print (num1,"بزرگتر است")
	elif num2 > num1:
		print (num2,"بزرگتر است")
	else:
		print ("هر دو عدد مساوی هستند")
مقایسه()