s = str(input ('введи строку '))
l = len(s)
a = 0
b = 0
for i in range (0,l):
	if s[i] == ')':
		a = a+1
	if s[i] == '(':
		b = b+1
if a == b:
	print ('одинаковое')
else:
	print ('неодинаковое')

