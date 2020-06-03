### Daniel Ryaboshapka
### march 1st 2020 

speedmarker = "Speed"
inputmarker = "Input"

with open("overall_tests", "r") as f:
	with open("tests.csv","w") as f2:
		for line in f: 
			if speedmarker in line:
				f2.write(str(line.split(" ")[2].split("\n")[0])+", ")
			else: 
				f2.write(str(line.split(" ")[4]))
