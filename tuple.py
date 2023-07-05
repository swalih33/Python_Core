vehicles=("car","bus","cycle")
print(len(vehicles))
tup2=1,2,3
tup3=vehicles+tup2
print(tup3)
if "bus" in vehicles:
	print("bus is found")
else:
	print("bus is not in the list")
for x in vehicles:
	print(x)
z=list(vehicles)
print(z)
z[0]="jeep"
print(z)
vehicles=tuple(z)
print(vehicles)