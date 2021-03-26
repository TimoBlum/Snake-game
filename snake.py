import pygame, random

pygame.init()

xy = 500
rows = 25
vel = 20
Frame = 0
possibleFoodPos = []
snakes = []
lastPositions = []
last_key = ""
clock = pygame.time.Clock()
run = True
difficulty = 10
counter = 0
lost = False

win = pygame.display.set_mode((xy, xy))
pygame.display.set_caption("Snake Game")

YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

for n in range(0, 25):
    possibleFoodPos.append(n * 20)


def yn(a, c):
    # decide if something, whether float or int is the same number
    b = a // c
    bb = a / c
    if b - bb == 0:
        return True
    else:
        return False


class Snake:
    def __init__(self, head):
        self.head = head
        self.x = 200
        self.y = 200
        if not self.head:
            self.x = -20
            self.y = -20
        self.width = 20
        self.height = 20
        self.vel = vel
        self.counter = counter - 1
        self.color = GREEN
        self.rect = (self.x, self.y, self.width, self.height)
        self.rectangle = pygame.Rect(self.rect)

    def draw(self):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        global last_key
        keys = pygame.key.get_pressed()
        if self.head:
            if keys[pygame.K_a] and last_key != "d":
                if yn(Frame, difficulty):
                    self.x -= self.vel
                last_key = 'a'
            elif keys[pygame.K_d] and last_key != "a":
                if yn(Frame, difficulty):
                    self.x += self.vel
                last_key = 'd'
            elif keys[pygame.K_w] and last_key != "s":
                if yn(Frame, difficulty):
                    self.y -= self.vel
                last_key = 'w'
            elif keys[pygame.K_s] and last_key != "w":
                if yn(Frame, difficulty):
                    self.y += self.vel
                last_key = 's'
            else:
                if last_key == 'a':
                    if yn(Frame, difficulty):
                        self.x -= self.vel
                    last_key = 'a'
                elif last_key == 'd':
                    if yn(Frame, difficulty):
                        self.x += self.vel
                    last_key = 'd'
                elif last_key == 'w':
                    if yn(Frame, difficulty):
                        self.y -= self.vel
                    last_key = 'w'
                elif last_key == 's':
                    if yn(Frame, difficulty):
                        self.y += self.vel
                    last_key = 's'
        elif not self.head:
            if yn(Frame, difficulty):
                self.x = lastPositions[self.counter][0]
                self.y = lastPositions[self.counter][1]
                print(lastPositions)
        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)


def drawGrid():
    global rows
    spaceBtwn = xy // rows
    x = 0
    y = 0

    for l in range(rows):
        x = x + spaceBtwn
        y = y + spaceBtwn

        pygame.draw.line(win, (0, 0, 0), (x, 0), (x, xy))
        pygame.draw.line(win, (0, 0, 0), (0, y), (xy, y))


class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.a = 20
        self.color = YELLOW
        self.rect = (x, y, self.a, self.a)

    def draw(self):
        pygame.draw.rect(win, self.color, self.rect)

    def makeNewPos(self):
        self.x = random.choice(possibleFoodPos)
        self.y = random.choice(possibleFoodPos)
        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.a, self.a)


snakes.append(Snake(True))
food = Food(random.choice(possibleFoodPos), random.choice(possibleFoodPos))


def makeNewLastPos():
    lst = []
    for s in snakes:
        lst.append((s.x, s.y))
    return lst


def redrawGameWindow():
    global lastPositions
    win.fill(WHITE)
    lastPositions = makeNewLastPos()
    for s in snakes:
        s.move()
        s.update()
        s.draw()
    food.draw()
    drawGrid()
    checkIfOut(snakes[0].x, snakes[0].y)
    if lost:
        win.fill((255, 0, 0))
    pygame.display.update()


def checkIfOut(x, y):
    global lost
    # Check borders of screen
    if x >= xy or x < 0 or y >= xy or y < 0:
        lost = True
    # Check for Snake Collision
    for s in lastPositions[1:]:
        if s == lastPositions[0]:
            lost = True


# Main
def main():
    global Frame, run, difficulty, counter
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        if snakes[0].x == food.x and snakes[0].y == food.y:
            food.makeNewPos()
            counter += 1
            snakes.append(Snake(False))
            if difficulty >= 7:
                difficulty -= 1

        Frame += 1
        if run:
            redrawGameWindow()


main()
