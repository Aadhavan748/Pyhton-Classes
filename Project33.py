import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))

pygame.display.set_caption("My first game screen")

background_color = (58, 58, 58)

image = pygame.image.load("image.png")
image = pygame.transform.scale(image, (300, 300))

image_x = (500 - 300) // 2
image_y = (500 - 300) // 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_color)

    screen.blit(image, (image_x, image_y))

    pygame.display.flip()

pygame.quit()