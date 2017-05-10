s = str(input ('введи строку '))
l = len(s)
a = 0
b = 0
for i in range (0,l+l,2):
	a = str(ord(s[i]))
	b = s[i+1]
	s[i+1] = a
	s[i+2] = b
for i in range (0,l+l):
	print (s[i])
