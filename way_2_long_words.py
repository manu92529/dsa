
num_words = int(input())

for i in range(num_words):
	word = input()

	length=len(word)
	if(length>10):
		print(word[0], length - 2, word[length - 1], sep="")
	else:
		print(word)
	