import random

xmls = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def function():
	a = ""
	for i in range(6):
		a += random.choice(xmls)
	return "%s.mp4"%a

def main():
	open(function(),"wb").write(open(input().replace('"',''),"rb").read()[2:])

if __name__ == '__main__':
	main()







	
