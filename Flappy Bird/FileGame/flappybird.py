import pygame, sys
#Hàm vẽ sàn
def draw_floor():
    screen.blit(floor,(floor_x_pos, 600))
    screen.blit(floor,(floor_x_pos + 432, 600))

pygame.init()
#Tạo màn hình
screen = pygame.display.set_mode((432,768))
clock = pygame.time.Clock()
gravity = 0.25
bird_move = 0
#Chèn background 
bg = pygame.image.load('Flappy Bird/FileGame/assets/background-night.png').convert()
bg = pygame.transform.scale2x(bg)
#Chèn sàn 
floor = pygame.image.load('Flappy Bird/FileGame/assets/floor.png').convert()
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0
#Chim
bird = pygame.image.load('Flappy Bird/FileGame/assets/yellowbird-midflap.png').convert()
bird = pygame.transform.scale2x(bird)
bird_rect = bird.get_rect(center = (200, 384))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_move = 0
                bird_move = -11  
    screen.blit(bg,(0, 0))
    bird_move += gravity
    bird_rect.centery += bird_move
    screen.blit(bird, bird_rect)
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -432:
        floor_x_pos = 0
    pygame.display.update()
    clock.tick(120)