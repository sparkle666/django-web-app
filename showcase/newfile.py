import math
area = 0
def calculate_circle(raduis):
	for x in range(0,11):
		area = math.pi **2 * raduis
		print("Num", x, "First area is: ", area) 
	return area		
calculate_circle(8)

def calculate_15(number):
	for x in range(0, 101):
		print("Number * 15 is: ", x*number)

calculate_15(15)