import pygame
import random

pygame.init()

# ---------------- SCREEN ----------------
screen = pygame.display.set_mode((700, 650))
pygame.display.set_caption("Word Hunter")

# ---------------- COLORS ----------------
WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
BLUE = (50, 120, 255)
GREEN = (50, 200, 100)
RED = (220, 50, 50)
YELLOW = (255, 200, 50)
GRAY = (100, 100, 100)

# ---------------- FONTS ----------------
title_font = pygame.font.Font(None, 55)
font = pygame.font.Font(None, 32)

# ---------------- WORDS ----------------
words = [
    "PYTHON",
    "ARRAY",
    "STRING",
    "LOOP",
    "FUNCTION"
]

# ---------------- HINTS ----------------
hints = [
    "A programming language",
    "A collection of elements",
    "A sequence of characters",
    "Repeats a block of code",
    "A reusable block of code"
]

# Alphabet
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# ---------------- START GAME ----------------
def start_game():

    number = random.randint(0, len(words) - 1)

    word = words[number]
    hint = hints[number]

    guessed = []
    lives = 6
    score = 0
    game_over = False

    return word, hint, guessed, lives, score, game_over


# Start the game
word, hint, guessed, lives, score, game_over = start_game()


# ---------------- BUTTONS ----------------
play_again_button = pygame.Rect(180, 570, 170, 50)
exit_button = pygame.Rect(370, 570, 150, 50)


# ---------------- MAIN LOOP ----------------
running = True

while running:

    # Background
    screen.fill(BLACK)

    # ---------------- TITLE ----------------
    title = title_font.render("WORD HUNTER", True, BLUE)
    screen.blit(title, (235, 30))


    # ---------------- HINT ----------------
    hint_text = font.render(
        "Hint: " + hint,
        True,
        YELLOW
    )

    screen.blit(hint_text, (150, 100))


    # ---------------- DISPLAY WORD ----------------
    display_word = ""

    for letter in word:

        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "


    word_text = title_font.render(
        display_word,
        True,
        WHITE
    )

    screen.blit(word_text, (220, 160))


    # ---------------- LIVES ----------------
    lives_text = font.render(
        "Lives: " + str(lives),
        True,
        RED
    )

    screen.blit(lives_text, (50, 240))


    # ---------------- SCORE ----------------
    score_text = font.render(
        "Score: " + str(score),
        True,
        GREEN
    )

    screen.blit(score_text, (570, 240))


    # ---------------- LETTER BUTTONS ----------------
    buttons = []

    for i in range(26):

        # Button position
        x = 80 + (i % 9) * 65
        y = 290 + (i // 9) * 55

        button = pygame.Rect(
            x,
            y,
            50,
            40
        )

        buttons.append(button)


        # Change color if letter is already guessed
        if letters[i] in guessed:
            pygame.draw.rect(
                screen,
                GRAY,
                button
            )
        else:
            pygame.draw.rect(
                screen,
                BLUE,
                button
            )


        # Letter inside button
        letter_text = font.render(
            letters[i],
            True,
            WHITE
        )

        screen.blit(
            letter_text,
            (x + 15, y + 7)
        )


    # ---------------- CHECK WIN ----------------
    if all(letter in guessed for letter in word):

        game_over = True

        result = font.render(
            "YOU WIN! 🎉",
            True,
            GREEN
        )

        screen.blit(
            result,
            (290, 525)
        )


    # ---------------- CHECK LOSE ----------------
    elif lives == 0:

        game_over = True

        result = font.render(
            "GAME OVER! Word: " + word,
            True,
            RED
        )

        screen.blit(
            result,
            (230, 525)
        )


    # ---------------- PLAY AGAIN + EXIT ----------------
    if game_over:

        # Play Again button
        pygame.draw.rect(
            screen,
            GREEN,
            play_again_button
        )

        # Exit button
        pygame.draw.rect(
            screen,
            RED,
            exit_button
        )


        # Play Again text
        play_text = font.render(
            "PLAY AGAIN",
            True,
            BLACK
        )

        play_x = play_again_button.x + (
            play_again_button.width -
            play_text.get_width()
        ) // 2

        play_y = play_again_button.y + (
            play_again_button.height -
            play_text.get_height()
        ) // 2

        screen.blit(
            play_text,
            (play_x, play_y)
        )


        # Exit text
        exit_text = font.render(
            "EXIT",
            True,
            WHITE
        )

        exit_x = exit_button.x + (
            exit_button.width -
            exit_text.get_width()
        ) // 2

        exit_y = exit_button.y + (
            exit_button.height -
            exit_text.get_height()
        ) // 2

        screen.blit(
            exit_text,
            (exit_x, exit_y)
        )


    # Update screen
    pygame.display.update()


    # ---------------- EVENTS ----------------
    for event in pygame.event.get():

        # Close window
        if event.type == pygame.QUIT:
            running = False


        # Mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_position = pygame.mouse.get_pos()


            # ---------------- GAME IS RUNNING ----------------
            if not game_over:

                for i in range(26):

                    if buttons[i].collidepoint(
                        mouse_position
                    ):

                        letter = letters[i]


                        # Check if already guessed
                        if letter not in guessed:

                            guessed.append(letter)


                            # Correct guess
                            if letter in word:
                                score += 10

                            # Wrong guess
                            else:
                                lives -= 1


            # ---------------- GAME IS OVER ----------------
            else:

                # PLAY AGAIN
                if play_again_button.collidepoint(
                    mouse_position
                ):

                    word, hint, guessed, lives, score, game_over = start_game()


                # EXIT
                elif exit_button.collidepoint(
                    mouse_position
                ):

                    running = False


# Close Pygame
pygame.quit()



