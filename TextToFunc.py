"""
Enter a text string and the script returns a function 
representation string compatible with desmos
"""
SPACEOFCHAR = 0.25 #the size of a space between 2 char
SPACESIZE = 1 #the size of a space string " "

Letters = {

		# @ represents the start index
		# the last number in each lists represents the length of the char

	' ':[SPACESIZE],

	'A':[r'2(x-@)\left\{@ <= x <= @+1\right\}',
	 	r'-2(x-@-2)\left\{@+1 <= x <= @+2\right\}',
	  	r' 1\left\{@+0.5 <= x <= @+1.5\right\}',
	  	2],

	'B':[r'x=@\left\{0 <= y <= 2\right\}',
	 	r'(x-(@+0.5))^2+(y-1.5)^2=0.25\left\{@+0.5 <= x <= @+1\right\}',
	  	r' y=0\left\{@ <= x <= @+0.5\right\}',
	  	r' y=1\left\{@ <= x <= @+0.5\right\}',
	  	r' y=2\left\{@ <= x <= @+0.5\right\}',
	  	r'(x-(@+0.5))^2+(y-0.5)^2=0.25\left\{@+0.5 <= x <= @+1\right\}',
	  	1],

	'C':[r'(x-@-1)^2+(y-1)^2=1\left\{@ <= x <= @+1.75\right\}',
		1.75],

	'D':[r'x=@\left\{0 <= y <= 2\right\}',
		r'2\left\{@ <= x <= @+0.5\right\}',
		r'0\left\{@ <= x <= @+0.5\right\}',
		r'(x-(@+0.5))^2 + (y-1)^2=1\left\{@+0.5 <= x \right\}',
		1.5],

	'E':[r'x=@\left\{0 <= y <= 2\right\}',
		r'2\left\{@ <= x <= @+1\right\}',
		r'1\left\{@ <= x <= @+1\right\}',
		r'0\left\{@ <= x <= @+1\right\}',
		1],

	'F':[r'x=@\left\{0 <= y <= 2\right\}',
		r'2\left\{@ <= x <= @+1\right\}',
		r'1\left\{@ <= x <= @+1\right\}',
		1],

	'G':[r'(x-(@+1))^2 + (y-1)^2=1\left\{@ <= x <= @+1.75\right\}',
		r'1\left\{@+1 <= x <= @+1.75\right\}',
		r'x=@+1.75\left\{0.35 <= y <= 1\right\}',
		1.75],

	'H':[r'x=@\left\{0 <= y <= 2\right\}',
		r'x=@+1\left\{0 <= y <= 2\right\}',
		r'1\left\{@ <= x <= @+1\right\}',
		1],

	'I':[r'x=@+0.5\left\{0 <= y <= 2\right\}',
		r'0\left\{@ <= x <= @+1\right\}',
		r'2\left\{@ <= x <= @+1\right\}',
		1],

	'J':[r'x=@+1\left\{0.5 <= y <= 2\right\}',
		r'2\left\{@+0.5 <= x <= @+1.5\right\}',
		r'(x-(@+0.5))^2 + (y-0.5)^2=0.25\left\{0 <= y <= 0.5\right\}',
		1.5],

	'K':[r'x=@\left\{0 <= y <= 2\right\}',
		r'-x+@+1\left\{@ <= x <= @+1\right\}',
		r'x-@+1\left\{@ <= x <= @+1\right\}',
		1],

	'L':[r'x=@\left\{0 <= y <= 2\right\}',
		r'y=0\left\{@ <= x <= @+1.25\right\}',
		1.25],

	'M':[r'x=@\left\{0 <= y <= 2\right\}',
		r'x=@+2\left\{0 <= y <= 2\right\}',
		r'-x+@+2\left\{@ <= x <= @+1\right\}',
		r'x-@\left\{@+1 <= x <= @+2\right\}',
		2],

	'N':[r'x=@\left\{0 <= y <= 2\right\}',
		r'x=@+1.5\left\{0 <= y <= 2\right\}',
		r'-4/3x+(4/3)@+2\left\{@ <= x <= @+1.5\right\}',
		1.5],

	'O':[r'(x-(@+1))^2 + (y-1)^2=1',
		2],

	'P':[r'x=@\left\{0 <= y <= 2\right\}',
		r'2\left\{@ <= x <= @+0.5\right\}',
		r'1\left\{@ <= x <= @+0.5\right\}',
		r'(x-(@+0.5))^2 + (y-1.5)^2=0.25\left\{@+0.5 <= x <= @+1\right\}',
		1],

	'Q':[r'(x-(@+1))^2+(y-1)^2=1',
		r'-x+@+2\left\{@+1.5 <= x <= @+2\right\}',
		2],

	'R':[r'x=@\left\{0 <= y <= 2\right\}',
		r'2\left\{@ <= x <= @+0.5\right\}',
		r'1\left\{@ <= x <= @+0.5\right\}',
		r'-2(x-@-0.5)+1\left\{@+0.5 <= x <= @+1\right\}',
		r'(x-(@+0.5))^2+(y-1.5)^2=0.25\left\{@+0.5 <= x <= @+1\right\}',
		1],

	'S':[r'(x-(@+0.5))^2+(y-1.5)^2=0.25\left\{y>1.5\right\}',
		r'(x-(@+0.5))^2+(y-1.5)^2=0.25\left\{@ <= x <= @+0.5\right\}',
		r'(x-(@+0.5))^2+(y-0.5)^2=0.25\left\{@+0.5 <= x <= @+1\right\}',
		r'(x-(@+0.5))^2+(y-0.5)^2=0.25\left\{0 <= y <= 0.5\right\}',
		1],

	'T':[r'x=@+1\left\{0 <= y <= 2\right\}',
		r'2\left\{@ <= x <= @+2\right\}',
		2],

	'U':[r'(x-(@+0.5))^2 +(y-0.5)^2=0.25\left\{0 <= y <= 0.5\right\}',
		r'x=@\left\{0.5 <= y <= 2\right\}',
		r'x=@+1\left\{0.5 <= y <= 2\right\}',
		1],

	'V':[r'2\left|x-@-1\right|\left\{@ <= x <= @+2\right\}',
		2],

	'W':[r'-2\left|x-@-1\right|+1\left\{@+0.5 <= x <= @+1.5\right\}',
		r'4(x-@-2)+2\left\{@+1.5 <= x <= @+2\right\}',
		r'-4(x-@)+2\left\{@ <= x <= @+0.5\right\}',
		2],

	'X':[r'\left|x-@-1\right|+1\left\{@ <= x <= @+2\right\}',
		r'-\left|x-@-1\right|+1\left\{@ <= x <= @+2\right\}',
		2],

	'Y':[r'\left|x-@-1\right|+1\left\{@ <= x <= @+2\right\}',
		r'x=@+1\left\{0 <= y <= 1\right\}',
		2],

	'Z':[r'2\left\{@ <= x <= @+2\right\}',
		r'0\left\{@ <= x <= @+2\right\}',
		r'x-@\left\{@ <= x <= @+2\right\}',
		2]
}



def charToFunc(c, startIndex):
	global Letters
	global SPACEOFCHAR
	funcList = ''
	for func in Letters[c]:
		if isinstance(func, int) or isinstance(func, float): # the lest argument of the list is the char length
			endIndex = startIndex+func
		else:
			funcList += func
			funcList += '\n'

	return (endIndex + SPACEOFCHAR ,funcList.replace('@', str(startIndex)))


def textInterpreter(text):
	funcString = ''
	startIndex = 0 #the index that the next character should start at
	for char in text:
		startIndex, charString = charToFunc(char, startIndex)
		funcString += charString
	return funcString





def main():
	print("Enter your text")
	inputText = input()
	funcString = textInterpreter(inputText)
	print(funcString)


if __name__ == '__main__':
	main()
