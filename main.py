# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame
import random

pygame.init()
winWidth = 900
winHeight = 504
screen = pygame.display.set_mode([winWidth, winHeight])

wing = pygame.mixer.Sound("sound/wing.mp3")
point = pygame.mixer.Sound("sound/point.mp3")
hit = pygame.mixer.Sound("sound/hit.mp3")
bg = pygame.image.load("img/flappyBird.png")
pipe = pygame.image.load("img/pipe.png").convert_alpha()
bird = pygame.image.load("img/bird.png").convert_alpha()
bird = pygame.transform.scale(bird, (80, 80))
pipe = pygame.transform.scale(pipe, (400, 800))
score = 0
blue = (0, 0, 255)
# setting the pygame font style(1st parameter)
# and size of font(2nd parameter)

# define the RGB value for white,
# green, yellow, orange colour

yellow = (255, 255, 0)
font = pygame.font.Font('freesansbold.ttf', 22)

class Pipe:

    def __init__(self):
        random.seed(None)
        self.y = random.randrange(-300, 0, 8)
        self.x = 900

    def mov(self):
        self.x = self.x-5
        if self.x == -400:
            self.x = 900
            self.y = random.randrange(-300, 0, 8)



class Bird:

    def __init__(self):
        self.x = 30
        self.y = 250

    def drop(self):
        self.y = self.y + 6

    def jump(self):
        self.y = self.y - 60
        wing.play()


def collide(b, p):
    if (b.y - p.y < 345 or b.y - p.y > 445) and (b.x - p.x > 130 and b.x - p.x < 210):
        hit.play()
        return True
    else:
        return False

def through(p):
    if p.x == -180:
        point.play()
        return True


running = True
p1 = Pipe()
p2 = Pipe()
p3 = Pipe()
p4 = Pipe()
p5 = Pipe()
p2.x = p1.x + 250
p3.x = p2.x + 250
p4.x = p3.x + 250
p5.x = p4.x + 250
b1 = Bird()
clock = pygame.time.Clock()
gameover = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                b1.jump()
                print("Space is pressed")
            if event.key == pygame.K_RETURN:
                gameover = False
                p1 = Pipe()
                p2 = Pipe()
                p3 = Pipe()
                p4 = Pipe()
                p5 = Pipe()
                p2.x = p1.x + 250
                p3.x = p2.x + 250
                p4.x = p3.x + 250
                p5.x = p4.x + 250
                b1 = Bird()
                score = 0
    if not gameover:
        text = font.render('Score: ' + str(score), True, yellow)
        text.set_alpha(127)
        gameOver = font.render('Game Over', True, blue)
        gameOver.set_alpha(127)
        restart = font.render('Press Enter to restart', True, blue)
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))
        screen.blit(bird, (b1.x, b1.y))

        b1.drop()
        screen.blit(pipe, (p1.x, p1.y))
        screen.blit(pipe, (p2.x, p2.y))
        screen.blit(pipe, (p3.x, p3.y))
        screen.blit(pipe, (p4.x, p4.y))
        screen.blit(pipe, (p5.x, p5.y))
        screen.blit(text, (3, 3))
        print("B1Y: " + str(b1.y))
        print("P1X: " + str(p1.x) + " P1Y: " + str(p1.y))
        print("P2X: " + str(p2.x) + " P2Y: " + str(p2.y))
        print("P3X: " + str(p3.x) + " P3Y: " + str(p3.y))
        print("P4X: " + str(p4.x) + " P4Y: " + str(p4.y))
        print("P5X: " + str(p5.x) + " P5Y: " + str(p5.y))
        print(p1.y)
        print(b1.y)
        p1.mov()
        p2.mov()
        p3.mov()
        p4.mov()
        p5.mov()
        if collide(b1, p1) or collide(b1, p2) or collide(b1, p3) or collide(b1, p4) or collide(b1, p5):
            gameover = True
        if b1.y <= 0 or b1.y >= 490:
            gameover = True
        if through(p1) or through(p2) or through(p3) or through(p4) or through(p5):
            score = score + 1

        print(score)
    else:
        screen.blit(gameOver, (winWidth / 2 - 40, winHeight / 2))
        screen.blit(restart, (winWidth / 2 - 80, winHeight / 2 + 30))
    pygame.display.flip()
    clock.tick(30*(1+(score/10)*0.2))


pygame.quit()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
