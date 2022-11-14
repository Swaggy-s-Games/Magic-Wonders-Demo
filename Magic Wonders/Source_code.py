import pygame
import random
import json

pygame.init()

pygame.display.set_caption('Magic @itsswaggy')
icon = pygame.image.load('crystal-ball.png')
pygame.display.set_icon(icon)

screen = pygame.display.set_mode((800, 600))

bg = pygame.image.load('bg.png')

bulletL = pygame.image.load('bulletL.png')
bulletR = pygame.image.load('bulletR.png')
bulletUp = pygame.image.load('bulletUp.png')
bulletDown = pygame.image.load('bulletDown.png')

bulletLhit = bulletL.get_rect()
bulletRhit = bulletR.get_rect()
bulletUphit = bulletUp.get_rect()
bulletDownhit = bulletDown.get_rect()

bulletRhit.x = 900
bulletLhit.x = -100
bulletUphit.y = -100
bulletDownhit.y = 700

L = pygame.image.load('playerL.png')
R = pygame.image.load('playerR.png')
bulletVel = 2

score = 0
highscore = 0
font = pygame.font.Font('Bubblegum.ttf', 22)
def show_score():
    score_value = font.render('Score: ' + str(score), True, (255,255,255))
    screen.blit(score_value, (345, 20))
def high_score():
    highscore_value = font.render('Highscore: ' + str(highscore), True, (255,255,255))
    screen.blit(highscore_value, (323, 40))

playerImg = R
hitbox = playerImg.get_rect()
vel = 1
hitbox.x = 368
hitbox.y = 268

ogreL = pygame.image.load('ogreL.png')
ogreR = pygame.image.load('ogreR.png')
ogreImg = ogreR
ogreHit = ogreImg.get_rect()
ogreVel = 1

speedImg = pygame.image.load('speed.png')
speedHit = speedImg.get_rect()
speedCounter1 = 960
speedCounter2 = 0
speedHit.x = random.randint(1,736)
speedHit.y = random.randint(1,536)

gunImg = pygame.image.load('gun.png')
gunHit = gunImg.get_rect()
gunCounter1 = 960
gunCounter2 = 0
gunHit.x = random.randint(1,736)
gunHit.y = random.randint(1,536)

checkUp = False
checkR = False
checkDown = False
checkL = False
ocheckR = True
ocheckL = False
scheck = True
nospam = False

with open('data.txt') as highscoreData:
    highscore = json.load(highscoreData)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_RIGHT]:
        hitbox.x += vel
        playerImg = R
        checkR = True
        checkDown = False
        checkL = False
        checkUp = False
    if userInput[pygame.K_LEFT]:
        hitbox.x -= vel
        playerImg = L
        checkR = False
        checkDown = False
        checkL = True
        checkUp = False
    if userInput[pygame.K_UP]:
        hitbox.y -= vel
        checkR = False
        checkDown = False
        checkL = False
        checkUp = True
    if userInput[pygame.K_DOWN]:
        hitbox.y += vel
        checkR = False
        checkDown = True
        checkL = False
        checkUp = False
    if userInput[pygame.K_SPACE] and checkL == True and bulletLhit.x < -90 and bulletRhit.x > 880 and bulletUphit.y < -90 and bulletDownhit.y > 680:
        bulletLhit.x = hitbox.x
        bulletLhit.y = hitbox.y
    if userInput[pygame.K_SPACE] and checkR == True and bulletRhit.x > 880 and bulletLhit.x < -90 and bulletUphit.y < -90 and bulletDownhit.y > 680:
        bulletRhit.x = hitbox.x
        bulletRhit.y = hitbox.y
    if userInput[pygame.K_SPACE] and checkUp == True and bulletUphit.y < -90 and bulletLhit.x < -90 and bulletDownhit.y > 680 and bulletRhit.x > 880:
        bulletUphit.x = hitbox.x
        bulletUphit.y = hitbox.y
    if userInput[pygame.K_SPACE] and checkDown == True and bulletDownhit.y > 680 and bulletLhit.x < -90 and bulletUphit.y < -90 and bulletRhit.x > 880:
        bulletDownhit.x = hitbox.x
        bulletDownhit.y = hitbox.y

    if bulletLhit.x > -100:
        bulletLhit.x -= bulletVel

    if bulletRhit.x < 900:
        bulletRhit.x += bulletVel

    if bulletUphit.y > -100:
        bulletUphit.y -= bulletVel
    
    if bulletDownhit.y < 700:
        bulletDownhit.y += bulletVel
    
    if ogreHit.x < 800 and ocheckR == True and ocheckL == False:
        ogreImg = ogreR
        ogreHit.x += ogreVel
    
    if ogreHit.x > -64 and ocheckR == False and ocheckL == True:
        ogreImg = ogreL
        ogreHit.x -= ogreVel
    
    if speedCounter2 == 0:
        vel = 1
    
    if speedCounter2 > 0:
        vel = 2

    if gunCounter2 == 0:
        bulletVel = 2
    
    if gunCounter2 > 0:
        bulletVel = 4
    
    if ogreHit.x == 800:
        ogreHit.y = random.randint(0,536)
        ocheckR = False
        ocheckL = True
    
    if ogreHit.x == -64:
        ogreHit.y = random.randint(0,536)
        ocheckR = True
        ocheckL = False

    if hitbox.y <= 5:
        hitbox.y = 5
    elif hitbox.y >= 516:
        hitbox.y = 516
        
    if hitbox.x <= 0:
        hitbox.x = 0
    elif hitbox.x >= 736:
        hitbox.x = 736

    if bulletRhit.colliderect(ogreHit):
        ogreHit.y = -64
        score += 1

    if bulletLhit.colliderect(ogreHit):
        ogreHit.y = -64
        score += 1

    if bulletUphit.colliderect(ogreHit):
        ogreHit.y = -1000
        score += 1
    
    if bulletDownhit.colliderect(ogreHit):
        ogreHit.y = -1000
        score += 1
    
    if hitbox.colliderect(ogreHit):
        with open('data.txt', 'w') as highscoreData:
            json.dump(highscore,highscoreData)
        pygame.quit()

    if hitbox.colliderect(speedHit) and speedCounter1 == 0:
        speedCounter2 += 1000
        speedCounter1 = 960
        speedHit.x = random.randint(0,736)
        speedHit.y = random.randint(0,536)
    
    if hitbox.colliderect(gunHit) and gunCounter1 == 0:
        gunCounter2 += 1000
        gunCounter1 = 960
        gunHit.x = random.randint(0,736)
        gunHit.y = random.randint(0,536)
    
    if speedCounter2 > 0:
        speedCounter2 -= 1
    
    if speedCounter1 > 0:
        speedCounter1 -= 1
    
    if gunCounter2 > 0:
        gunCounter2 -= 1
    
    if gunCounter1 > 0:
        gunCounter1 -= 1
    
    if score > highscore:
        highscore = score

    screen.blit(bg, (0,0))
    screen.blit(bulletR, bulletRhit)
    screen.blit(bulletL, bulletLhit)
    screen.blit(bulletUp, bulletUphit)
    screen.blit(bulletDown, bulletDownhit)
    screen.blit(playerImg, hitbox)
    screen.blit(ogreImg, ogreHit)

    if speedCounter1 == 0:
        screen.blit(speedImg, speedHit)
    
    if gunCounter1 ==0:
        screen.blit(gunImg, gunHit)

    high_score()
    show_score()

    pygame.time.delay(3)
    pygame.display.update()