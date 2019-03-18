amount=input("Enter amount to withdraw:")
amount=int(amount)
rupees=(2000,500,200,100)
if amount%2==0:
	print("processing")
	for i in rupees:
		if amount<100:
			print("balance:",amount,":smaller denomination notes cannot be accessed through ATM")
			break
		if amount<i:
			continue
		q=amount//i
		r=amount%i
		if r//i<1:
			print(i,"note=",q,"nos=>",i,"*",q,"=",i*q)
			amount=r
			if amount==0:
				break
else:
	print("Coins cannot be accessed")	