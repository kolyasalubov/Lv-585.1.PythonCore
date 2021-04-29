import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()

screen = pygame.display.set_mode([800, 600])

pygame.display.set_caption('Fly')

clock = pygame.time.Clock()

pygame.display.update()

background_position = [0, 0]

player_image = pygame.image.load(r"D:\ptashka.png").convert()

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