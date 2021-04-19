import pygame

pygame.init()
 
screen = pygame.display.set_mode((300,200))

screen.fill((255, 255, 255))

pygame.display.set_caption("Draw fonts")


f1 = pygame.font.Font(None, 36)
text1 = f1.render('Hello World!!!', 1, (255, 0, 0))
 
f2 = pygame.font.SysFont('serif', 48)
text2 = f2.render("Привіт Світ!!!", 0, (20, 110, 0))
 
screen.blit(text1, (10, 50))
screen.blit(text2, (10, 100))
 
pygame.display.update()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()