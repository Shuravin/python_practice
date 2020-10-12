print("Please think of a number between 0 and 100")

numGuesses = 0
start = 0
end = 101
guess = int((start + end) / 2)

while numGuesses <= 100:
    print("Is your secret number", guess, "?")
    print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    ans = str(input())
    if ans == 'h':
        end = guess
        guess = int((start + end) / 2)
    elif ans == 'l':
        start = guess
        guess = int((start + end) / 2)
    elif ans == 'c':
        print("Game over. Your secret number was:", guess)
        print("Your secret number was guessed after", numGuesses, "tries")
        break
    numGuesses += 1