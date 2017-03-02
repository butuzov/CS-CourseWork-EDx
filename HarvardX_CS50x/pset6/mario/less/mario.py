'''
 	mario.py

	Printing of custom Mario pyramide.

	Usage        : python3 mario.py
	Description  : http://docs.cs50.net/problems/mario/less/mario.html

'''
def ask():
	while True:
		HeightStr = input("Height:")
		Height 	  = 0;

		if HeightStr.isdigit() :
			Height = int(HeightStr)
		else :
			continue

		if Height not in range(1, 24):
			return ask()

		return Height

def main():

	# this long code used to
	# learn about inputs and analize
	# instead cs50 library.
	Height 	  = ask()

	for line in range(1, Height+1) :
		print( ( " " * ( Height - line) ) + ( "#" * ( line + 1 ) ) )

if __name__ == '__main__':
	main();
