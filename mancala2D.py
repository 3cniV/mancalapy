import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PIT_SIZE = 50
PIT_MARGIN = 20
MANCALA_WIDTH = 100
MANCALA_HEIGHT = 300
PIT_COLOR = (100, 100, 100)
MANCALA_COLOR = (150, 150, 150)
BACKGROUND_COLOR = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mancala")

# Function to draw pits for a player
def draw_pits(player, num_pits):
    pit_y = SCREEN_HEIGHT // 2 if player == 'A' else SCREEN_HEIGHT // 4
    pit_spacing = (SCREEN_WIDTH - 2 * MANCALA_WIDTH - 2 * PIT_MARGIN - num_pits * PIT_SIZE) // (num_pits - 1)
    for i in range(num_pits):
        pit_x = MANCALA_WIDTH + PIT_MARGIN + i * (PIT_SIZE + pit_spacing)
        pygame.draw.circle(screen, PIT_COLOR, (pit_x, pit_y), PIT_SIZE)

# Function to draw Mancala for a player
def draw_mancala(player):
    mancala_y = SCREEN_HEIGHT // 2 - MANCALA_HEIGHT // 2 if player == 'A' else SCREEN_HEIGHT // 4 - MANCALA_HEIGHT // 2
    pygame.draw.rect(screen, MANCALA_COLOR, (0, mancala_y, MANCALA_WIDTH, MANCALA_HEIGHT))

# Function to draw the board
def draw_board():
    # Fill the background
    screen.fill(BACKGROUND_COLOR)

    # Draw player A's pits
    draw_pits('A', 6)

    # Draw player B's pits
    draw_pits('B', 6)

    # Draw player A's Mancala
    draw_mancala('A')

    # Draw player B's Mancala
    draw_mancala('B')

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the board
    draw_board()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

