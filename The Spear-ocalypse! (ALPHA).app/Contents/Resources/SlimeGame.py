def __main__():
    import pygame
    import os
    import random
    import time
    pygame.font.init()
    # Made by Caleb Greene
    # Welcome to the code! This was all created by me and as of now it is still in the early alpha testing.
    #  sets window
    WIDTH, HEIGHT = 500, 700
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Slime Dodgeball: The Spear-ocalypse!")
    #  starting slime cords
    Slime_X = 175
    Slime_Y = 500
    #  define colors
    SKY = (0, 220, 220)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    #  frame rate (don't recommend changing) standard 60
    FPS = 60
    #  defines images
    TITLE_IMAGE = pygame.image.load(os.path.join
                                    ('Assets', '/Users/calebgreene/Desktop/folder of folders/Sprites/Title Screen.png'))

    DEATH_IMAGE = pygame.image.load(os.path.join
                                    ('Assets', '/Users/calebgreene/Desktop/folder of folders/Sprites/DeadScreen.png'))

    SPEAR_IMAGE = pygame.image.load(os.path.join
                                    ('Assets', '/Users/calebgreene/Desktop/folder of folders/Sprites/SIMPLE SPEAR.png'))

    SPEAR_IMAGE = pygame.transform.scale(SPEAR_IMAGE, (30, 180))

    SUN_IMAGE = pygame.image.load(os.path.join
                                  ('Assets', '/Users/calebgreene/Desktop/folder of folders/Sprites/Simple Sun.png'))

    SUN_IMAGE = pygame.transform.scale(SUN_IMAGE, (200, 200))

    GROUND_IMAGE = pygame.image.load(os.path.join
                                     ('Assets', '/Users/calebgreene/Desktop/folder of folders/Sprites/Simple Ground.png'))

    GROUND_IMAGE = pygame.transform.scale(GROUND_IMAGE, (200, 200))

    SLIME_IMAGE = pygame.image.load(os.path.join
                                    ('Assets', '/Users/calebgreene/Desktop/folder of folders/Sprites/Simple Slime.gif'))
    SLIME_IMAGE = pygame.transform.scale(SLIME_IMAGE, (150, 150))

    seconds = 0

    previous = 0
    #  code tries to read the file. If the file is not found creates a new file and reads it again.
    try:
        with open('Score.txt', 'r') as read:
            for line in read.readlines():
                previous = int(round(float(line), 0))
    except FileNotFoundError:
        with open('Score.txt', 'w') as w:
            pass
        with open('Score.txt', 'r') as read:
            for line in read.readlines():
                previous = int(round(float(line), 0))


    def display_loss_message():
        WIN.blit(DEATH_IMAGE, (0, 0))
        pygame.display.update()
        time.sleep(3)


    def draw_window(spear, x):
        WIN.fill(SKY)
        WIN.blit(GROUND_IMAGE, (0, 600))
        WIN.blit(GROUND_IMAGE, (200, 600))
        WIN.blit(GROUND_IMAGE, (400, 600))
        WIN.blit(SUN_IMAGE, (-60, -60))
        WIN.blit(SPEAR_IMAGE, (x, spear))


    def main(x, y):
        t = 0
        spear_y = -200
        spear_x = random.randint(0, 500)
        draw_window(spear_y, spear_x)
        clock = pygame.time.Clock()
        run = True
        velocity = 10
        speed = 7
        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
            keys = pygame.key.get_pressed()
            while y < 501:
                y += 1
            if keys[pygame.K_d]:
                if x < 400:
                    x += speed
                else:
                    pass
            if keys[pygame.K_a]:
                if x > -40:
                    x -= speed
                else:
                    pass
            if keys[pygame.K_ESCAPE]:
                exit()
            WIN.fill(SKY)
            draw_window(spear_y, spear_x)
            WIN.blit(SLIME_IMAGE, (x, y))
            if spear_y < 425:
                spear_y += velocity
            else:
                spear_y = -400
                spear_x = random.randint(0, 500)
            rect = SPEAR_IMAGE.get_rect()
            rect.center = (spear_x, spear_y)
            collide = rect.colliderect(SLIME_IMAGE.get_rect())
            if collide:
                pass
            if spear_y >= 400 and x + 70 >= spear_x >= x:
                previous = 0

                with open('Score.txt', 'r') as read:
                    for line in read.readlines():
                        previous = float(line)
                if t > previous:
                    os.remove("Score.txt")
                    with open('Score.txt', 'w') as write:
                        write.write(str(t))
                display_loss_message()
                __main__()

            if spear_y >= 400 and x + 100 >= spear_x >= x:
                previous = 0

                with open('Score.txt', 'r') as read:
                    for line in read.readlines():
                        previous = float(line)
                if t > previous:
                    os.remove("Score.txt")
                    with open('Score.txt', 'w') as write:
                        write.write(str(t))
                display_loss_message()
                __main__()
            velocity += 0.005
            t += 0.0167
            speed += 0.005
            menu_font = pygame.font.Font(None, 60)
            text = menu_font.render(f"{int(round(t, 0))}", True, WHITE)
            text_rect = text.get_rect()
            text_rect.center = (WIDTH // 2, HEIGHT // 2 - 50)

            menu_text_surface = pygame.Surface((text_rect.width + 20, text_rect.height + 20))
            menu_text_surface.fill(GREEN)
            menu_text_surface.blit(text, (10, 10))
            pygame.draw.rect(menu_text_surface, BLACK, menu_text_surface.get_rect(), 5)
            menu_text_surface = pygame.transform.scale(menu_text_surface, (text_rect.width + 20, text_rect.height + 20))
            menu_text_surface = pygame.transform.scale(menu_text_surface, (text_rect.width + 20, text_rect.height + 20))

            menu_text_rect = menu_text_surface.get_rect()
            menu_text_rect.center = (WIDTH // 2, HEIGHT // 2 + 150)
            WIN.blit(text, (WIDTH // 2, HEIGHT // 2))

            pygame.display.update()


    def menu_screen():
        menu_surface = pygame.Surface((WIDTH, HEIGHT))
        WIN.blit(menu_surface, (0, 0))
        WIN.blit(TITLE_IMAGE, (0, 0))
        menu_font = pygame.font.Font(None, 60)
        text = menu_font.render(f"High Score: {previous}", True, WHITE)
        text_rect = text.get_rect()
        text_rect.center = (WIDTH // 2, HEIGHT // 2)
        menu_text_surface = pygame.Surface((text_rect.width + 20, text_rect.height + 20))
        menu_text_surface.fill(GREEN)
        menu_text_surface.blit(text, (10, 10))
        pygame.draw.rect(menu_text_surface, WHITE, menu_text_surface.get_rect(), 5)
        menu_text_rect = menu_text_surface.get_rect()
        menu_text_rect.center = (WIDTH // 2, HEIGHT // 2 + 150)
        WIN.blit(text, (120, HEIGHT // 2 - 300))
        pygame.display.update()

        menu = True
        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        menu = False
        main(Slime_X, Slime_Y)


    menu_screen()


__main__()
