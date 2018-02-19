t = ()

def rate(vote):
	l = list(t)
	l.append(vote)
	print('a',l)
	ave = sum(l)/len(l)
	return ave

print(rate(10))
print(rate(5))