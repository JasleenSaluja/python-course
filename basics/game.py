import pygame
from sys import exit
def display_score():
    current_time=int(pygame.time.get_ticks()/1000)-start_time
    score_surf=test_font.render(f'score:{current_time}',False,(64,64,64))
    score_rect=score_surf.get_rect(center=(400,50))
    screen.blit(score_surf,score_rect)
    return current_time
    


pygame.init()
screen = pygame.display.set_mode((800,400)) #to create a display screen
pygame.display.set_caption('Runner') #To give a name to the display window
clock =pygame.time.Clock() 
test_font = pygame.font.Font('font/Pixeltype.ttf',50) #(font_type,font_size1)
game_active=False
start_time=0
score=0

sky_surface = pygame.image.load('graphics/sky.png').convert() #create a regular surface with an img
ground_surface = pygame.image.load('graphics/ground.png').convert()

#score_surface =test_font.render('My game',False,(64,64,64))  #(text,AA,color) AA-Anti_Aliasing
#score_rect = score_surface.get_rect(center=(400,50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()     
snail_rect = snail_surface.get_rect(midbottom=(600,300))

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80,300))
player_gravity=0 

#into screen
player_stand=pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center=(400,200))

game_name=test_font.render('Pixel Runner',False,(111,196,169))
game_name_rect=game_name.get_rect(center=(400,80))

game_msg=test_font.render('Press space to run',False,(111,196,169))
game_msg_rect=game_msg.get_rect(center=(400,320))

while True:  #to hold the display window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  #to exit the infinite loop or display window
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom>=300:
                    player_gravity = -20 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom>=300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
                game_active=True
                snail_rect.left=800
                start_time=int(pygame.time.get_ticks()/1000)


    if game_active:
        screen.blit(sky_surface,(0,0)) #put one surfecon another
        screen.blit(ground_surface,(0,300))
        #pygame.draw.rect(screen,'#c0e8ec',score_rect)
        #pygame.draw.rect(screen,'#c0e8ec',score_rect,10)
        #screen.blit(score_surface,score_rect)
        score=display_score()

        snail_rect.x -=4
        if snail_rect.right<=0:
            snail_rect.left=800
        screen.blit(snail_surface,snail_rect)

        #player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom>=300:
            player_rect.bottom=300
        screen.blit(player_surface,player_rect)

        #collisions
        if snail_rect.colliderect(player_rect):
            game_active=False
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)

        score_msg=test_font.render(f'Your Score:{score}',False,(11,196,169))
        score_msg_rect=score_msg.get_rect(center=(400,330))
        screen.blit(game_name,game_name_rect)
        if score==0:
            screen.blit(game_msg,game_msg_rect)   
        else:
            screen.blit(score_msg,score_msg_rect)             


    pygame.display.update() #To update the display window
    clock.tick(60)  #To diplay 60 img per second
