def isSeq(n: int):
	if n < 10:
		return 1
	
	SN = list(map(int, list(str(n))))
	L = [SN[0]]
	
	S = n % 10 - (n//10) % 10
	
	for i in SN[1:]:
		if i == L[-1] + S:
			L.append(i)
		else:
			return 0
	return 1

if __name__ == "__main__":
	ns = 0
	for i in range(1, int(input())+1):
		ns += isSeq(i)
	print(ns)
