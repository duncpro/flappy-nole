import sys, pygame
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

gravity = .20
ballposition = 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect(center = (160, 120))   # places ball in middle of screen...based on current size (320, 240)

# ground = pygame.

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # when space bar is pressed down
                ballposition = -10

#     ballrect = ballrect.move(speed)
#     if ballrect.left < 0 or ballrect.right > width:
#         speed[0] = -speed[0]
#     if ballrect.top < 0 or ballrect.bottom > height:
#         speed[1] = -speed[1]

    screen.fill(black)
    ballposition += gravity
    ballrect.centery += ballposition    # moves ball downward
    screen.blit(ball, ballrect)
#     pygame.display.flip()

    pygame.display.update()
