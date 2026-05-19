# Activity 1 - Draw a Rectangle

"""import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(30, 30, 60, 60))
    pygame.display.flip()

# Activity 2 - Hollow and Filled Cirlce

import pygame

pygame.init()
# Create the display surface object of specific dimension
window = pygame.display.set_mode((400, 400))
# Fill the screen with white color
window.fill((255, 255, 255))
# Define colors
Green = (0, 255, 0)
# Draw solid circle
pygame.draw.circle(window, Green, (300, 300), 50)
# Draw outlined circle
pygame.draw.circle(window, Green, (100, 100), 50, 3)
# Draws the surface object to the screen
pygame.display.update()
# Game loop
running = True
while running:
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit pygame
pygame.quit()"""

# Activity 3 - Color changing bouncing square

import pygame

def main():
    pygame.init()
    screen_width, screen_height = 500, 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Color changing sprite")

    # Mapping of color names to RGB values
    colors = {
        "Red" : pygame.Color("Red"),
        "Green" : pygame.Color("Green"),
        "Blue" : pygame.Color("Blue"),
        "Yellow" : pygame.Color("Yellow"),
        "White" : pygame.Color("White")
    }
    current_color = colors["White"]
    x, y = 30, 30
    sprite_width, sprite_height = 60, 60

    clock = pygame.time.Clock()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_a]: x -= 3
        if pressed[pygame.K_d]: x += 3
        if pressed[pygame.K_w]: y -= 3
        if pressed[pygame.K_s]: y += 3

        x = min(max(0, x), screen_width - sprite_width)
        y = min(max(0, y), screen_height - sprite_height)

        # Change color based on boundary contact
        if x == 0: current_color = colors["Blue"]
        elif x == screen_width - sprite_width: current_color = colors["Yellow"]
        elif  y == 0: current_color = colors["Red"]
        elif y == screen_height - sprite_height:
            current_color = colors["Green"]
        else:
            current_color = colors["White"]

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, current_color, (x, y, sprite_width, sprite_height))
        
        pygame.display.flip()
        clock.tick(90)

    pygame.quit()
if __name__ == "__main__":
    main()