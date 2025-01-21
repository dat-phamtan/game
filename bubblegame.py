import pygame

pygame.init()
#Cửa sổ gamegame
WIDTH = 800
HEIGHT = 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

#Màu 
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)

#Biến kích thước
CIRCLE_CENTER = [WIDTH/2, HEIGHT/2]
CIRCLE_RADIUS = 150
BALL_RADIUS = 5
ball_pos = [WIDTH/2, HEIGHT/2 - 120]

#Biến khác
running = True
GRAVITY = 0.2 

#Vòng lặp 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    ball_pos[1] += GRAVITY
    window.fill(BLACK)
    pygame.draw.circle(window, ORANGE, CIRCLE_CENTER, CIRCLE_RADIUS, 3)# 3 là width(độ dày)
    pygame.draw.circle(window, RED, ball_pos, BALL_RADIUS)# không ghi số 3 vì quả bóng
    #phải được lấp đầy
     
    pygame.display.flip()
    clock.tick(60)
pygame.quit()