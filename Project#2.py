#Project HangMan
import random
def HangMan():
    play = True
    while(play):
        words = ["happy","code","chill","pop","lofi","coding","hangman",
                  "sad","covid","cuarentena"]
        chosen_word = random.choice(words).lower()
        player_guess = None
        word_guessed = []
        guessed_letter = []
        for x in chosen_word:
            word_guessed.append("-")
        joined_word = None

        hangman = (
        """
        ---------
        ||      |  
        ||      
        ||      
        ||      
        ||      
        ||      
        ||        
        ==============
        """,
        """
        ---------
        ||      |  
        ||      O
        ||      
        ||      
        ||      
        ||     
        ||       
        ==============
        """,
        """
        ---------
        ||      |  
        ||      O
        ||      T 
        ||      
        ||      
        ||      
        ||        
        ==============
        """,
        """
        ---------
        ||      |  
        ||      O
        ||     /T
        ||      
        ||      
        ||     
        ||       
        ==============
        """,
        """
        ---------
        ||      |  
        ||      O
        ||     /T\ 
        ||      
        ||      
        ||     
        ||       
        ==============
        """,
        """
        ---------
        ||      |  
        ||      O
        ||     /T\ 
        ||      |
        ||      
        ||     
        ||       
        ==============
        """,
        """
        ---------
        ||      |  
        ||      O
        ||     /T\ 
        ||      |
        ||      |
        ||     
        ||        
        ==============
        """,
        """
        ---------
        ||      |  
        ||      O
        ||     /T\ 
        ||      |
        ||      |
        ||     | 
        ||       
        ==============
        """,
        """
        ---------
        ||      |  
        ||      O
        ||     /T\ 
        ||      |
        ||      |
        ||     | 
        ||     L   
        ==============
        """,
        """
        ---------
        ||      |  
        ||      O
        ||     /T\ 
        ||      |
        ||      |
        ||     | |
        ||     L 
        ==============
        """,
         """
        ---------
        ||      |  
        ||      O
        ||     /T\ 
        ||      |
        ||      |
        ||     | |
        ||     L L
        ==============
        """)
        print(hangman[0])  
        attemps = len(hangman) - 1
        while(attemps != 0 and "-" in word_guessed):
            print(("Have {} attemps.").format(attemps))
            joined_word = " ".join(word_guessed)
            print(joined_word)

            try:
                player_guess = str(input("Enter a letter: ")).lower()
            except:
                print("Input invalid!")
                continue
            else:
                if not player_guess.isalpha():
                    print("Try again with a letter.")
                    continue
                elif player_guess in guessed_letter:
                    print(("Try a letter other than {}").format(player_guess))
                    continue
                elif len(player_guess) > 1: 
                    print("Try again with only one letter")
                    continue
                else:
                    pass
            guessed_letter.append(player_guess)

            for x in range(len(chosen_word)):
                if player_guess == chosen_word[x]:
                    word_guessed[x] = player_guess
            if player_guess not in chosen_word:
                attemps -= 1
                print(hangman[(len(hangman)-1)-attemps])
        if "-" not in word_guessed:
            print("You win!")
            print(("The chosen word is {}").format(chosen_word))
        else:
            print("Bad luck!")
            print(("The chosen word is {}").format(chosen_word))
        break
if __name__ == "__main__":
    HangMan()