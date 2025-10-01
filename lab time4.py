numbers=list(map(int, input('Please enter a sequence of numbers: ').split()))



odd_count=0

even_count=0

for i in numbers:
    if i==0:
        break

    if i%2==0:
        odd_count=odd_count+1


    else:
        even_count=even_count+1


print(f"the even count is: {even_count}")
print(f"the odd count is: {odd_count}")

print()


word=input("input a word: ")

new_word = []

for i in word:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        continue
    else:   
        new_word.append(i)


new_word="".join(new_word)
print(f"the new word is: {new_word}")