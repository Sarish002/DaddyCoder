
import random
import time
import math
import pygame


b = 0.002
pygame.init()
screen = pygame.display.set_mode((900, 700))
pygame.display.set_caption("Happy Father's Day!")
CL = pygame.time.Clock()
shown = True
music = pygame.mixer.music.load('father-111369.mp3')
pygame.mixer.music.play(-1, 0.0)
font = pygame.font.Font('CandyBeans-qnM5.ttf', 80)
fonts = pygame.font.Font('CandyBeans-qnM5.ttf', 40)
texts = font.render('Start!', True, 'black')
texts1 = fonts.render('1st Level --> Click 1', True, '#94ebff')
texts2 = fonts.render('2nd Level --> Click 2', True, '#94ff9f')
texts3 = fonts.render('3rd Level --> Click 3', True, '#ffcb94')
texts4 = fonts.render('4th Level --> Click 4', True, '#ff4d4d')

image = pygame.transform.scale(pygame.image.load('Boy.png'),
                               (200, 200))


while shown:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            shown = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            shown = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        b = 0.001
        sound = pygame.mixer.Sound('game-over-39-199830.mp3')
        sound.play()

    if keys[pygame.K_2]:
        b = 0.002
        sound = pygame.mixer.Sound('game-over-39-199830.mp3')
        sound.play()

    if keys[pygame.K_3]:
        b = 0.003
        sound = pygame.mixer.Sound('game-over-39-199830.mp3')
        sound.play()

    if keys[pygame.K_4]:
        b = 0.004
        sound = pygame.mixer.Sound('game-over-39-199830.mp3')
        sound.play()


    screen.fill((255, 255, 255))
    screen.blit(texts, (620, 450))

    screen.blit(texts1, (40, 264))
    screen.blit(texts2, (40, 328))
    screen.blit(texts3, (40, 392))
    screen.blit(texts4, (40, 456))


    screen.blit(image, (620, 200))
    pygame.display.update()

    CL.tick(60)

i = 1
z = 0


r = 10
c = 0
j = c
x = 0

pygame.init()
screen = pygame.display.set_mode((900, 650))
running = True
CL = pygame.time.Clock()
Y_GRAVITY = 4
JUMPHEIGHT = 50
Y_VELOCITY = 50
lives = 5

image = pygame.transform.scale(pygame.image.load('Boy.png'),
                               (90, 90))

imagerect = image.get_rect(center=(250, 472))
imagerect2 = image.get_rect(center=(900, random.choice([430, 440, 450, 460, 470, 480, 490, 500, 510, 520])))
imagerect3 = image.get_rect(center=(900, 440))

pygame.display.flip()
jumping = False
while running:
    text2 = font.render(f'Lives: {math.floor(lives)}', True, 'black')
    text = font.render(f'Hearts: {math.ceil(j / 17)}', True, 'black')

    imagerect2.x -= r
    r += b
    if imagerect2.x <= -200:
        imagerect2.x = 900
        imagerect2.y = random.choice([430, 440, 450, 460, 470, 480, 490, 500, 510, 520])
        i += 1

        imagerect2 = image.get_rect(center=(900, 440))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        jumping = True

    if jumping:
        imagerect.y -= Y_VELOCITY
        Y_VELOCITY -= Y_GRAVITY
        if Y_VELOCITY < -JUMPHEIGHT:
            jumping = False
            Y_GRAVITY = 4
            JUMPHEIGHT = 50
            Y_VELOCITY = 50

    screen.fill('white')

    pygame.draw.line(screen,
                     'black',
                     (0, 506),
                     (1500, 506),
                     5)

    if i % 4 == 0:
        pyimage = pygame.image.load('Heart.png')
        pyimage = pygame.transform.scale(pyimage, (80, 80))

        screen.blit(pyimage, imagerect2)
        if imagerect.colliderect(imagerect2):
            j += 1


    else:
        pyimage = pygame.image.load('My first design 75.png')
        pyimage = pygame.transform.scale(pyimage, (25, 25))

        screen.blit(pyimage, imagerect2)
        if imagerect.colliderect(imagerect2):
            lives -= 1 / 17

    screen.blit(image, imagerect)
    screen.blit(text, (275, 200))
    screen.blit(text2, (275, 100))
    pygame.display.update()
    if math.floor(lives) <= 0:

        running = False
        screen = pygame.display.set_mode((900, 650))
        active = True
        CL = pygame.time.Clock()
        pygame.display.flip()
        image2 = pygame.transform.scale(pygame.image.load('Boy.png'),
                                        (150, 150))
        imagerect4 = image2.get_rect(center=(430, 470))
        image3 = pygame.transform.scale(pygame.image.load('download.png'),
                                        (150, 150))
        imagerect5 = image2.get_rect(center=(370, 120))
        texti = pygame.font.Font('DancingMinotaur-d9JVR.ttf',
                                 100).render(f"Happy Father's Day!",
                                             True, 'black')
        textj = pygame.font.Font('CandyBeans-qnM5.ttf',
                                 100).render(f": {int(j / 17)}",
                                             True, 'black')
        pymus = pygame.mixer.music.load('happy-loop-6978.mp3')
        pygame.mixer.music.play(-1, 0.0)
        pygame.display.flip()
        while active:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    active = False

                elif keys[pygame.K_y]:
                    break
                    showing = True
            screen.fill('white')
            screen.blit(image2, imagerect4)
            screen.blit(image3, imagerect5)
            screen.blit(texti, (56, 200))
            screen.blit(textj, (470, 60))

            pygame.display.update()
            z += 1
            CL.tick(60)
    CL.tick(60)

pygame.quit()
