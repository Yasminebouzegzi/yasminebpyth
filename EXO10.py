word = input("Please type in a word: ")
is_palindrome = True
j=len(word)
for i in range(j // 2):
    # Compare characters from the start and the end using negative indexing
    if word[i] != word[j-1-i]:
        is_palindrome = False
        break

if is_palindrome:
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.")
