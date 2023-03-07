def __main__():
    import pygame
    import os
    import random
    import time
    pygame.font.init()
    # Made by Caleb Greene
    # Welcome to the code! This was all created by me and as of now it is still in the early alpha testing.
    #  sets window
    width, height = 500, 700
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("The Spear-ocalypse!")
    #  starting slime cords
    slime_x = 175
    slime_y = 500
    #  define colors
    sky = (0, 220, 220)
    white = (255, 255, 255)
    black = (0, 0, 0)
    green = (0, 255, 0)
    #  frame rate (don't recommend changing) standard 60
    fps = 60
    #  defines images
    title_image = pygame.image.load(os.path.join
                                    ('Assets', '/Users/calebgreene/Desktop/folder of folders/Sprites/Title Screen.png'))

    death_image = pygame.image.load(os.path.join
                                    ('Assets', '/Users/calebgreene/Desktop/folder of folders/Sprites/DeadScreen.png'))

    spear_image = pygame.image.load(os.path.join
                                    ('Assets', '/Users/calebgreene/Desktop/folder of folders/Sprites/SIMPLE SPEAR.png'))

    spear_image = pygame.transform.scale(spear_image, (30, 180))

    sun_image = pygame.image.load(os.path.join
                                  ('Assets', '/Users/calebgreene/Desktop/folder of folders/Sprites/Simple Sun.png'))

    sun_image = pygame.transform.scale(sun_image, (200, 200))

    ground_image = pygame.image.load(os.path.join
                                     ('Assets', '/Users/calebgreene/Desktop/folder '
                                                'of folders/Sprites/Simple Ground.png'))

    ground_image = pygame.transform.scale(ground_image, (200, 200))

    slime_image = pygame.image.load(os.path.join
                                    ('Assets', '/Users/calebgreene/Desktop/folder of folders/Sprites/Simple Slime.gif'))
    slime_image = pygame.transform.scale(slime_image, (150, 150))

    previous = 0
    #  code tries to read the file. If the file is not found creates a new file and reads it again.
    try:
        with open('Score.txt', 'r') as read:
            for line in read.readlines():
                previous = int(round(float(line), 0))
    except FileNotFoundError:
        with open('Score.txt', 'w'):
            pass
        with open('Score.txt', 'r') as read:
            for line in read.readlines():
                previous = int(round(float(line), 0))

    def display_loss_message():
        win.blit(death_image, (0, 0))
        pygame.display.update()
        time.sleep(3)

    def draw_window(spear, x):
        win.fill(sky)
        win.blit(ground_image, (0, 600))
        win.blit(ground_image, (200, 600))
        win.blit(ground_image, (400, 600))
        win.blit(sun_image, (-60, -60))
        win.blit(spear_image, (x, spear))

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
            clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
            keys = pygame.key.get_pressed()
            while y < 501:
                y += 1
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                if x < 400:
                    x += speed
                else:
                    pass
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                if x > -40:
                    x -= speed
                else:
                    pass
            if keys[pygame.K_ESCAPE]:
                exit()
            win.fill(sky)
            draw_window(spear_y, spear_x)
            win.blit(slime_image, (x, y))
            if spear_y < 425:
                spear_y += velocity
            else:
                spear_y = -400
                spear_x = random.randint(0, 500)
            rect = spear_image.get_rect()
            rect.center = (spear_x, spear_y)
            collide = rect.colliderect(slime_image.get_rect())
            if collide:
                pass
            if spear_y >= 400 and x + 70 >= spear_x >= x:
                early = 0

                with open('Score.txt', 'r') as r:
                    for line1 in r.readlines():
                        early = float(line1)
                if t > early:
                    os.remove("Score.txt")
                    with open('Score.txt', 'w') as write:
                        write.write(str(t))
                display_loss_message()
                __main__()

            if spear_y >= 400 and x + 100 >= spear_x >= x:
                early = 0

                with open('Score.txt', 'r') as r:
                    for line2 in r.readlines():
                        early = float(line2)
                if t > early:
                    os.remove("Score.txt")
                    with open('Score.txt', 'w') as write:
                        write.write(str(t))
                display_loss_message()
                __main__()
            velocity += 0.005
            t += 0.0167
            speed += 0.005
            menu_font = pygame.font.Font(None, 60)
            text = menu_font.render(f"{int(round(t, 0))}", True, white)
            text_rect = text.get_rect()
            text_rect.center = (width // 2, height // 2 - 50)

            menu_text_surface = pygame.Surface((text_rect.width + 20, text_rect.height + 20))
            menu_text_surface.fill(green)
            menu_text_surface.blit(text, (10, 10))
            pygame.draw.rect(menu_text_surface, black, menu_text_surface.get_rect(), 5)
            menu_text_surface = pygame.transform.scale(menu_text_surface, (text_rect.width + 20, text_rect.height + 20))
            menu_text_surface = pygame.transform.scale(menu_text_surface, (text_rect.width + 20, text_rect.height + 20))

            menu_text_rect = menu_text_surface.get_rect()
            menu_text_rect.center = (width // 2, height // 2 + 150)
            win.blit(text, (width // 2, height // 2))

            pygame.display.update()

    def menu_screen():
        menu_surface = pygame.Surface((width, height))
        win.blit(menu_surface, (0, 0))
        win.blit(title_image, (0, 0))
        menu_font = pygame.font.Font(None, 60)
        text = menu_font.render(f"High Score: {previous}", True, white)
        text_rect = text.get_rect()
        text_rect.center = (width // 2, height // 2)
        menu_text_surface = pygame.Surface((text_rect.width + 20, text_rect.height + 20))
        menu_text_surface.fill(green)
        menu_text_surface.blit(text, (10, 10))
        pygame.draw.rect(menu_text_surface, white, menu_text_surface.get_rect(), 5)
        menu_text_rect = menu_text_surface.get_rect()
        menu_text_rect.center = (width // 2, height // 2 + 150)
        win.blit(text, (120, height // 2 - 300))
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
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()
        main(slime_x, slime_y)

    menu_screen()


__main__()
