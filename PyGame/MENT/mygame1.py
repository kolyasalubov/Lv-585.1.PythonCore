import pygame
#Здається я неправильно зробив

FPS = 60



BLACK = (255, 255, 255)
BLUE = (20, 20, 20)

pygame.init()
screen = pygame.display.set_mode((1200, 800))

pygame.display.set_caption("My first game")

clock = pygame.time.Clock()

pygame.display.update()

background_position = [0, 0]

player_image = pygame.image.load(r"/Users/ivanmintenko/Desktop/pln.png").convert()

player_image.set_colorkey(BLACK)




done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]

    screen.fill((BLACK))

    screen.blit(player_image, [x, y])

    pygame.display.flip()

    clock.tick(60)

pygame.quit()