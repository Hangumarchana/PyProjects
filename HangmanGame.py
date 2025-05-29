import random

word_list = [
    "apple", "banana", "cherry", "orange", "mango",
    "grape", "melon", "kiwi", "lemon", "peach",
    "pear", "plum", "apricot", "blueberry", "raspberry",
    "coconut", "fig", "papaya", "guava", "lychee"
]

hangManDiagram = [
    """
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    """,
    """
    +---+
    |   |
        |
        |
        |
        |
    =========
    """
]


list_length = len(word_list)


random_word=random.randint(0,list_length-1)

random_word_letter=len(word_list[random_word])
print("The word has ",random_word_letter,"letters.")

list_word=[]
word_blank=["_"]*len(word_list[random_word])

for line in word_blank:
    print(line,end=" ")

lives=6
while lives>0 and "_" in word_blank:
    print("")
    while True:
        guess=input("Guess a letter: ").lower()
        if len(guess)!=1:
            print("You can only guess a single letter")

        elif  not guess.isalpha():
            print("You can only guess a letter")


        elif len(guess)==1 and  guess.isalpha():
            break


    if guess in list_word:
        print("You already guessed that letter")
    elif guess in word_list[random_word]:
        print("Good Guess")
        if guess not in list_word:
            list_word.append(guess)

        for i in range(len(word_list[random_word])):
            if word_list[random_word][i]==guess:
                word_blank[i]=guess


        for line in word_blank:
            print(line,end=" ")
        print("")
        print("HangMan Diagram:")
        print(hangManDiagram[lives])








    else:
        print("Sorry, that letter is not in the word")
        lives-=1
        print("You have",lives,"lives left")
        print("HangMan Diagram:")
        print(hangManDiagram[lives])

if "_" not in word_blank:
    print("\n🎉 Congratulations! You guessed the word!")
    print(f"The word was: {word_list[random_word]}")

else:
    print(f"\n💀 Game over! The word was: {word_list[random_word]}")





