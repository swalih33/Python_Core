vehicle=["cycle","car","jeep"]
print("list=",vehicle)
selection=str(input("enter your selection;"))
comp_gues=random.randrange[0,2]
gues=vehicle[comp_gues]
if(selection==gues):
	print("you won")
else:
	print("you fail")
print("your selection=",selection)
print("comp_gues=",gues)
