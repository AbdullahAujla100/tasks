import random
import copy_here

random_words=copy_here.random_words
words=random.choice(random_words)

lives=6
display=[]

for dashes in words:
    display+='_'   
print(display)

hint_indices = []

if  len(words) >= 6:
    hint_indices = [random.choice(range(len(words)))]

for idx in hint_indices:
    display[idx] = words[idx]

print("Hint applied:")
print(display)

game_over=False
while not game_over:
    guessed_word=input("Guess your  letter : ").lower()

    for position in range(len(words)):
        letter=words[position]
        if guessed_word == letter:
            display[position]=guessed_word
    print(display)        

    if guessed_word not in words:
        lives-=1
        print ("word not found")
        print (f"you have {lives} lives left ")
        if lives == 0:
            game_over= True
            print(f"You loose the word was : {words}")
            

    if '_' not in display:
        game_over=True  
        print("You win")          