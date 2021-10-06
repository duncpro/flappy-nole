import sys, pygame
pygame.init()

size = width, height = 576, 1024
clock=pygame.time.Clock() #g

speed = [2, 2]
black = 0, 0, 0

gravity = .20
ballposition = 0

screen = pygame.display.set_mode(size)

#ball = pygame.image.load("intro_ball.gif")
tempBackgrd= pygame.image.load("WestcottIMG.xcf")

ball = pygame.image.load("logocropped2.png") #ball=logo 300by306 pixels
ballrect = ball.get_rect(center = (288, 512))   # places ball in middle of screen...based on current size (576, 1024)

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

    #screen.fill(black)
    screen.blit(tempBackgrd, (0, 0)) #set temp background
    ballposition += gravity
    ballrect.centery += ballposition    # moves ball downward
    screen.blit(ball, ballrect)
#     pygame.display.flip()

    pygame.display.update()
    clock.tick(120) #limits to 120
