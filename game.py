import random 
from words import word_list


def get_word():
    word = random.choice(word_list)
    return word.lower()

def play(word):
    word_display = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Let's start your word has %d letter. you have %d tries" %(len(word) ,tries))
    print(word_display)
    print("\n")

    while not guessed and tries > 0:

        guess = input("guess: ").lower()

        if len(guess) == 1 and guess.isalpha(): # guess in harf olup olmadığını sorguluyoruz isalpha() ile
            if guess in guessed_letters:
                print("the %s letter is already guessed" %(guess))
            elif guess not in word:
                tries -= 1
                print("the %s letter is not in word. Remaining tries: %d" %(guess, tries))
                guessed_letters.append(guess)
            else:
                print("%s letter is in word" %(guess))
                guessed_letters.append(guess)
                
                word_as_array = list(word_display)
                indices = [i for i, letter in enumerate(word) if letter == guess] # enumerate içerisine tanımladığımız değeri nesne olarak döndürür burda kelimemi harflere parçalıyorum eğer harf ile guess tutuyorsa i for i diyerek indexini bir dizi halinde geriye döndürüyorum 
                for index in indices:
                    word_as_array[index] = guess 
                word_display = "".join(word_as_array) # word displayi arada boşluk olmayacak şekilde word as array ile birleştiriyoruz
                if "_" not in word_display:
                    guessed = True
                    
        
        elif len(guess) == len(word) and guess.isalpha():
            if guess == word:
                guessed = True
                word_display = word 
            elif guess in guessed_words:
                print("%s word is already guessed" %(guess))

            else:
                tries -= 1
                print("%s is not the true. remaining tries: %d" %(guess, tries))
                guessed_words.append(guess)
        else: 
            print("invalid guess")

        print(word_display)
        print("\n")
        
    if guessed:
        print("You found the word.")
    else:
        print("you lose :( The word is: %s" %(word))

def main():
    word = get_word()
    play(word)
    while input("do you wanna play again? (Y/N)").upper() == "Y":
        word = get_word()
        play(word)

main()
        