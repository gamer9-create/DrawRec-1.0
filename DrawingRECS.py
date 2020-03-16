import pygame
pygame.init()
win = pygame.display.set_mode((1000, 1000))

pygame.display.set_caption("Fight shooters")
width = 40
height = 40
run = True
while run:
    x = 0
    y = 0
    print(x)
    print(y)
   

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("hgvg")
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
            (x, y) = pygame.mouse.get_pos()
        
        
            
            print("You clicked a rec!")
    Keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()
    if Keys[pygame.K_b]:
        width = width + 4
        height = height + 4
    if Keys[pygame.K_s]:
        width = width - 4
        height = height - 4
    if Keys[pygame.K_m]:
        (x, y) = pygame.mouse.get_pos()
        pass
    play_button = pygame.draw.rect(win, (221, 35, 0), (x, y, width, height))
    pygame.display.update()
pygame.quit()
