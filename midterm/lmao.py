import random 


with open("fakenews.csv","w") as f:
	for i in range(250):
		f.write(str(random.randint(0,1))+ "\n")