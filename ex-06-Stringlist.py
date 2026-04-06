word = str(input("Enter a word: "))
word = word.lower()
stringlist = list(word)
reversedlist = stringlist[::-1]
if stringlist == reversedlist:
    print("The word is a palindrome.")
else:    print("The word is not a palindrome.") 