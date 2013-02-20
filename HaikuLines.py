import random
def haikuLines(numSyl):
	tmp=0
	lines=[]
	x=random.randint(1, 3)
	lines.append(x)
	if x==numSyl:
		return lines
	else:
		rest=(numSyl-x)
		if rest>1:
			y=random.randint(1,rest)
		else:
			y=1
		lines.append(y)
		total =x+y
		if (total==numSyl):
			return lines
		else:
			rest=numSyl-(x+y)
			if rest==1:
				z=1
				lines.append(z)
				return lines
			else:
				z=random.randint(1,rest)
				lines.append(z)
				if ((x+y+z)==numSyl):
					return lines
				else:
					a=numSyl-(x+y+z)
					lines.append(a)
					return lines
	for element in lines:
		tmp=tmp+element
	if element!=numSyl:
		print "ERROR"

haiku = open("haiku.html",'w')
def makeHaiku(sylnums, file1,file2,file3,file4,file5):
	one =[]
	two =[]
	three=[]
	x=haikuLines(sylnums)
	for element in x:

		if element==1:
			x=file1.readline
			if not x:
				file1.seek(0)
			else:
				one.append(file1.readline())
		elif element==2:
			x=file2.readline
			if not x:
				file2.seek(0)
			else:
				one.append(file2.readline())
		elif element==3:
			x=file3.readline
			if not x:
				file3.seek(0)
			else:
				one.append(file3.readline())
		elif element==4:
			x=file4.readline
			if not x:
				file4.seek(0)
			else:
				one.append(file4.readline())
		elif element==5:
			x=file5.readline
			if not x:
				file5.seek(0)
			else:
				one.append(file5.readline())
	sone="".join(one)
	sone = sone.replace("\n"," ")
	return sone
red="<div class = \"box red\" >"
pink="<div class = \"box pink\" >"
grey="<div class = \"box grey\" >"
blue="<div class = \"box blue\" >"
green="<div class = \"box green\" >"
redName="<div class = \"name obama\" > Obama"
pinkName="<div class = \"name abortion\" > Abortion " 
greyName="<div class = \"name guns\" > Guns"
blueName="<div class = \"name taxes\" > Taxes"
greenName="<div class = \"name gay\" >Gay"
css="<link href=\"style.css\" rel=\"stylesheet\" type=\"text/css\" /> \n"
js= "<script src=\"http://code.jquery.com/jquery-1.9.1.min.js\"></script> \n<script src=\"http://code.jquery.com/jquery-migrate-1.1.1.min.js\"></script>"
haiku.write(css)
haiku.write(js)
haiku.write("\n \n")
haiku.write(red)
haiku.write("</div> \n")
haiku.write("\n \n")
haiku.write(blue)
haiku.write("</div> \n")
haiku.write("\n \n")
haiku.write(pink)
haiku.write("</div> \n")
haiku.write("\n \n")
haiku.write(green)
haiku.write("</div> \n")
haiku.write("\n \n")
haiku.write(grey)
haiku.write("</div> \n")
haiku.write("\n \n")
haiku.write(redName)
haiku.write("</div> \n")
haiku.write("\n \n")
haiku.write(blueName)
haiku.write("</div> \n")
haiku.write("\n \n")
haiku.write(pinkName)
haiku.write("</div> \n")
haiku.write("\n \n")
haiku.write(greenName)
haiku.write("</div> \n")
haiku.write("\n \n")
haiku.write(greyName)
haiku.write("</div> \n")
haiku.write("\n \n")
f1 = open('/Users/CodyFulcher/Desktop/Haiku/obama/1.txt', 'r')
f2 = open('/Users/CodyFulcher/Desktop/Haiku/obama/2.txt', 'r')
f3 = open('/Users/CodyFulcher/Desktop/Haiku/obama/3.txt', 'r')
f4 = open('/Users/CodyFulcher/Desktop/Haiku/obama/4.txt', 'r')
f5 = open('/Users/CodyFulcher/Desktop/Haiku/obama/5.txt', 'r')
letter =["obama a","obama b","obama c","obama d","obama e","guns a","guns b","guns c","guns d","guns e", "abortion a","abortion b","abortion c","abortion d","abortion e","taxes a","taxes b","taxes c","taxes d","taxes e","gay a","gay b","gay c","gay d","gay e","y","z"]
j=0
while j<25:
	if j==0:
		f1 = open('/Users/CodyFulcher/Desktop/Haiku/obama/1.txt', 'r')
		f2 = open('/Users/CodyFulcher/Desktop/Haiku/obama/2.txt', 'r')
		f3 = open('/Users/CodyFulcher/Desktop/Haiku/obama/3.txt', 'r')
		f4 = open('/Users/CodyFulcher/Desktop/Haiku/obama/4.txt', 'r')
		f5 = open('/Users/CodyFulcher/Desktop/Haiku/obama/5.txt', 'r')
	if j==6:
		f1 = open('/Users/CodyFulcher/Desktop/Haiku/guns/1.txt', 'r')
		f2 = open('/Users/CodyFulcher/Desktop/Haiku/guns/2.txt', 'r')
		f3 = open('/Users/CodyFulcher/Desktop/Haiku/guns/3.txt', 'r')
		f4 = open('/Users/CodyFulcher/Desktop/Haiku/guns/4.txt', 'r')
		f5 = open('/Users/CodyFulcher/Desktop/Haiku/guns/5.txt', 'r')
	if j==11:
		f1 = open('/Users/CodyFulcher/Desktop/Haiku/abortion/1.txt', 'r')
		f2 = open('/Users/CodyFulcher/Desktop/Haiku/abortion/2.txt', 'r')
		f3 = open('/Users/CodyFulcher/Desktop/Haiku/abortion/3.txt', 'r')
		f4 = open('/Users/CodyFulcher/Desktop/Haiku/abortion/4.txt', 'r')
		f5 = open('/Users/CodyFulcher/Desktop/Haiku/abortion/5.txt', 'r')
	if j==16:
		f1 = open('/Users/CodyFulcher/Desktop/Haiku/taxes/1.txt', 'r')
		f2 = open('/Users/CodyFulcher/Desktop/Haiku/taxes/2.txt', 'r')
		f3 = open('/Users/CodyFulcher/Desktop/Haiku/taxes/3.txt', 'r')
		f4 = open('/Users/CodyFulcher/Desktop/Haiku/taxes/4.txt', 'r')
		f5 = open('/Users/CodyFulcher/Desktop/Haiku/taxes/5.txt', 'r')
	if j==21:
		f1 = open('/Users/CodyFulcher/Desktop/Haiku/gay/1.txt', 'r')
		f2 = open('/Users/CodyFulcher/Desktop/Haiku/gay/2.txt', 'r')
		f3 = open('/Users/CodyFulcher/Desktop/Haiku/gay/3.txt', 'r')
		f4 = open('/Users/CodyFulcher/Desktop/Haiku/gay/4.txt', 'r')
		f5 = open('/Users/CodyFulcher/Desktop/Haiku/gay/5.txt', 'r')
	i = letter[j]
	z=j/5
	print z
	tag = "<div class = \"poem "+i+"\" >"
	haiku.write(tag)
	one = makeHaiku(7,f1,f2,f3,f4,f5)
	haiku.write(" "+one+"<br> \n")
	two = makeHaiku(5,f1,f2,f3,f4,f5)
	haiku.write(" "+two+"<br> \n")
	three = makeHaiku(7,f1,f2,f3,f4,f5)
	haiku.write(" "+three+"<br> \n")
	haiku.write("</div> \n")
	j=j+1
print one, "\n", two ,"\n", three