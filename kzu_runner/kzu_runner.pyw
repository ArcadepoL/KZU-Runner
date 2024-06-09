import pygame
import time
from sys import exit
from random import randint, choice
import datetime
import os
from os.path import abspath, dirname
os.chdir(dirname(abspath(__file__)))

class Background(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == 'ground':
            self.image = pygame.image.load('graphics/ground.png').convert_alpha()
            self.rect = pygame.Rect(0, 810, 1, 1)
            self.type = 'ground'
        elif type == 'sky':
            self.image = pygame.image.load('graphics/sky.png').convert_alpha()
            self.rect = pygame.Rect(0, 0, 1, 1)
            self.type = 'sky'
    def update(self):
        if self.rect.top == 810:
            self.rect.x -= (player.sprite.speed + 2)*dt
        else:
            self.rect.x -= (player.sprite.speed)*dt
        if self.rect.x <= -1920:
            self.rect.x += 1920
            if self.rect.top == 810:pygame.event.post(pygame.event.Event(obstacle_timer))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk1 = pygame.image.load('graphics/player/player_walk1.png').convert_alpha()
        player_walk2 = pygame.image.load('graphics/player/player_walk2.png').convert_alpha()
        player_walk3 = pygame.image.load('graphics/player/player_walk3.png').convert_alpha()
        player_walk4 = pygame.image.load('graphics/player/player_walk4.png').convert_alpha()
        self.walk = [player_walk1, player_walk2, player_walk3, player_walk4]
        self.index = 0
        self.jump = pygame.image.load('graphics/player/player_jump.png').convert_alpha()
        self.scale = 0.3
        self.gravity = 0
        self.speed = 10
        self.stand_speed = 10
        self.hit_ability_6er = False
        self.hit = False

        self.jump_sound = pygame.mixer.Sound('audio/jump.wav')
        self.jump_sound.set_volume(0.3)

        self.image = pygame.transform.rotozoom(self.walk[self.index],0,self.scale)
        self.rect = self.image.get_rect(midbottom= (80, 300))
          
   
    def player_input(self):
        if keys[pygame.K_a] and game_active:
            self.speed -= 4
        if keys[pygame.K_d] == True and game_active:
            self.speed += 4
        if keys[pygame.K_SPACE] == True and self.rect.bottom >=810:
            self.gravity = -20
            self.jump_sound.play()
        if keys[pygame.K_w] == True and self.hit == False:
            self.hit = True
        else: self.hit = False

    def apply_gravity(self):
        self.gravity += 0.7*dt
        self.rect.y += self.gravity
        if self.rect.bottom >= 810:self.rect.bottom = 810

    def animation_state(self):
        if self.rect.bottom < 810:
            self.image = pygame.transform.rotozoom(self.jump,0,1.1)
        else:
            if self.speed == self.stand_speed:
                self.index += 0.2*dt
            elif self.speed < self.stand_speed:
                self.index += 0.1*dt
            else:
                self.index += 0.3*dt
            if self.index >= len(self.walk): self.index = 0
            self.image = pygame.transform.rotozoom(self.walk[int(self.index)],0,self.scale)

    def update(self):
        self.speed = self.stand_speed
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == 'table':
            table1 = pygame.image.load('graphics/table/table1.png').convert_alpha()
            table2 = pygame.image.load('graphics/table/table2.png').convert_alpha()
            table3 = pygame.image.load('graphics/table/table3.png').convert_alpha()
            table4 = pygame.image.load('graphics/table/table4.png').convert_alpha()
            self.frames = [table1, table2, table3, table4]
            self.index = 0
            self.scale = 0.3
            self.speed = 0
            self.y_pos = 810
            self.type = type
        elif type == 'sign':
            sign1 = pygame.image.load('graphics/sign/sign1.png').convert_alpha()
            sign2 = pygame.image.load('graphics/sign/sign2.png').convert_alpha()
            sign3 = pygame.image.load('graphics/sign/sign3.png').convert_alpha()
            sign4 = pygame.image.load('graphics/sign/sign4.png').convert_alpha()
            self.frames = [sign1, sign2, sign3, sign4]
            self.scale = 0.4
            self.speed = 0
            self.y_pos = 250
            self.type = type
        elif type == 'teacher':
            teacher1 = pygame.image.load('graphics/teacher/teacher1.png').convert_alpha()
            teacher2 = pygame.image.load('graphics/teacher/teacher2.png').convert_alpha()
            teacher3 = pygame.image.load('graphics/teacher/teacher3.png').convert_alpha()
            teacher4 = pygame.image.load('graphics/teacher/teacher4.png').convert_alpha()
            self.frames = [teacher1, teacher2, teacher3, teacher4]
            self.scale = 4.5
            self.speed = 2
            self.y_pos = 810
            self.type = type

        else:
            teacher1 = pygame.transform.rotozoom(pygame.image.load('graphics/sportsteacher/sportsteacher1.png').convert_alpha(), 0, 4.4)
            teacher2 = pygame.transform.rotozoom(pygame.image.load('graphics/sportsteacher/sportsteacher2.png').convert_alpha(), 0, 4.4)
            teacher3 = pygame.transform.rotozoom(pygame.image.load('graphics/sportsteacher/sportsteacher3.png').convert_alpha(), 0, 4.4)
            teacher4 = pygame.transform.rotozoom(pygame.image.load('graphics/sportsteacher/sportsteacher4.png').convert_alpha(), 0, 4.4)
            self.frames = [teacher1, teacher2, teacher3, teacher4]

            attention1 = pygame.transform.rotozoom(pygame.image.load('graphics/sportsteacher/attention1.png').convert_alpha(), 0, 4.4)
            attention2 = pygame.transform.rotozoom(pygame.image.load('graphics/sportsteacher/attention2.png').convert_alpha(), 0, 4.4)
            attention3 = pygame.transform.rotozoom(pygame.image.load('graphics/sportsteacher/attention3.png').convert_alpha(), 0, 4.4)
            attention4 = pygame.transform.rotozoom(pygame.image.load('graphics/sportsteacher/attention4.png').convert_alpha(), 0, 4.4)
            self.frames_attention = [attention1, attention2, attention3, attention4]

            self.dunk_frames = []
            for x in range(1, 18):
                self.dunk_frames.append(pygame.image.load('graphics/sportsteacher/dunk'+str(x)+'.png').convert_alpha())
            self.gravity = 0
            self.dunk = False
            self.dunked = False
            self.dunk_coordinates = randint(220+int(player.sprite.stand_speed), 1793+int(player.sprite.stand_speed))
            self.dunk_index = 0
            self.scale = 0.5
            self.speed = 3
            self.y_pos = 820
            self.type = type

        self.animation_index = 0
        self.image = pygame.transform.rotozoom(self.frames[self.animation_index],0, self.scale)
        self.rect = self.image.get_rect(midbottom = (randint(2000, 2300), self.y_pos))
    
    def animation_state(self):
        self.animation_index += 0.1*dt
        if self.type == 'sportsteacher' and self.rect.x < self.dunk_coordinates+400 and not self.dunked:
            if not self.dunk:
                if self.animation_index >= len(self.frames): self.animation_index = 0
                self.image =  pygame.transform.rotozoom(self.frames_attention[int(self.animation_index)],0, 0.2)
        else:        
            if self.animation_index >= len(self.frames): self.animation_index = 0
            self.image =  pygame.transform.rotozoom(self.frames[int(self.animation_index)],0, self.scale)

    def dunk_animation(self):
        self.dunk_index += 0.1*dt
        self.image =  pygame.transform.rotozoom(self.dunk_frames[int(self.dunk_index)],0, 4.5)


    def apply_gravity(self):
        self.gravity += 0.7*dt
        self.rect.y += self.gravity
        if self.rect.bottom >= 820:
            self.dunk = False
            self.dunked = True

    def teacher_hit(self):
        if player.sprite.hit_ability_6er and player.sprite.hit and player.sprite.rect.bottom == 810:
            if self.type == 'teacher' and self.rect.left > player.sprite.rect.right + 10 and self.rect.left < player.sprite.rect.right + 800:
                destroy_teacher_animation(self)

    def check_for_dunk(self):
        if self.dunk_coordinates > self.rect.x and not self.dunk and not self.dunked:
            self.dunk = True
            self.gravity = -25

    def update(self):
        self.animation_state()
        self.teacher_hit()
        if self.type == 'sportsteacher':
            self.check_for_dunk()
            if self.dunk:
                self.dunk_animation()
                self.apply_gravity()
        self.rect.x -= (player.sprite.speed + self.speed + 2)*dt
        self.destroy()

    def destroy(self):
        if self.rect.x < -400:
            self.kill()

class friendly_objects(pygame.sprite.Sprite):
    def __init__(self, type, obj_rect):
        super().__init__()
        if type == 'dead_teacher':
            self.image =  pygame.transform.rotozoom(pygame.image.load('graphics/animations/teacher_destroy/dead_teacher.png').convert_alpha(), 0, 4.6)
            self.rect = obj_rect
            self.scale = 0.3
            self.speed = 0
    def destroy(self):
        if self.rect.x < -500:
            self.kill()    
    def update(self):
        self.rect.x -= (player.sprite.speed + self.speed + 2)*dt
        self.destroy()

class items(pygame.sprite.Sprite):
    icons = [[], [], []]
    sd = 0
    su = 0
    def __init__(self, type):
        super().__init__()
        if type == '6er':
            self.image = pygame.image.load('graphics/icons/6er_item.png').convert_alpha()
            self.animation_index = 0
            self.icon_index = 0
            self.type = type

        elif type == 'speedup':
            self.image = pygame.image.load('graphics/icons/speedup_item.png').convert_alpha()
            self.animation_index = 0
            self.icon_index = 1
            self.type = type

        else:
            self.image = pygame.image.load('graphics/icons/slowdown_item.png').convert_alpha()
            self.animation_index = 0
            self.icon_index = 2
            self.type = type

        self.rect = self.image.get_rect(midbottom=(randint(2000, 3500), randint(250, 810)))
    
    def check_collision_with_player(self):
        if self.rect.colliderect(player.sprite.rect):
            self.add_item_to_list()

    def add_item_to_list(self):
        if len(items.icons[self.icon_index]) < 3:
            item_pickup.play()
            if self.type == 'slowdown':
                player.sprite.stand_speed -= 5
                items.sd = time.time()
            elif self.type == 'speedup':
                player.sprite.stand_speed += 5
                items.su = time.time()
            items.icons[self.icon_index].append(self.icon_index)
            self.kill()
            
    def move(self):
        self.rect.x -= (player.sprite.speed + 2)*dt

    def destroy(self):
        if self.rect.x < -250:
            self.kill()

    def animation(self):
        self.animation_index += 1
        if self.animation_index == 60:
            self.rect.y += 10
            self.animation_index = 0
        elif self.animation_index == 30:
            self.rect.y -= 10
    
    def update(self):
        self.animation()
        self.move()
        self.destroy()
        self.check_collision_with_player()

def render_icons():
    x_pos = 70
    y_pos = 70
    for type in items.icons:
        for icon in type:
            if icon == 0:
                screen.blit(icon_6er, icon_6er.get_rect(center=(x_pos, y_pos)))
                player.sprite.hit_ability_6er = True
                x_pos += 130
            elif icon == 1:
                screen.blit(icon_speedup, icon_speedup.get_rect(center=(x_pos, y_pos)))
            else:
                screen.blit(icon_slowdown, icon_slowdown.get_rect(center=(x_pos, y_pos)))
    if len(items.icons[0]) == 0:
        player.sprite.hit_ability_6er = False
    ctime = time.time()
    if len(items.icons[1]) != 0:
        if ctime - items.su > 5:
            items.icons[1].pop()
            player.sprite.stand_speed -= 5
    elif len(items.icons[2]) != 0:
        if ctime - items.sd > 5:
            player.sprite.stand_speed += 5
            items.icons[2].pop()

def display_score(color):
    score_surface = test_font.render(f'Score: {int(score//420)}',False, color)
    score_rect = score_surface.get_rect(center=(960, 100))
    screen.blit(score_surface, score_rect)

def destroy_teacher_animation(teacher):

    global last_time, score

    player1 = pygame.image.load('graphics/animations/teacher_destroy/6er1.png').convert_alpha()
    player2 = pygame.image.load('graphics/animations/teacher_destroy/6er2.png').convert_alpha()
    player3 = pygame.image.load('graphics/animations/teacher_destroy/6er3.png').convert_alpha()
    player4 = pygame.image.load('graphics/animations/teacher_destroy/6er4.png').convert_alpha()
    player5 = pygame.image.load('graphics/animations/teacher_destroy/6er5.png').convert_alpha()
    player6 = pygame.image.load('graphics/animations/teacher_destroy/6er6.png').convert_alpha()
    player7 = pygame.image.load('graphics/animations/teacher_destroy/6er7.png').convert_alpha()
    player8 = pygame.image.load('graphics/animations/teacher_destroy/6er8.png').convert_alpha()
    player9 = pygame.image.load('graphics/animations/teacher_destroy/6er9.png').convert_alpha()
    player10 = pygame.image.load('graphics/animations/teacher_destroy/6er10.png').convert_alpha()

    shock1 = pygame.image.load('graphics/animations/teacher_destroy/6er_shock1.png').convert_alpha()
    shock2 = pygame.image.load('graphics/animations/teacher_destroy/6er_shock2.png').convert_alpha()
    shock3 = pygame.image.load('graphics/animations/teacher_destroy/6er_shock3.png').convert_alpha()
    shock4 = pygame.image.load('graphics/animations/teacher_destroy/6er_shock4.png').convert_alpha()
    shock5 = pygame.image.load('graphics/animations/teacher_destroy/6er_shock5.png').convert_alpha()

    destroy1= pygame.image.load('graphics/animations/teacher_destroy/dying1.png').convert_alpha()
    destroy2= pygame.image.load('graphics/animations/teacher_destroy/dying2.png').convert_alpha()
    destroy3= pygame.image.load('graphics/animations/teacher_destroy/dying3.png').convert_alpha()
    destroy4= pygame.image.load('graphics/animations/teacher_destroy/dying4.png').convert_alpha()
    destroy5= pygame.image.load('graphics/animations/teacher_destroy/dying5.png').convert_alpha()
    destroy6= pygame.image.load('graphics/animations/teacher_destroy/dying6.png').convert_alpha()
    destroy7= pygame.image.load('graphics/animations/teacher_destroy/dying7.png').convert_alpha()
    destroy8= pygame.image.load('graphics/animations/teacher_destroy/dying8.png').convert_alpha()
    destroy9= pygame.image.load('graphics/animations/teacher_destroy/dying9.png').convert_alpha()
    destroy10= pygame.image.load('graphics/animations/teacher_destroy/dying10.png').convert_alpha()
    destroy11= pygame.image.load('graphics/animations/teacher_destroy/dying11.png').convert_alpha()
    destroy12= pygame.image.load('graphics/animations/teacher_destroy/dying12.png').convert_alpha()

    destroy_frames = [destroy1, destroy2, destroy3, destroy4, destroy5, destroy6, destroy7, destroy8, destroy9, destroy10, destroy11, destroy12]
    destroy1_rect = destroy_frames[0].get_rect(center=(teacher.rect.x+70, teacher.rect.y))
    destroy_index = 0

    index = 0

    player_frames = [player1, player2, player3, player4, player5, player6, player7, player8, player9, player10]
    shock_frames = [shock1, shock2, shock3, shock4, shock5]


    shock_surface = shock_frames[index]
    shock_rect = shock_surface.get_rect(center=(player.sprite.rect.centerx + 140, player.sprite.rect.centery-10))

    player_surface = player_frames[index]
    player_rect = player_surface.get_rect(midbottom= (80, 810))

    shock_list = []
    shock_list.append(pygame.Rect.copy(shock_rect))

    sound_play = False


    while not shock_list[0].colliderect(destroy1_rect):
        if index == 7:
            if sound_play == False:
                boom_6er.play()
                sound_play = True
            background.draw(screen)
            enemy_group.draw(screen)
            screen.blit(player_frames[6], player_rect)
            if shock_list[len(shock_list)-1].x - shock_rect.x > 130:
                shock_list.append(pygame.Rect.copy(shock_rect))
            for x in range(0, len(shock_list)):
                if shock_list[x].left - shock_rect.right <= 30:
                    screen.blit(shock_frames[0], shock_rect)
                    shock_list[x].x += 2
                elif shock_list[x].left - shock_rect.right <= 60 :
                    screen.blit(shock_frames[1], shock_list[x])
                    shock_list[x].x += 2
                elif shock_list[x].left - shock_rect.right <= 90:
                    screen.blit(shock_frames[2], shock_list[x])
                    shock_list[x].x += 2
                elif shock_list[x].left - shock_rect.right <= 120:
                    screen.blit(shock_frames[3], shock_list[x])
                    shock_list[x].x += 2
                else:
                    screen.blit(shock_frames[4], shock_list[x])
                    shock_list[x].x += 2
            resized_screen = pygame.transform.scale(screen, (infoObject.current_w, infoObject.current_h))
            screen.fill('black')
            window.blit(resized_screen, (0, 0))
            pygame.display.update()
        
        else:
            background.draw(screen)
            enemy_group.draw(screen)
            screen.blit(player_frames[index], player_rect)
            pygame.time.wait(100)
            resized_screen = pygame.transform.scale(screen, (infoObject.current_w, infoObject.current_h))
            screen.fill('black')
            window.blit(resized_screen, (0, 0))
            pygame.display.update()
            index += 1
    #death Physiklehrer
    else:
        teacher.kill()
        shock_list.pop(0)
        for x in range(0, 12):
            background.draw(screen)
            enemy_group.draw(screen)
            friendly_group.draw(screen)
            screen.blit(player_frames[6], player_rect)
            for x in range(0, len(shock_list)):
                if shock_list[x].left - shock_rect.right <= 30:
                    screen.blit(shock_frames[0], shock_rect)
                    shock_list[x].x += 10
                elif shock_list[x].left - shock_rect.right <= 60 :
                    screen.blit(shock_frames[1], shock_list[x])
                    shock_list[x].x += 10
                elif shock_list[x].left - shock_rect.right <= 90:
                    screen.blit(shock_frames[2], shock_list[x])
                    shock_list[x].x += 10
                elif shock_list[x].left - shock_rect.right <= 120:
                    screen.blit(shock_frames[3], shock_list[x])
                    shock_list[x].x += 10
                else:
                    screen.blit(shock_frames[4], shock_list[x])
                    shock_list[x].x += 10
            screen.blit(pygame.transform.rotozoom(destroy_frames[destroy_index], 0, 4.6), destroy1_rect)
            resized_screen = pygame.transform.scale(screen, (infoObject.current_w, infoObject.current_h))
            screen.fill('black')
            window.blit(resized_screen, (0, 0))
            pygame.display.update()
            pygame.time.wait(100)
            destroy_index += 1
        friendly_group.add(friendly_objects('dead_teacher', destroy1_rect))
        for x in range(0, 21):
            score += 420
            score_sound.play()
            background.draw(screen)
            enemy_group.draw(screen)
            friendly_group.draw(screen)
            screen.blit(player_frames[6], player_rect)
            display_score('gold')
            pygame.time.wait(50)
            resized_screen = pygame.transform.scale(screen, (infoObject.current_w, infoObject.current_h))
            screen.fill('black')
            window.blit(resized_screen, (0, 0))
            pygame.display.update()

    #take 6er back
    for x in range (0,3):
        background.draw(screen)
        enemy_group.draw(screen)
        friendly_group.draw(screen)
        screen.blit(player_frames[index+x], player_rect)
        pygame.time.wait(100)
        resized_screen = pygame.transform.scale(screen, (infoObject.current_w, infoObject.current_h))
        screen.fill('black')
        window.blit(resized_screen, (0, 0))
        pygame.display.update()
    items.icons[0].pop()
    last_time = time.time()

def update_spawning():
    for event in pygame.event.get():
        if event.type == obstacle_timer:
            enemy_group.add(Enemy(choice(['table', 'table', 'table', 'table', 'sign', 'sign', 'sign',  'teacher', 'teacher', 'sportsteacher'])))
            if randint(0, 9) == 9:
                items_group.add(items(choice(['6er', 'speedup', 'slowdown'])))
            player.sprite.stand_speed += 0.3
            if player.sprite.stand_speed > 39:
                player.sprite.stand_speed = 39

def check_for_quit(keys):
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def game_over_display():

    global score, game_active, last_time
    bg_music.stop()
    bell_sound.stop()
    animation_index = 0.5
    animation_max = False
    personal_best, last_highscore = check_for_new_highscore(score//420)
    
    if personal_best: win_sound.play()

    welcome_message_surface1 = test_font.render('Willkommen beim KZU-Runner des Arcade-PoLs', False, 'orange')
    welcome_message_rect1 = welcome_message_surface1.get_rect(center=(960, 450))
    welcome_message_surface2 = test_font.render('SPACE --> Springen, D --> Schneller', False, 'red')
    welcome_message_rect2 = welcome_message_surface2.get_rect(center=(960, 600))
    welcome_message_surface3 = test_font.render('A --> langsamer, W --> Item einsetzen', False, 'red')
    welcome_message_rect3 = welcome_message_surface3.get_rect(center=(960, 700))

    game_over_text1_surf = test_font.render('KZU Runner', False, 'orange')
    game_over_text1_rect = game_over_text1_surf.get_rect(center=(960, 70))
    game_instructions1_surf = test_font.render('A: Neues Spiel', False, 'orange')
    game_instructions1_rect = game_instructions1_surf.get_rect(center = (960, 900))
    personal_best_surf = test_font.render('Personal Best!!!', False, 'orange')
    score_surf = test_font.render('Score: ' + str(int(score//420)), False, 'orange')
    score_rect = score_surf.get_rect(center=(960, 400))
    last_score_surf = test_font.render('Letzter Highscore:' + str(last_highscore), False, 'orange')
    last_score_rect = last_score_surf.get_rect(center=(960, 550))

    player_scaled = pygame.transform.rotozoom(player.sprite.walk[0],0,0.3)
    

    while game_active == False:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit() 
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit() 
                    exit()
                elif event.key == pygame.K_a:
                    bell_sound.play()
                    bg_music.play(loops=-1)
                    game_active = True
                    score = 0
                    last_time = time.time()
                    player.sprite.index = 0
                    player.sprite.stand_speed = 10

        screen.fill('black')
        if last_highscore > 0: screen.blit(last_score_surf, last_score_rect)
        elif score == 0 and last_highscore == 0:
            screen.blit(welcome_message_surface1, welcome_message_rect1)
            screen.blit(welcome_message_surface2, welcome_message_rect2)
            screen.blit(welcome_message_surface3, welcome_message_rect3)
        if score > 0: screen.blit(score_surf, score_rect)
        
        screen.blit(logo_surface, logo_rect)
        screen.blit(player_scaled, player_scaled.get_rect(center=(80, 220)))
        screen.blit(player_scaled, player_scaled.get_rect(center=(1840, 220)))
        screen.blit(game_over_text1_surf, game_over_text1_rect)
        screen.blit(game_instructions1_surf, game_instructions1_rect)
        screen.blit(name_surface, name_rect)
        if personal_best:
            screen.blit(pygame.transform.rotozoom(personal_best_surf, 330, animation_index), (1200, 190))
            if animation_max == False: animation_index += 0.02
            else: animation_index -= 0.02
            if animation_index > 1.2:
                animation_max = True
            elif animation_index <= 0.6:
                animation_max = False

        resized_screen = pygame.transform.scale(screen, (infoObject.current_w, infoObject.current_h))
        screen.fill('black')
        window.blit(resized_screen, (0, 0))
        pygame.display.update()

def check_for_new_highscore(score):
    score_file = open("data/highscore.dat", "r")
    highscore = int(score_file.read(-1))
    print(score, highscore)
    if score > highscore:
        score_file.close()
        score_file = open("data/highscore.dat", "w")
        score_file.write(str(int(score)))
        score_file.close()
        return True, highscore
    else:
        score_file.close()
        return False, highscore

def collisions():
    if pygame.sprite.spritecollide(player.sprite, enemy_group, False):
        enemy_group.empty()
        friendly_group.empty()
        items_group.empty()
        items.icons = [[], [], []]
        return False
    else: return True

pygame.init()
infoObject = pygame.display.Info()
print(infoObject.current_w, infoObject.current_h)
screen = pygame.display.set_mode((1920, 1080))
window = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
pygame.mouse.set_visible(False)
pygame.display.set_caption('Arcade PoL')
clock = pygame.time.Clock()

test_font = pygame.font.Font('font/pixeltype.ttf', 100)

background = pygame.sprite.Group()
background.add(Background('sky'))
background.add(Background('ground'))

player = pygame.sprite.GroupSingle()
player.add(Player())

player_death = pygame.mixer.Sound('audio/die.wav')
player_death.set_volume(900)
score_sound = pygame.mixer.Sound('audio/score.mp3')
score_sound.set_volume(0.5)
boom_6er = pygame.mixer.Sound('audio/6er_boom.mp3')
boom_6er.set_volume(0.6)
item_pickup = pygame.mixer.Sound('audio/item_pickup.mp3')
item_pickup.set_volume(0.7)
win_sound = pygame.mixer.Sound('audio/win.wav')
win_sound.set_volume(0.5)
bell_sound = pygame.mixer.Sound('audio/bell_sound.wav')
bell_sound.set_volume(1000)
bg_music = pygame.mixer.Sound('audio/music.mp3')
bg_music.set_volume(0.2)


enemy_group = pygame.sprite.Group()

friendly_group = pygame.sprite.Group()

items_group = pygame.sprite.Group()

icon_6er = pygame.transform.rotozoom(pygame.image.load('graphics/icons/6er_icon.png').convert_alpha(),0, 0.4)
icon_speedup = pygame.transform.rotozoom(pygame.image.load('graphics/icons/speedup_icon.png').convert_alpha(),0, 0.4)
icon_slowdown = pygame.transform.rotozoom(pygame.image.load('graphics/icons/slowdown_icon.png').convert_alpha(),0, 0.4)

logo_surface = pygame.image.load('graphics/pol/logo.png').convert_alpha()
logo_rect = logo_surface.get_rect(center=(1750, 900))

name_surface = pygame.transform.rotozoom(pygame.image.load('graphics/pol/name.png').convert_alpha(), 0, 0.5)
name_rect = name_surface.get_rect(center= (190, 950))


game_active = False
score = 0

#timers
obstacle_timer = pygame.USEREVENT + 1


while True:
    clock.tick(144)
    keys = pygame.key.get_pressed()
    check_for_quit(keys)

    if game_active:
        dt = time.time() - last_time
        last_time = time.time()
        dt *= 60

        score += player.sprite.speed*dt

        background.draw(screen)
        background.update()

        update_spawning()

        player.draw(screen)
        player.update()

        enemy_group.draw(screen)
        enemy_group.update()

        friendly_group.draw(screen)
        friendly_group.update()

        items_group.draw(screen)
        items_group.update()
        render_icons()

        display_score('black')

        game_active = collisions()

    else:
        game_over_display()
    
    resized_screen = pygame.transform.scale(screen, (infoObject.current_w, infoObject.current_h))
    screen.fill('black')
    window.blit(resized_screen, (0, 0))
    pygame.display.update()
