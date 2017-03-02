'''
 	mario.py

	Printing of custom Mario pyramide.

	Usage        : python3 mario.py
	Description  : http://docs.cs50.net/problems/mario/more/mario.html

'''

# ask for height untill get it.
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


# main
def main():
	Height 	  = ask()
	for line in range(1, Height+1) :
		Padding = " " * ( Height - line )
		Bricks = "#" * ( line  )
		print( Padding + Bricks + " " * 2 + Bricks + Padding )

if __name__ == '__main__':
	main()
