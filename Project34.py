import pygame

pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("My first game screen")

WHITE = (255, 255, 255)
BLUE = (0, 122, 204)
BLACK = (0, 0, 0)

rect_width = 150
rect_height = 100
center_x = (WIDTH - rect_width) // 2
center_y = (HEIGHT - rect_height) // 2
my_rect = pygame.Rect(center_x, center_y, rect_width, rect_height)

font = pygame.font.Font(None, 36)
text_surface = font.render("This is my game", True, BLACK)
text_rect = text_surface.get_rect(center=(WIDTH // 2, 80))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, my_rect)
    screen.blit(text_surface, text_rect)

    pygame.display.flip()

pygame.quit()