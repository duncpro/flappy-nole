import sys, pygame

pygame.init()

# Screen Dimensions
screen_width = 576
screen_height = 1024
screen_size = (screen_width, screen_height)

speed = [2, 2]
black = 0, 0, 0

clock=pygame.time.Clock() #g

gravity = .20
ballposition = 0

screen = pygame.display.set_mode(screen_size)

#ball = pygame.image.load("intro_ball.gif")
tempBackgrd= pygame.image.load("WestcottIMG.xcf")

ball = pygame.image.load("logocropped2.png") #ball=logo 300by306 pixels
ballrect = ball.get_rect(center = (screen_width / 2, screen_height / 2))   # places ball in middle of screen...based on current size (576, 1024)

# ground = pygame.

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # when space bar is pressed down
                ballposition = -10

    #screen.fill(black)
    screen.blit(tempBackgrd, (0, 0)) #set temp background
    ballposition += gravity
    ballrect.centery += ballposition    # moves ball downward
    screen.blit(ball, ballrect)
#     pygame.display.flip()

    pygame.display.update()
    clock.tick(120) #limits to 120
