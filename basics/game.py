import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400)) #to create a display screen
pygame.display.set_caption('Runner') #To give a name to the display window
clock =pygame.time.Clock() 
test_font = pygame.font.Font('font/Pixeltype.ttf',50) #(font_type,font_size1)


sky_surface = pygame.image.load('graphics/sky.png').convert() #create a regular surface with an img
ground_surface = pygame.image.load('graphics/ground.png').convert()

score_surface =test_font.render('My game',False,'Black')  #(text,AA,color) AA-Anti_Aliasing
score_rect = score_surface.get_rect(center=(400,50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(600,300))

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80,300))

while True:  #to hold the display window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  #to exit the infinite loop or display window
        #if event.type ==pygame.MOUSEMOTION:
           #if player_rect.collidepoint(event.pos):
            #   print('collision') 

    screen.blit(sky_surface,(0,0)) #put one surfecon another
    screen.blit(ground_surface,(0,300))
    pygame.draw.rect(screen,'Pink',score_rect)
    pygame.draw.rect(screen,'Pink',score_rect,10)
    screen.blit(score_surface,score_rect)

    snail_rect.x -=4
    if snail_rect.right<=0:
        snail_rect.left=800
    screen.blit(snail_surface,snail_rect)
    screen.blit(player_surface,player_rect)

    #if player_rect.colliderect(snail_rect):
    #    print('collision ')

    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint(mouse_pos):
        print(pygame.mouse.get_pressed())



    pygame.display.update() #To update the display window
    clock.tick(60)  #To diplay 60 img per second
