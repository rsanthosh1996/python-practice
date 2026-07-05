x = int(input("enter a number "))
for i in range(2,x-1):
	if (x%i) == 0:
		print("its not prime")
		break
else:
	print("its prime")
