a=0
while True:
	b=raw_input("Enter Number: ")
	if b=='':
		break
	elif b.isdigit()==True:
		i=int(b)
		a=a+i
print('sum of your Number: %d' %a)
