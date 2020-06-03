
string = "Hello my name is Daniel"
check = string.split(" ")
for word in check: 
	if 'e' in word: 
		print("E is in %(word)s" % {"word": word}) 
		print("E is in ", word)