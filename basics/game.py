import pygame
from sys import exit
from random import randint


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk_1,player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()

        self.image=self.player_walk[self.player_index]
        self.rect=self.image.get_rect(midbottom=(200,300))
        self.gravity=0
    
    def player_input(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom>=300:
            self.gravity=-20
    
    def apply_gravity(self):
        self.gravity+=1
        self.rect.y+=self.gravity
        if self.rect.bottom>=300:
            self.rect.bottom=300
    
    def animation_state(self):
        if self.rect.bottom<300:
            self.image=self.player_jump
        else:
            self.player_index+=0.1
            if self.player_index >= len(self.player_walk):self.player_index=0
            self.image=self.player_walk[int(self.player_index)]


    def update(self):
        self.player_input()
        self.apply_gravity()



def display_score():
    current_time=int(pygame.time.get_ticks()/1000)-start_time
    score_surf=test_font.render(f'score:{current_time}',False,(64,64,64))
    score_rect=score_surf.get_rect(center=(400,50))
    screen.blit(score_surf,score_rect)
    return current_time
  
def player_animation():
    global player_surf,player_index

    if player_rect.bottom<300:
        player_surf=player_jump
    else:
        player_index+=0.1
        if player_index>=len(player_walk):player_index=0
        player_surf =player_walk[int(player_index)]


def obstacle_movement(obstacle_list): 
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -=5 

            if obstacle_rect.bottom ==300:
                screen.blit(snail_surf,obstacle_rect)
            else:
                screen.blit(fly_surf,obstacle_rect)

        obstacle_list=[obstacle for obstacle in obstacle_list if obstacle.x>-100]

        return obstacle_list #for global scope
    else:
        return[]
    
def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

pygame.init()
screen = pygame.display.set_mode((800,400)) #to create a display screen
pygame.display.set_caption('Runner') #To give a name to the display window
clock =pygame.time.Clock() 
test_font = pygame.font.Font('font/Pixeltype.ttf',50) #(font_type,font_size1)
game_active=False
start_time=0
score=0

player=pygame.sprite.GroupSingle()
player.add(Player())

sky_surface = pygame.image.load('graphics/sky.png').convert() #create a regular surface with an img
ground_surface = pygame.image.load('graphics/ground.png').convert()

#score_surface =test_font.render('My game',False,(64,64,64))  #(text,AA,color) AA-Anti_Aliasing
#score_rect = score_surface.get_rect(center=(400,50))

#snail
snail_frame_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha() 
snail_frame_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()   
snail_frames = [snail_frame_1,snail_frame_2]
snail_frame_index=0
snail_surf = snail_frames[snail_frame_index] 

#fly
fly_frame_1=pygame.image.load('graphics/fly/Fly1.png').convert_alpha()
fly_frame_2=pygame.image.load('graphics/fly/Fly2.png').convert_alpha()
fly_frames = [fly_frame_1,fly_frame_2]
fly_frame_index=0
fly_surf=fly_frames[fly_frame_index]

obstacle_rect_list=[]

player_walk_1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1,player_walk_2]
player_index = 0
player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()

player_surf =player_walk[player_index]
player_rect = player_surf.get_rect(midbottom=(80,300))
player_gravity=0 

#into screen
player_stand=pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center=(400,200))

game_name=test_font.render('Pixel Runner',False,(111,196,169))
game_name_rect=game_name.get_rect(center=(400,80))

game_msg=test_font.render('Press space to run',False,(111,196,169))
game_msg_rect=game_msg.get_rect(center=(400,320))

#timer
obstacle_timer = pygame.USEREVENT +1
pygame.time.set_timer(obstacle_timer,1500)

snail_animation_timer=pygame.USEREVENT+2
pygame.time.set_timer(snail_animation_timer,500)

fly_animation_timer=pygame.USEREVENT+3
pygame.time.set_timer(fly_animation_timer,200)


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
                start_time=int(pygame.time.get_ticks()/1000)
        if game_active:
            if event.type==obstacle_timer:
                if randint(0,2):
                    obstacle_rect_list.append(snail_surf.get_rect(midbottom=(randint(900,1100),300)))
                else:
                    obstacle_rect_list.append(fly_surf.get_rect(midbottom=(randint(900,1100),210)))

            if event.type ==snail_animation_timer:
                if snail_frame_index ==0:snail_frame_index=1
                else:snail_frame_index=0
                snail_surf=snail_frames[snail_frame_index]


            if event.type ==fly_animation_timer:
                if fly_frame_index ==0:fly_frame_index=1
                else:fly_frame_index=0
                fly_surf=fly_frames[fly_frame_index]

    if game_active:
        screen.blit(sky_surface,(0,0)) #put one surfecon another
        screen.blit(ground_surface,(0,300))
        #pygame.draw.rect(screen,'#c0e8ec',score_rect)
        #pygame.draw.rect(screen,'#c0e8ec',score_rect,10)
        #screen.blit(score_surface,score_rect)
        score=display_score()

        #snail_rect.x -=4
        #if snail_rect.right<=0:
        #    snail_rect.left=800
        #screen.blit(snail_surface,snail_rect)

        #player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom>=300:
            player_rect.bottom=300
        player_animation()
        screen.blit(player_surf,player_rect)
        player.draw(screen)
        player.update()

        #obstacle movement
        obstacle_rect_list=obstacle_movement(obstacle_rect_list)

        #collsions
        game_active =collisions(player_rect,obstacle_rect_list)

    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom=(80,300)
        player_gravity=0

        score_msg=test_font.render(f'Your Score:{score}',False,(11,196,169))
        score_msg_rect=score_msg.get_rect(center=(400,330))
        screen.blit(game_name,game_name_rect)
        if score==0:
            screen.blit(game_msg,game_msg_rect)   
        else:
            screen.blit(score_msg,score_msg_rect)             


    pygame.display.update() #To update the display window
    clock.tick(60)  #To diplay 60 img per second
