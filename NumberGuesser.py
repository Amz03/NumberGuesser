import pygame
import random
import sys

pygame.init()

#--Display 
Width, Height = 700, 500 #Screen pixel size
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Guess The Number!") #Sets display name on the game

#--Colours to be used
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (173, 216, 230)
DARK_BLUE = (0, 102, 204)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
GREY = (220, 220, 220)

#--Font
fontlarge = pygame.font.SysFont("Comic Sans MS", 48, bold=True)
fontmedium = pygame.font.SysFont("Arial", 32)
fontsmall = pygame.font.SysFont("Arial", 24)

#--Variables for the game
number = random.randint(1, 100) # Computer generated random number
user_text = '' #Temporary storage for what is to be written into the empty box
feedback = "Guess a number between 1 and 100" #Telling the user to guess a number
attempts = 0
maxattempts = 7 #Number of attempts the user has
score = 0
games_played = 0
games_won = 0
game_over = False

#-- Reset the Game
def reset_game():
    global number, user_text, feedback, attempts,game_over
    number = random.randint(1, 100) #Generates a random number between 1-100
    user_text = ''
    feedback = "Guess a number between 1 and 100"
    attempts = 0
    game_over = False

#-- Display Text
def display_text(text, y, color=BLACK, font=fontmedium, center=True):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(Width/2, y)) if center else (10, y)
    screen.blit(text_surface, text_rect)

#- Loop
running = True
while running:
    screen.fill(LIGHT_BLUE) #Background colour is light blue
    #Title
    display_text("Guess The Number!", 60, DARK_BLUE, fontlarge) #Title text is dark blue
    #Feedback
    display_text(feedback, 150,BLACK, fontmedium)
    # Input box
    pygame.draw.rect(screen,WHITE, pygame.Rect(Width/2 - 100, 200, 200, 50), border_radius=10) #White input box to enter guesses
    input_surface = fontmedium.render(user_text, True, BLACK) #Number user inputs
    screen.blit(input_surface, (Width/2 - 90, 210))
    # Display attempts and stats
    display_text(f"Attempts: {attempts}/{maxattempts}", 280, BLACK) #Display the number of attempts in Black font
    display_text(f"Score: {score} | Games Played:{games_played} | Wins: {games_won}", 330, BLACK, fontsmall) #Displays the scores and statistics in Black font
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if not game_over:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key ==pygame.K_RETURN:
                    if user_text.isdigit():
                        guess = int(user_text)
                        attempts += 1
                        if guess < number:
                            feedback = "Too low! Try Again."
                        elif guess > number:
                            feedback = "Too high! Try Again."
                        else:
                            feedback = f"CONGRATULATIONS! The number was {number}"
                            score += (maxattempts-attempts+1) * 10
                            games_won += 1
                            game_over = True
                        if attempts >= maxattempts and not game_over:
                            feedback = f"Oh no... Out of attempts! The number was {number}"
                            game_over = True
                    else:
                        feedback = "Enter a valid number!"
                    user_text = ''
                elif event.unicode.isdigit() and len(user_text) < 3:
                    user_text += event.unicode
            else:
                # If the game is over, allow '1' to reset
                if event.key == pygame.K_1:
                    games_played += 1
                    reset_game()

    # If the game is over, show restart message
    if game_over:
        display_text("Press '1' to play again or ESC to quit", 400, RED, fontsmall) # 1 to play again or ESC to quit

    pygame.display.flip() #Updates the graphics in real time

pygame.quit() #Pygame quites the game
