import pygame
import random
pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("game")

screenwidth = 500
x = 50
y = 450
width = 40
height = 50
vel = 5

run = True

#loop to run program
while run:
    #time delay so code doesnt excute too fast
    pygame.time.delay(100)

    #checking for if the player closes the window; if so then it will close the program
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            run = False
    
    #intraction with other square
    for x in range(5):
        ran1 = random.randint(0, 500)
        ran2 = random.randint(0, 500)
        pygame.draw.rect(win, (0,255,0)), (ran1, ran2))
    #movement and boundaries
    keys = pygame.key.get_pressed()

    
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if  keys[pygame.K_RIGHT] and x < screenwidth - width- vel:
        x += vel
    if keys[pygame.K_UP] and y > vel:
        y -= vel
    if keys[pygame.K_DOWN] and y < screenwidth - height - vel:
        y += vel

    
    #placing the player on the screen/updating player position
    win.fill((0,0,0))
    pygame.draw.rect(win, (255, 0, 0), (x,y,width,height))
    pygame.display.update()

pygame.quit()