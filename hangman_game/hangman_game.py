import random
from hangman_art import LOGO, STAGES
from hangman_words import WORDS

MAX_REPEAT_WRONG = 2  # limit repeated wrong guesses


def choose_difficulty():
    while True:
        level = input("Choose difficulty (easy / medium / hard): ").lower()
        if level in WORDS:
            return level
        print("❌ Invalid difficulty.")


def get_random_word(level):
    return random.choice(WORDS[level])


def initialize_display(word):
    return ["_"] * len(word)


def print_status(display, wrong_guesses):
    print(STAGES[wrong_guesses])
    print("Word:", " ".join(display))


def process_guess(word, display, guess):
    correct = False
    for i, letter in enumerate(word):
        if letter == guess:
            display[i] = guess
            correct = True
    return correct


def play_game():
    print(LOGO)

    difficulty = choose_difficulty()
    word = get_random_word(difficulty)
    display = initialize_display(word)

    guessed_letters = set()
    wrong_guesses = 0
    repeated_wrong = {}

    max_wrong = len(STAGES) - 1

    print_status(display, wrong_guesses)

    while "_" in display and wrong_guesses < max_wrong:
        guess = input("\nGuess a letter: ").lower()

        # Validation
        if not guess.isalpha() or len(guess) != 1:
            print("❌ Enter a single alphabet.")
            continue

        if guess in guessed_letters:
            print("⚠️ Already guessed.")
            continue

        guessed_letters.add(guess)

        if process_guess(word, display, guess):
            print("✅ Correct!")
        else:
            repeated_wrong[guess] = repeated_wrong.get(guess, 0) + 1

            if repeated_wrong[guess] > MAX_REPEAT_WRONG:
                print("❌ Repeated wrong guess penalty!")
                wrong_guesses += 1

            wrong_guesses += 1
            print("❌ Wrong guess!")

        print_status(display, wrong_guesses)

    if "_" not in display:
        print("\n🎉 You WIN! Word was:", word)
    else:
        print("\n💀 You LOSE! Word was:", word)


def replay():
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").lower()
        if again != "y":
            print("👋 Thanks for playing!")
            break


if __name__ == "__main__":
    replay()