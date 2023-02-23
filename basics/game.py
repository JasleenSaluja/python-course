import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400)) #to create a display screen
pygame.display.set_caption('Runner') #To give a name to the display window
clock =pygame.time.Clock() 
test_font = pygame.font.Font('font/Pixeltype.ttf',50) #(font_type,font_size1)


sky_surface = pygame.image.load('graphics/sky.png') #create a regular surface with an img
ground_surface = pygame.image.load('graphics/ground.png')
text_surface =test_font.render('My game',False,'Black')  #(text,AA,color) AA-Anti_Aliasing

snail_surface = pygame.image.load('graphics/snail/snail1.png')
snail_x_pos =600

while True:  #to hold the display window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  #to exit the infinite loop or display window

    screen.blit(sky_surface,(0,0)) #put one surfecon another
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))
    snail_x_pos -= 1 
    screen.blit(snail_surface,(snail_x_pos,250))


    pygame.display.update() #To update the display window
    clock.tick(60)  #To diplay 60 img per second
