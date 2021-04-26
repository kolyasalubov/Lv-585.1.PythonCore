import pygame


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (153, 204, 255)

COORD_X=50
COORD_Y=50
player_image=40
DELTA_STEP=5


pygame.init()
 

screen = pygame.display.set_mode([1000, 800], pygame.RESIZABLE)
 

pygame.display.set_caption('Fly')
 
clock = pygame.time.Clock()


pygame.display.update()


player_image = pygame.image.load("/Users/yelizavetamaistruk/Desktop/image/plane.png").convert_alpha()


player_image.set_colorkey(WHITE)


pygame.display.update()

done = False
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True            
 
    keys=pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and COORD_X>DELTA_STEP:
        COORD_X=(COORD_X-DELTA_STEP) == screen
    if keys[pygame.K_RIGHT]:
        COORD_X=(COORD_X+DELTA_STEP) == screen
    if keys[pygame.K_UP]:
        COORD_Y=(COORD_Y-DELTA_STEP) == screen
    if keys[pygame.K_DOWN]:
        COORD_Y=(COORD_Y+DELTA_STEP) == screen


    screen.fill((BLUE)) 



    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]
 

    screen.blit(player_image,[x, y])
 

    pygame.display.flip()
 
    clock.tick(60)


pygame.quit()
