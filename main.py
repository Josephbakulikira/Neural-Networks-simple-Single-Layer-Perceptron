import pygame
from Perceptron import *
from Point import *
import random

width, height = 1000, 1000
size = (width, height)
black, blue, white = (10, 10, 10), (1, 159, 255), (255,255,255)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Neural networks")
clock = pygame.time.Clock()
fps = 30

points = []

for i in range(100):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    breed = 0
    if x > y:
        breed = 1
    else:
        breed = -1
    points.append(Point(x, y, breed))


perceptron = Perceptron()
inputs = [-1, 0.5]
prediction = perceptron.predict(inputs)
# print(prediction)

run = True
while run:
    screen.fill(black)
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.draw.line(screen, white, (0, 0), (size), 2)

    for point in points:
        point.Display(screen)
        desired = point.breed
         perceptron.train(point.GetInputs(), desired)
        guess = perceptron.predict(point.GetInputs())
        if desired == guess:
            pygame.draw.circle(screen, white, (point.x, point.y), 4)
        else:
            pygame.draw.circle(screen, blue, (point.x, point.y), 4)


    pygame.display.update()
pygame.quit()
