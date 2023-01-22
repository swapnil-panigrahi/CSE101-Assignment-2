import requests
from random import randint

words = ["apple", "table", "green", "smile", "happy", "watch", "light", "water", "plant", "fruit", "woman", "child", "world", "house", "small", "sound", "paper", "group", "study", "night", "beach", "south", "north", "motel", "abuse", "river", "field", "adult", "heart", "music", "sport", "gamer", "dance", "party", "store", "hotel", "plane", "later", "biker", "train", "horse", "mouse", "place", "break", "carry", "shoot","agent", "basis", "blood","chain","claim"]

x=randint(0,len(words)-1)
chosen_word=words[x]

chances=1
guessed=["_","_","_","_","_"]

while chances<=6:
    guess=input("\nEnter a 5 letter guess: ")

    url = "https://api.dictionaryapi.dev/api/v2/entries/en/"            #API call
    url+=guess
    response=requests.get(url)

    if len(guess)!=5:
        print("Guess isn't 5 letter word!")
        continue
    elif response.status_code==404:
        print("Word entered isn't a valid word")
    else:
        wrong_place=[]

        for i in range(len(chosen_word)):
            if guess[i]==chosen_word[i]:
                guessed[i]=guess[i]
            elif guess[i] in chosen_word:
                wrong_place.append(guess[i])
        else:
            print("".join(guessed))
            if not "".join(guessed)==chosen_word:
                print("Other letters: ", end="")
            
                for i in wrong_place:
                    if i not in guessed:
                        print(i,end=' ')
            else:
                print("Good Game! Well Played")
                break
            
        chances+=1
        
else:
    print("The word was:",chosen_word)
    print("Skill Issue! Get Good!")