import pygame
import random
pygame.init()

xy = 500
rows = 25
vel = 20
score = 0
possibleFoodPos = []
positions = []
last_key = ""

win = pygame.display.set_mode((xy,xy))
pygame.display.set_caption("Snake Game")

YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()

for n in range(0, 25):
    possibleFoodPos.append(n*20)


class Snake:
    def __init__(self, x, y, width, height, vel, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.color = color
        self.rect = (x,y,width,height)
        self.rectangle = pygame.Rect(self.rect)

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        global last_key
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and self.x >= 0:
            self.x -= self.vel
            last_key = 'a'
        elif keys[pygame.K_d] and self.x <= xy - self.width:
            self.x += self.vel
            last_key = 'd'
        elif keys[pygame.K_w] and self.y >= 0:
            self.y -= self.vel
            last_key = 'w'
        elif keys[pygame.K_s] and self.y <= xy - self.height:
            self.y += self.vel
            last_key = 's'
        else:
            if last_key == 'a' and self.x >= 0:
                self.x -= self.vel
                last_key = 'a'
            elif last_key == 'd' and self.x <= xy - self.width:
                self.x += self.vel
                last_key = 'd'
            elif last_key == 'w' and self.y >= 0:
                self.y -= self.vel
                last_key = 'w'
            elif last_key == 's' and self.y <= xy - self.height:
                self.y += self.vel
                last_key = 's'

        self.update()

    def drawGrid(self,win,rows,xy):
        spaceBtwn = xy // rows
        x = 0
        y = 0

        for l in range(rows):
            x = x + spaceBtwn
            y = y + spaceBtwn

            pygame.draw.line(win,(0, 0, 0), (x, 0), (x, xy))
            pygame.draw.line(win, (0, 0, 0), (0, y), (xy, y))

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

    def makeNewHead(self):
        pass

    def fillHeadPos(self,headPos):
        pass


class Food:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.a = 20
        self.color = YELLOW
        self.rect = (x,y,self.a,self.a)
        self.rectangle = pygame.Rect(self.rect)

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def makeNewPos(self):
        self.x = random.choice(possibleFoodPos)
        self.y = random.choice(possibleFoodPos)
        self.update()

    def update(self):
        self.rect = (self.x,self.y,self.a,self.a)
        self.rectangle = pygame.Rect(self.rect)


P = Snake(200,200,20,20,vel,GREEN)
food = Food(120,100)


def redrawGameWindow():
    #Redraw Window
    win.fill(WHITE)
    P.draw(win)
    P.drawGrid(win, rows, xy)
    food.draw(win)
    pygame.display.update()


def checkIfOut(x,y):
    #Check Right
    if x >= xy:
        return False
    #Check Left
    elif x < 0:
        return False
    #Check Up
    elif y < 0:
        return False
    #Check Down
    elif y >= xy:
        return False
    else:
        return True

clock = pygame.time.Clock()

#Main
def main():
    global score
    run = True
    while run:
        pygame.time.delay(50)
        speed = 7 + score
        clock.tick(speed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        if P.x == food.x and P.y == food.y:
            food.makeNewPos()
            score += 1
            print('Yummy! your score is now: ', score)
        P.move()
        redrawGameWindow()
        run = checkIfOut(P.x, P.y)
        if not run:
            print('Aww thats a shame!')


main()
