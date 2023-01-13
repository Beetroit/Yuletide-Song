num_dict= {1:"First",2:"Second",3:"Third",4:"Fourth",5:"Fifth",6:"Sixth",7:"Seventh",8:"Eigth",9:"Ninth",10:"Tenth",11:"Eleventh",12:"Twelvth"}
def yule(num):
	responses={1:"A patridge in a pear tree.",2:"Two turtle doves",3:"Three french hens",4:"Four calling birds",5:"Five gold rings",6:"Six geese a laying",7:"Seven swams a swimming",8:"Eight Maids a milking",9:"Nine ladies dancing",10:"Ten lords a leaping",11:"Eleven pipers piping",12:"Twelve drummers drumming"}
	#print(num_dict[num],responses[num])
	return responses[num]
	

def main(num):
	lst=[yule(i) for i in range(num,0,-1)]
	if len(lst) >1:
		lst.insert(-1,"and")
	print(f"On the {num_dict[num]} day of christmas my true love gave to me, ",end="")
	print(", ".join(lst))

condition=True
while condition:
	def again():
		cont = input("Again? ")
		if cont[0].lower()=="y":
			condition=True
		else:
			print("Goodbye and Merry Christmas in Advance")
			condition=False
		return condition
	num=int(input("Enter gift number (1-12) "))
	if num >12:
		print("A year has only 12 months")
		condition=again()
	else:
		main(num)
		print()
	